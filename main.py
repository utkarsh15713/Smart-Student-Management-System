from storage import load_students

from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

from analysis import (
    show_performance,
    class_statistics,
    top_performers,
    subject_analysis
)

from utils import (
    display_header,
    display_menu,
    pause,
    goodbye
)


def main():
    students = load_students()

    while True:
        display_header()
        display_menu()

        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            add_student(students)
            pause()

        elif choice == "2":
            view_students(students)
            pause()

        elif choice == "3":
            search_student(students)
            pause()

        elif choice == "4":
            update_student(students)
            pause()

        elif choice == "5":
            delete_student(students)
            pause()

        elif choice == "6":
            show_performance(students)
            pause()

        elif choice == "7":
            class_statistics(students)
            pause()

        elif choice == "8":
            top_performers(students)
            pause()

        elif choice == "9":
            subject_analysis(students)
            pause()

        elif choice == "10":
            goodbye()
            break

        else:
            print("\nInvalid choice! Please enter a number from 1 to 10.")
            pause()


if __name__ == "__main__":
    main()
