"""Lesson 19: regular expressions and dates."""

import re
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
LOG_LINE = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) "
    r"(?P<level>[A-Z]+) (?P<message>.*)"
)


def extract_emails(text: str) -> list[str]:
    return EMAIL.findall(text)


def parse_log_line(line: str) -> dict[str, str] | None:
    match = LOG_LINE.fullmatch(line)
    return match.groupdict() if match else None


def days_between(start: str, end: str) -> int:
    return (date.fromisoformat(end) - date.fromisoformat(start)).days


def age_on(birth: date, on: date) -> int:
    had_birthday = (on.month, on.day) >= (birth.month, birth.day)
    return on.year - birth.year - (not had_birthday)


def convert_timezone(iso_local: str, from_tz: str, to_tz: str) -> str:
    local = datetime.fromisoformat(iso_local).replace(tzinfo=ZoneInfo(from_tz))
    return local.astimezone(ZoneInfo(to_tz)).isoformat()


def format_duration(delta: timedelta) -> str:
    minutes = int(delta.total_seconds()) // 60
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return f"{days}d {hours:02d}h {minutes:02d}m"
