# PowerShell script to safely clean up junk files in the workspace
# Deletes only .venv, __pycache__, .pyc, and duplicate/backup scripts (e.g., (2), (3) in name)
# Leaves .md, .txt, .zip, images, and other valuable files untouched

$root = "C:\ThinkAlike"

# Remove all .venv folders recursively
Get-ChildItem -Path $root -Directory -Recurse -Force -ErrorAction SilentlyContinue | Where-Object { $_.Name -eq ".venv" } | ForEach-Object { Remove-Item $_.FullName -Recurse -Force -ErrorAction SilentlyContinue }

# Remove all __pycache__ folders recursively
Get-ChildItem -Path $root -Directory -Recurse -Force -ErrorAction SilentlyContinue | Where-Object { $_.Name -eq "__pycache__" } | ForEach-Object { Remove-Item $_.FullName -Recurse -Force -ErrorAction SilentlyContinue }

# Remove all .pyc files recursively
Get-ChildItem -Path $root -Recurse -Include *.pyc -File -Force -ErrorAction SilentlyContinue | Remove-Item -Force -ErrorAction SilentlyContinue

# Remove duplicate/backup scripts (e.g., file (2).py, file (3).py, etc.) but NOT .md, .txt, .zip, images
$dupPattern = "*(*).py"
Get-ChildItem -Path $root -Recurse -Include $dupPattern -File -Force -ErrorAction SilentlyContinue | ForEach-Object {
    if ($_.Extension -eq ".py") {
        Remove-Item $_.FullName -Force -ErrorAction SilentlyContinue
    }
}

Write-Host "Cleanup complete. No .md, .txt, .zip, images, or valuable files were deleted."
