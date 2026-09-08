import os
import sys


SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path = [path for path in sys.path if os.path.abspath(path or ".") != SCRIPT_DIRECTORY]

import csv
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any


FIELDNAMES = ["id", "customer", "amount", "paid"]
DELIMITER = ";"


def create_csv_with_writer(file_path: Path) -> None:
    """Write rows with csv.writer, headers, UTF-8, and a semicolon delimiter."""
    rows = [
        ["1", "Ana García", "125.50", "true"],
        ["2", "Luis", "", "false"],
        ["3", "Marta", "80.00", "true"],
    ]
    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=DELIMITER)
        writer.writerow(FIELDNAMES)
        writer.writerows(rows)


def create_csv_with_dict_writer(file_path: Path) -> None:
    """Write dictionaries with csv.DictWriter and explicit headers."""
    rows = [
        {"id": 4, "customer": "Diego", "amount": 42.75, "paid": True},
        {"id": 5, "customer": "Sofía", "amount": 19.90, "paid": False},
    ]
    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES, delimiter=DELIMITER)
        writer.writeheader()
        writer.writerows(rows)


def read_with_reader(file_path: Path) -> list[list[str]]:
    """Read rows as lists with csv.reader, separating the header."""
    with file_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=DELIMITER)
        headers = next(reader, [])
        rows = list(reader)
    print(f"csv.reader headers: {headers}")
    return rows


def convert_value(field: str, value: str | None) -> Any:
    """Convert CSV text to a useful Python type, preserving missing values."""
    if value in (None, ""):
        return None
    if field == "id":
        return int(value)
    if field == "amount":
        return float(value)
    if field == "paid":
        return value.lower() == "true"
    return value


def convert_row(row: dict[str, str | None]) -> dict[str, Any]:
    """Convert every field in one DictReader row."""
    return {
        field: convert_value(field, row.get(field))
        for field in FIELDNAMES
    }


def read_with_dict_reader(file_path: Path) -> list[dict[str, Any]]:
    """Read named columns with csv.DictReader and convert their types."""
    with file_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=DELIMITER)
        converted_rows = [convert_row(row) for row in reader]
    return converted_rows


def process_incrementally(file_path: Path) -> int:
    """Process one row at a time without building a list of all rows."""
    processed_rows = 0
    with file_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=DELIMITER)
        for row in reader:
            converted_row = convert_row(row)
            processed_rows += 1
            print(f"Incremental row {processed_rows}: {converted_row['id']}")
    return processed_rows


def inspect_empty_file(file_path: Path) -> None:
    """Handle an empty CSV without assuming that headers or rows exist."""
    with file_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=DELIMITER)
        first_row = next(reader, None)
    print(f"Empty file has data: {first_row is not None}")


def main() -> None:
    """Demonstrate CSV reading, writing, conversion, and incremental processing."""
    with TemporaryDirectory() as temporary_directory:
        directory = Path(temporary_directory)
        writer_file = directory / "orders.csv"
        dict_writer_file = directory / "new_orders.csv"
        empty_file = directory / "empty.csv"

        create_csv_with_writer(writer_file)
        create_csv_with_dict_writer(dict_writer_file)
        empty_file.write_text("", encoding="utf-8")

        rows = read_with_reader(writer_file)
        print(f"csv.reader first row: {rows[0]}")
        print(f"csv.DictReader converted rows: {read_with_dict_reader(writer_file)}")
        print(f"DictWriter output: {read_with_dict_reader(dict_writer_file)}")
        print(f"Rows processed incrementally: {process_incrementally(writer_file)}")
        inspect_empty_file(empty_file)


if __name__ == "__main__":
    main()