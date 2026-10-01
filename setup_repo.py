from pathlib import Path

folders = ["days", "src/grind", "tests", "data", "scripts", "notes", "capstone"]
for f in folders:
    Path(f).mkdir(parents=True, exist_ok=True)
    (Path(f) / ".gitkeep").touch()

Path("src/grind/__init__.py").touch()
Path("notes/notes.md").write_text("# Daily notes\n\n## Day 1\n")
Path("requirements.txt").touch()
Path(".gitignore").write_text("venv/\n.venv/\n__pycache__/\n*.pyc\ndata/big_*\n")
Path("README.md").write_text(
    "# daily-grind\n\n28 days of small Python problems.\n\n"
    "| Day | Topic | Done |\n|-----|-------|------|\n| 1 | Clean messy user input | |"
)
print("Done. Now run: git init")