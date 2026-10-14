from pathlib import Path

# current working directory
root = Path(".")

# Folders to create
folders = [
    "app/api",
    "app/rag",
    "app/core",
    "app/services",
    "data",
    "templates",
    "static",
    "uploads",
    "tests"
]

# Files to create
files = [
    "app/main.py",
    "ingest_sample_kb.py",
    "run.py",
]


# create folders
for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)

# create files
for file in files:
    (root / file).touch(exist_ok=True)


print("Project Structure created successfully.")