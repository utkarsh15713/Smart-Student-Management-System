from validation import (
    get_valid_name,
    get_valid_roll_number,
    get_valid_marks
)

from marks import get_performance
from storage import save_students


SUBJECTS = ["Maths", "Physics", "Chemistry", "Python"]


def find_student(students, roll_no):
    """Find a student using roll number."""
    for student in students:
        if student["roll_no"] == roll_no:
            return student

    return None


def add_student(students):
    """Add a new student."""
    print("\n========== ADD STUDENT ==========")

    roll_no = get_valid_roll_number()

    if find_student(students, roll_no):
        print("A student with this roll number already exists.")
        return

    name = get_valid_name()

    branch = input("Enter branch: ").strip()

    if branch == "":
        branch = "CSE"

    marks = {}

    for subject in SUBJECTS:
        marks[subject] = get_valid_marks(subject)

    performance = get_performance(marks)

    student = {
        "roll_no": roll_no,
        "name": name,
        "branch": branch,
        "marks": marks,
        "total": performance["total"],
        "percentage": performance["percentage"],
        "grade": performance["grade"],
        "status": performance["status"]
    }

    students.append(student)
    save_students(students)

    print("\nStudent added successfully!")


def display_student(student):
    """Display complete student information."""
    print("\n----------------------------------------")
    print(f"Roll Number : {student['roll_no']}")
    print(f"Name        : {student['name']}")
    print(f"Branch      : {student['branch']}")

    print("\nMarks:")
    for subject, mark in student["marks"].items():
        print(f"{subject:<12}: {mark}")

    print(f"\nTotal       : {student['total']}")
    print(f"Percentage  : {student['percentage']:.2f}%")
    print(f"Grade       : {student['grade']}")
    print(f"Status      : {student['status']}")
    print("----------------------------------------")


def view_students(students):
    """Display all students."""
    print("\n========== ALL STUDENTS ==========")

    if not students:
        print("No student records available.")
        return

    for student in students:
        display_student(student)


def search_student(students):
    """Search student by roll number."""
    print("\n========== SEARCH STUDENT ==========")

    roll_no = input("Enter roll number: ").strip()

    student = find_student(students, roll_no)

    if student:
        display_student(student)
    else:
        print("Student not found.")


def update_student(students):
    """Update student details."""
    print("\n========== UPDATE STUDENT ==========")

    roll_no = input("Enter roll number: ").strip()

    student = find_student(students, roll_no)

    if not student:
        print("Student not found.")
        return

    print("Leave name/branch blank to keep the existing value.")

    new_name = input(f"Name [{student['name']}]: ").strip()

    if new_name:
        student["name"] = new_name

    new_branch = input(f"Branch [{student['branch']}]: ").strip()

    if new_branch:
        student["branch"] = new_branch

    print("\nEnter updated marks:")

    for subject in SUBJECTS:
        student["marks"][subject] = get_valid_marks(subject)

    performance = get_performance(student["marks"])

    student["total"] = performance["total"]
    student["percentage"] = performance["percentage"]
    student["grade"] = performance["grade"]
    student["status"] = performance["status"]

    save_students(students)

    print("\nStudent updated successfully!")


def delete_student(students):
    """Delete a student record."""
    print("\n========== DELETE STUDENT ==========")

    roll_no = input("Enter roll number: ").strip()

    student = find_student(students, roll_no)

    if not student:
        print("Student not found.")
        return

    confirmation = input(
        f"Delete record of {student['name']}? (y/n): "
    ).lower()

    if confirmation == "y":
        students.remove(student)
        save_students(students)
        print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")
