
from pathlib import Path

LINE = "The alarm rang at 6 on a Saturday and then, smugly, hit snooze on itself. Even it knows this is a crime."

target = Path("/output/entry.txt")
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(LINE, encoding="utf-8")
