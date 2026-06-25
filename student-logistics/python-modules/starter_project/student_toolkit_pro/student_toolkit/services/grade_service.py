from student_toolkit.config import PASS_PERCENTAGE
from student_toolkit.utils.validators import validate_positive_number


def calculate_percentage(obtained_marks, total_marks):
    validate_positive_number(total_marks, "Total marks")
    percentage = (obtained_marks / total_marks) * 100
    return percentage


def assign_grade(percentage):
    if percentage >= 90:
        return "A plus"
    if percentage >= 75:
        return "A"
    if percentage >= 60:
        return "B"
    if percentage >= PASS_PERCENTAGE:
        return "C"
    return "Fail"
