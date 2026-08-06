"""
Updates the <!--LAST_SYNCED--> marker inside README.md with the current
UTC and IST timestamps every time the 'Update README Timestamp' workflow runs.
Keeps the profile visibly "alive" without touching any other content.
"""

import re
from datetime import datetime, timedelta, timezone

README_PATH = "README.md"
IST = timezone(timedelta(hours=5, minutes=30))

def main() -> None:
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    now_ist = datetime.now(IST).strftime("%d %b %Y, %H:%M IST")
    new_line = f"<!--LAST_SYNCED-->Last synced: {now_ist}<!--/LAST_SYNCED-->"

    pattern = r"<!--LAST_SYNCED-->.*?<!--/LAST_SYNCED-->"
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, new_line, content, flags=re.DOTALL)
    else:
        content += f"\n\n{new_line}\n"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    main()
