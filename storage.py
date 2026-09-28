import json
import os

FILE_PATH = "data/students.json"


def create_data_file():
    """Create data folder and JSON file if they don't exist."""
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as file:
            json.dump([], file, indent=4)


def load_students():
    """Load student records from JSON file."""
    create_data_file()

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_students(students):
    """Save student records to JSON file."""
    create_data_file()

    with open(FILE_PATH, "w") as file:
        json.dump(students, file, indent=4)
