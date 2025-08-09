"""
Test Document Utilities
======================

This module tests the document_utils.py module.

Version: 1.0
Maintained by: Lumina∴ System Meta-Agent
"""

import unittest

from src.shared_utils.document_utils import (DocumentManager,
                                             DocumentProcessor,
                                             get_core_document_content)


class TestDocumentUtils(unittest.TestCase):
    """Test cases for document_utils.py"""

    def setUp(self):
        """Set up test environment"""
        self.base_dir = "c:/---ThinkAlike---"
        self.doc_manager = DocumentManager(self.base_dir)

    def test_build_document_index(self):
        """Test building document index"""
        index = self.doc_manager.build_document_index()
        self.assertIsNotNone(index)
        self.assertIn("by_path", index)
        self.assertIn("by_title", index)
        self.assertIn("by_tag", index)
        self.assertIn("by_status", index)
        self.assertIn("core_documents", index)

        # Verify we have documents
        self.assertGreater(len(index["by_path"]), 0)
        print(f"Found {len(index['by_path'])} documents")

    def test_get_core_documents(self):
        """Test getting core documents"""
        core_docs = self.doc_manager.get_core_documents()
        self.assertIsNotNone(core_docs)

        # Print core documents
        print(f"Found {len(core_docs)} core documents:")
        for doc in core_docs:
            print(f"- {doc['path']}")

    def test_search_documents(self):
        """Test searching documents"""
        results = self.doc_manager.search_documents("ThinkAlike")
        self.assertIsNotNone(results)
        self.assertGreater(len(results), 0)

        # Print search results
        print(f"Found {len(results)} documents containing 'ThinkAlike':")
        for result in results[:3]:  # Show top 3
            print(f"- {result['path']}")

    def test_get_document_by_title(self):
        """Test getting document by title"""
        doc = self.doc_manager.get_document_by_title(
            "Source of Truth — ThinkAlike Project"
        )
        self.assertIsNotNone(doc)
        self.assertIn("content", doc)
        self.assertIn("metadata", doc)

        # Print document info
        print(f"Found document: {doc['path']}")
        print(f"Title: {doc['metadata'].get('title')}")
        print(f"Status: {doc['metadata'].get('status')}")

    def test_find_documents_by_status(self):
        """Test finding documents by status"""
        docs = self.doc_manager.find_documents_by_status("core")
        self.assertIsNotNone(docs)

        # Print documents
        print(f"Found {len(docs)} core status documents:")
        for doc in docs[:3]:  # Show top 3
            print(f"- {doc['path']}")

    def test_analyze_document_links(self):
        """Test analyzing document links"""
        analysis = self.doc_manager.analyze_document_links()
        self.assertIsNotNone(analysis)
        self.assertIn("broken_wiki_links", analysis)
        self.assertIn("orphaned_documents", analysis)
        self.assertIn("most_linked", analysis)

        # Print analysis
        print(f"Found {len(analysis['broken_wiki_links'])} broken links")
        print(f"Found {len(analysis['orphaned_documents'])} orphaned docs")
        print("Most linked documents:")
        for doc in analysis["most_linked"][:3]:  # Show top 3
            print(f"- {doc['path']}: {doc['count']} links")

    def test_find_missing_documents(self):
        """Test finding missing documents"""
        missing = self.doc_manager.find_missing_documents()
        self.assertIsNotNone(missing)

        # Print missing documents
        print(f"Found {len(missing)} missing documents:")
        for doc in missing[:10]:  # Show top 10
            print(f"- {doc}")

    def test_generate_document_stats(self):
        """Test generating document statistics"""
        stats = self.doc_manager.generate_document_stats()
        self.assertIsNotNone(stats)
        self.assertIn("total_documents", stats)
        self.assertIn("total_words", stats)
        self.assertIn("status_counts", stats)

        # Print statistics
        print(f"Total documents: {stats['total_documents']}")
        print(f"Total words: {stats['total_words']}")
        print(f"Average words per document: {stats['avg_words_per_doc']:.2f}")
        print("Documents by status:")
        for status, count in stats["status_counts"].items():
            print(f"- {status}: {count}")

    def test_document_processor(self):
        """Test document processor"""
        processor = DocumentProcessor(self.doc_manager)
        self.assertIsNotNone(processor)

        # Test extracting sections from a document
        source_of_truth = "docs/00_context/source_of_truth.md"
        sections = processor.extract_sections(source_of_truth)
        self.assertIsNotNone(sections)

        # Print sections (safely handling Unicode)
        print(f"Found {len(sections)} sections in {source_of_truth}:")
        for section in sections:
            try:
                print(f"- {section}")
            except UnicodeEncodeError:
                print("- [Section with special characters]")

    def test_helper_functions(self):
        """Test helper functions"""
        content = get_core_document_content("SYSTEM_BLUEPRINT")
        self.assertIsNotNone(content)
        self.assertIn("ThinkAlike", content)


if __name__ == "__main__":
    unittest.main()
