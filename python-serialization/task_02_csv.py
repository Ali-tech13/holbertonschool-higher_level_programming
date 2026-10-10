
#!/usr/bin/env python3
"""Module for converting CSV data to JSON."""

import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON and save it to data.json."""
    try:
        with open(filename, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True
    except (OSError, csv.Error, UnicodeError):
        return False
