from student_toolkit.services.attendance_service import (
    calculate_attendance_percentage,
    check_exam_eligibility,
)


def test_attendance_percentage():
    assert calculate_attendance_percentage(75, 100) == 75


def test_exam_eligibility():
    assert check_exam_eligibility(80) == "Eligible"
