from datetime import datetime
from pathlib import Path

def generate_daily_plan():
    today = datetime.now().strftime("%Y-%m-%d")
    filename = Path(f"plans/{today}.md")
    filename.parent.mkdir(exist_ok=True)

    content = f"""# Daily Planner – {today}

## 📝 Top Priorities
- 

## 📞 Vendor Calls / Recruiters
- 

## 🚀 Project Work
- 

## 📚 Learning / Practice
- 

## ✔ Completed
- 
"""

    filename.write_text(content)
    print(f"Generated: {filename}")

if __name__ == "__main__":
    generate_daily_plan()
