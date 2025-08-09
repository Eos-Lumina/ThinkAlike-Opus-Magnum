# This script sets up the development environment for the ThinkAlike project.

# Ensure pip is up to date
python -m pip install --upgrade pip

# Install dependencies from requirements.txt
if (Test-Path requirements.txt) {
    pip install -r requirements.txt
    Write-Host "Dependencies installed successfully."
} else {
    Write-Host "requirements.txt not found. Please ensure you are in the project root directory."
}

# Install pre-commit hooks
pre-commit install
Write-Host "Pre-commit hooks installed."
