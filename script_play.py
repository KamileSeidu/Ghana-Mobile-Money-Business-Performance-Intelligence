
from pathlib import Path

# Define the project root directory
PROJECT_ROOT = Path("data_analysis_project")

# Define the folder structure
folders = [
    "data/raw",
    "data/processed",
    "data/reference",
    "excel",
    "sql",
    "python",
    "powerbi",
    "reports",
    "docs"
]

# Create the folders
for folder in folders:
    (PROJECT_ROOT / folder).mkdir(parents=True, exist_ok=True)

print(f"Project folder structure created successfully at: {PROJECT_ROOT.resolve()}")
