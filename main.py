#!/usr/bin/env python3
"""Convert JSON arrays of objects to CSV and CSV tables to JSON."""
import argparse
import csv
import json
from pathlib import Path
from typing import Any


def flatten(value: Any, prefix: str = "", result: dict | None = None) -> dict:
    result = result if result is not None else {}
    if isinstance(value, dict) and value:
        for key, child in value.items():
            name = f"{prefix}.{key}" if prefix else str(key)
            flatten(child, name, result)
    elif prefix:
        result[prefix] = json.dumps(value, ensure_ascii=False) if isinstance(value, list) else value
    return result


def json_to_csv(source: Path, destination: Path) -> int:
    data = json.loads(source.read_text(encoding="utf-8-sig"))
    if not isinstance(data, list) or any(not isinstance(row, dict) for row in data):
        raise ValueError("JSON input must be an array of objects")
    rows = [flatten(row) for row in data]
    columns = list(dict.fromkeys(key for row in rows for key in row))
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        if columns:
            writer.writeheader()
            writer.writerows(rows)
    return len(rows)


def csv_to_json(source: Path, destination: Path) -> int:
    with source.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    destination.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return len(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    if not args.source.is_file():
        parser.error(f"input file does not exist: {args.source}")
    try:
        if args.source.suffix.lower() == ".json" and args.destination.suffix.lower() == ".csv":
            count = json_to_csv(args.source, args.destination)
        elif args.source.suffix.lower() == ".csv" and args.destination.suffix.lower() == ".json":
            count = csv_to_json(args.source, args.destination)
        else:
            parser.error("use a .json source with .csv output, or a .csv source with .json output")
        print(f"Converted {count} rows -> {args.destination}")
        return 0
    except (ValueError, json.JSONDecodeError, OSError) as exc:
        parser.error(str(exc))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
