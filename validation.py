def validate_marks(marks):
    """Check whether marks are between 0 and 100."""
    return 0 <= marks <= 100


def validate_roll_number(roll_no):
    """Check whether roll number is not empty."""
    return roll_no.strip() != ""


def validate_name(name):
    """Check whether name contains valid characters."""
    return name.strip() != ""


def get_valid_marks(subject):
    """Keep asking until valid marks are entered."""
    while True:
        try:
            marks = float(input(f"Enter {subject} marks (0-100): "))

            if validate_marks(marks):
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def get_valid_name():
    """Get a non-empty student name."""
    while True:
        name = input("Enter student name: ")

        if validate_name(name):
            return name.strip()

        print("Name cannot be empty.")


def get_valid_roll_number():
    """Get a non-empty roll number."""
    while True:
        roll_no = input("Enter roll number: ")

        if validate_roll_number(roll_no):
            return roll_no.strip()

        print("Roll number cannot be empty.")
