import csv
from repos.constants import CSV_FILE, CSV_FIELDS


def read_users():
    users = []
    try:
        with open(CSV_FILE, "r") as f:
            reader = csv.DictReader(f, fieldnames=CSV_FIELDS)
            next(reader, None)  # skip the header row
            users = list(reader)
    except FileNotFoundError:
        pass
    return users
