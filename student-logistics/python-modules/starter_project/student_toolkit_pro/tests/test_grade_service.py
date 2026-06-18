from student_toolkit.services.grade_service import calculate_percentage, assign_grade


def test_calculate_percentage():
    assert calculate_percentage(80, 100) == 80


def test_assign_grade_top_grade():
    assert assign_grade(95) == "A plus"


def test_assign_grade_fail():
    assert assign_grade(30) == "Fail"
