"""Lesson 18: JSON and CSV round trips."""

import csv
import io
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path


@dataclass
class Event:
    name: str
    when: date
    tags: list[str]


def to_json(data: dict) -> str:
    return json.dumps(data, indent=2, sort_keys=True)


def read_csv_rows(text: str) -> list[dict[str, str]]:
    # newline="" semantics: StringIO keeps embedded newlines in quoted fields
    return list(csv.DictReader(io.StringIO(text, newline="")))


def write_csv(rows: list[dict[str, str | int]], fieldnames: list[str]) -> str:
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()


def csv_to_json(csv_text: str, int_fields: list[str]) -> str:
    rows: list[dict] = read_csv_rows(csv_text)
    for row in rows:
        for field in int_fields:
            row[field] = int(row[field])
    return json.dumps(rows, indent=2, sort_keys=True)


def encode_event(event: Event) -> str:
    return json.dumps(
        {"name": event.name, "when": event.when.isoformat(), "tags": event.tags}
    )


def decode_event(text: str) -> Event:
    raw = json.loads(text)
    return Event(raw["name"], date.fromisoformat(raw["when"]), raw["tags"])


def load_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    return json.loads(path.read_text())
