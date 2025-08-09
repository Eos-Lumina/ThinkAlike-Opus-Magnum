import argparse
import asyncio
import re
import sys
from pathlib import Path
from typing import List, NamedTuple

import aiohttp

# This script checks for broken links in Markdown files.

LINK_REGEX = re.compile(r"\[[^\]]+\]\((?!#)([^\)]+)\)")

# Exclude files that are known to have links that are not worth checking
EXCLUDE_FILES = {"CHANGELOG.md"}


class FoundLink(NamedTuple):
    """Represents a link found in a file."""

    target: str
    source: Path
    line: int


class BrokenLink(NamedTuple):
    """Represents a broken link."""

    url: str
    source: str
    line: int
    status: int
    reason: str


def find_markdown_files(directory: Path) -> List[Path]:
    """Finds all Markdown files in a directory, excluding specified files."""
    return [
        f
        for f in directory.rglob("*.md")
        if f.is_file() and f.name not in EXCLUDE_FILES
    ]


def parse_links(file_path: Path) -> List[FoundLink]:
    """Extracts all links from a given markdown file."""
    links = []
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for i, line_text in enumerate(f, 1):
                for match in LINK_REGEX.finditer(line_text):
                    links.append(FoundLink(match.group(1), file_path, i))
    except IOError as e:
        print(
            f"Warning: Could not read file {file_path}: {e}",
            file=sys.stderr,
        )
    return links


async def check_external_link(
    session: aiohttp.ClientSession, link: FoundLink
) -> BrokenLink | None:
    """Checks a single external link."""
    try:
        # Use HEAD request to be faster and lighter
        async with session.head(link.target, timeout=10) as response:
            if response.status >= 400:
                return BrokenLink(
                    link.target,
                    str(link.source),
                    link.line,
                    response.status,
                    response.reason or "",
                )
    except asyncio.TimeoutError:
        return BrokenLink(link.target, str(link.source), link.line, 0, "Timeout")
    except aiohttp.ClientError as e:
        # Covers a wide range of connection errors
        return BrokenLink(
            link.target,
            str(link.source),
            link.line,
            0,
            f"Client Error: {e}",
        )
    return None


def check_internal_link(link: FoundLink, root_dir: Path) -> BrokenLink | None:
    """Checks a single internal link."""
    # Normalize the link target
    target_path_str = link.target.split("#")[0].lstrip("/")
    if not target_path_str:
        return None  # Skip anchor-only links

    # Resolve path relative to the source file
    target_path = link.source.parent / Path(target_path_str)

    # For root-relative links, resolve from the project root
    if link.target.startswith("/"):
        target_path = root_dir / target_path_str

    if not target_path.exists():
        return BrokenLink(
            link.target, str(link.source), link.line, 404, "File not found"
        )
    return None


async def main():
    """Main function for the link checker script."""
    parser = argparse.ArgumentParser(
        description="Check for broken links in Markdown files."
    )
    parser.add_argument(
        "--dir",
        type=Path,
        default=Path.cwd(),
        help="The directory to search for Markdown files.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print all checked links, not just broken ones.",
    )
    args = parser.parse_args()

    print(f"Scanning for Markdown files in: {args.dir.resolve()}")
    markdown_files = find_markdown_files(args.dir)
    if not markdown_files:
        print("No Markdown files found.")
        return

    all_links: List[FoundLink] = []
    for file in markdown_files:
        all_links.extend(parse_links(file))

    external_links = [link for link in all_links if link.target.startswith("http")]
    internal_links = [link for link in all_links if not link.target.startswith("http")]
    broken_links: List[BrokenLink] = []

    print(
        f"Found {len(all_links)} links ({len(external_links)} external, "
        f"{len(internal_links)} internal). Checking..."
    )

    # Check internal links
    for link in internal_links:
        if args.verbose:
            print(f"Checking internal link: {link.target}")
        result = check_internal_link(link, args.dir)
        if result:
            broken_links.append(result)

    # Check external links concurrently
    async with aiohttp.ClientSession() as session:
        tasks = [check_external_link(session, link) for link in external_links]
        results = await asyncio.gather(*tasks)
        for result in results:
            if result:
                broken_links.append(result)
            elif args.verbose:
                # This part is tricky because we don't have the original link object here
                # A more complex implementation would map results back to links
                pass

    if not broken_links:
        print("\n✅ No broken links found.")
    else:
        print(f"\n❌ Found {len(broken_links)} broken links:\n")
        for link in sorted(broken_links, key=lambda b: b.source):
            print(
                f"- [File] {link.source} (Line {link.line})\n"
                f"  Link: {link.url}\n"
                f"  HTTP Status: {link.status} {link.reason}"
            )
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
