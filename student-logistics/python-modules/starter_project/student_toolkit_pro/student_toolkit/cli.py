from student_toolkit.services.grade_service import calculate_percentage, assign_grade
from student_toolkit.services.attendance_service import (
    calculate_attendance_percentage,
    check_exam_eligibility,
)
from student_toolkit.services.quiz_service import (
    pick_random_student,
    generate_module_question,
)
from student_toolkit.services.report_service import generate_summary, format_summary
from student_toolkit.storage.json_storage import load_students, save_students
from student_toolkit.storage.csv_exporter import export_students_to_csv
from student_toolkit.utils.validators import validate_non_empty_text
from student_toolkit.utils.logger import get_logger

logger = get_logger(__name__)


def add_student():
    try:
        name = input("Enter student name: ")
        validate_non_empty_text(name, "Student name")

        obtained_marks = float(input("Enter obtained marks: "))
        total_marks = float(input("Enter total marks: "))
        present_days = int(input("Enter present days: "))
        total_days = int(input("Enter total working days: "))

        percentage = calculate_percentage(obtained_marks, total_marks)
        grade = assign_grade(percentage)
        attendance_percentage = calculate_attendance_percentage(present_days, total_days)
        eligibility = check_exam_eligibility(attendance_percentage)

        student = {
            "name": name,
            "obtained_marks": obtained_marks,
            "total_marks": total_marks,
            "percentage": percentage,
            "grade": grade,
            "attendance_percentage": attendance_percentage,
            "eligibility": eligibility,
        }

        students = load_students()
        students.append(student)
        save_students(students)
        print("Student added successfully.")
        logger.info("Student added: %s", name)
    except ValueError as error:
        print("Input Error:", error)
        logger.error("Input error: %s", error)


def show_students():
    students = load_students()
    if not students:
        print("No students found.")
        return
    for index, student in enumerate(students, start=1):
        print(f"\nStudent {index}")
        print(f"Name                  : {student['name']}")
        print(f"Percentage            : {student['percentage']:.2f}")
        print(f"Grade                 : {student['grade']}")
        print(f"Attendance Percentage : {student['attendance_percentage']:.2f}")
        print(f"Eligibility           : {student['eligibility']}")


def pick_student():
    try:
        students = load_students()
        names = [student["name"] for student in students]
        selected = pick_random_student(names)
        print("Selected student:", selected)
    except ValueError as error:
        print("Error:", error)
        logger.error("Random student selection failed: %s", error)


def show_quiz_question():
    print("Question:", generate_module_question())


def show_report():
    students = load_students()
    summary = generate_summary(students)
    print(format_summary(summary))


def export_report():
    students = load_students()
    if not students:
        print("No students available to export.")
        return
    file_path = export_students_to_csv(students)
    print(f"Report exported to: {file_path}")


def show_menu():
    print("\nStudent Toolkit Pro")
    print("-------------------")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Pick Random Student")
    print("4. Generate Module Question")
    print("5. Show Class Report")
    print("6. Export CSV Report")
    print("7. Exit")


def run_app():
    logger.info("Application started.")
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            pick_student()
        elif choice == "4":
            show_quiz_question()
        elif choice == "5":
            show_report()
        elif choice == "6":
            export_report()
        elif choice == "7":
            logger.info("Application closed.")
            print("Thank you for using Student Toolkit Pro.")
            break
        else:
            print("Invalid choice. Please try again.")
