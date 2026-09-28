def class_average(students):
    if not students:
        return 0

    total_percentage = sum(
        student["percentage"] for student in students
    )

    return total_percentage / len(students)


def highest_scorer(students):
    if not students:
        return None

    return max(
        students,
        key=lambda student: student["percentage"]
    )


def lowest_scorer(students):
    if not students:
        return None

    return min(
        students,
        key=lambda student: student["percentage"]
    )


def pass_fail_count(students):
    passed = 0
    failed = 0

    for student in students:
        if student["status"] == "PASS":
            passed += 1
        else:
            failed += 1

    return passed, failed


def class_statistics(students):
    if not students:
        print("\nNo student records found.")
        return

    average = class_average(students)
    highest = highest_scorer(students)
    lowest = lowest_scorer(students)
    passed, failed = pass_fail_count(students)

    print("\n===== CLASS STATISTICS =====")

    print(f"\nTotal Students : {len(students)}")
    print(f"Class Average  : {average:.2f}%")

    print("\nHighest Scorer:")
    print(
        f"{highest['name']} "
        f"({highest['roll_no']}) - "
        f"{highest['percentage']:.2f}%"
    )

    print("\nLowest Scorer:")
    print(
        f"{lowest['name']} "
        f"({lowest['roll_no']}) - "
        f"{lowest['percentage']:.2f}%"
    )

    print("\nPass/Fail Report:")
    print(f"Passed : {passed}")
    print(f"Failed : {failed}")


def student_performance(students):
    if not students:
        print("\nNo student records found.")
        return

    roll_no = input("\nEnter Roll Number: ")

    found_student = None

    for student in students:
        if student["roll_no"] == roll_no:
            found_student = student
            break

    if found_student is None:
        print("\nStudent not found.")
        return

    student = found_student

    print("\n===== STUDENT PERFORMANCE =====")

    print(f"\nRoll Number : {student['roll_no']}")
    print(f"Name        : {student['name']}")
    print(f"Branch      : {student['branch']}")

    print("\nSubject Marks:")

    for subject, mark in student["marks"].items():
        print(f"{subject:<12}: {mark}")

    print("\nAcademic Result:")

    print(f"Total       : {student['total']}")
    print(f"Percentage  : {student['percentage']:.2f}%")
    print(f"Grade       : {student['grade']}")
    print(f"Status      : {student['status']}")

    print(
        f"Performance Level : "
        f"{performance_level(student)}"
    )


def show_performance(students):
    student_performance(students)


def top_performers(students):
    if not students:
        print("\nNo student records found.")
        return

    top_students = sorted(
        students,
        key=lambda student: student["percentage"],
        reverse=True
    )[:3]

    print("\n===== TOP 3 PERFORMERS =====")

    for i, student in enumerate(top_students, start=1):
        print(
            f"{i}. {student['name']} "
            f"({student['roll_no']}) - "
            f"{student['percentage']:.2f}%"
        )


def subject_analysis(students):
    if not students:
        print("\nNo student records found.")
        return

    subjects = list(students[0]["marks"].keys())

    print("\n===== SUBJECT-WISE ANALYSIS =====")

    averages = {}

    for subject in subjects:
        total = sum(
            student["marks"][subject]
            for student in students
        )

        average = total / len(students)

        averages[subject] = average

        print(f"{subject:<12}: {average:.2f}%")

    strongest = max(averages, key=averages.get)
    weakest = min(averages, key=averages.get)

    print("\nStrongest Subject:")
    print(f"Highest Average : {strongest}")

    print("\nWeakest Subject:")
    print(f"Lowest Average  : {weakest}")


def performance_level(student):
    percentage = student["percentage"]

    if percentage >= 90:
        return "Outstanding"

    elif percentage >= 75:
        return "Excellent"

    elif percentage >= 60:
        return "Good"

    elif percentage >= 50:
        return "Average"

    else:
        return "Needs Improvement"
