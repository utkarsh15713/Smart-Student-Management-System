def calculate_total(marks):
    """Calculate total marks."""
    return sum(marks.values())


def calculate_percentage(marks):
    """Calculate percentage."""
    total = calculate_total(marks)
    return total / len(marks)


def calculate_grade(percentage):
    """Calculate grade based on percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def calculate_status(marks):
    """Determine pass/fail status."""
    for mark in marks.values():
        if mark < 40:
            return "FAIL"

    return "PASS"


def get_performance(marks):
    """Return complete academic performance."""
    total = calculate_total(marks)
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)
    status = calculate_status(marks)

    return {
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": status
    }
