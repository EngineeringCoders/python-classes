from student_toolkit.config import ATTENDANCE_ELIGIBILITY_PERCENTAGE
from student_toolkit.utils.validators import validate_positive_number


def calculate_attendance_percentage(present_days, total_days):
    validate_positive_number(total_days, "Total working days")
    return (present_days / total_days) * 100


def check_exam_eligibility(attendance_percentage):
    if attendance_percentage >= ATTENDANCE_ELIGIBILITY_PERCENTAGE:
        return "Eligible"
    return "Not Eligible"
