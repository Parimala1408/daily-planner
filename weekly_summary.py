from pathlib import Path

def generate_week_summary():
    files = sorted(Path("plans").glob("*.md"))
    summary = Path("plans/weekly_summary.md")

    content = "# Weekly Summary\n\n"

    for f in files:
        content += f"- {f.name}\n"

    summary.write_text(content)
    print("Generated weekly summary.")

if __name__ == "__main__":
    generate_week_summary()
