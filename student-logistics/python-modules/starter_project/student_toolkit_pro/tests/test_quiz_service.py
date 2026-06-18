from student_toolkit.services.quiz_service import pick_random_student


def test_pick_random_student():
    students = ["Asha", "Ravi", "Kiran"]
    selected = pick_random_student(students)
    assert selected in students
