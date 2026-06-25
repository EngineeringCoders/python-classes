import random

MODULE_QUESTIONS = [
    "What is a Python module?",
    "What is the difference between a module and package?",
    "What is __init__.py?",
    "What is sys.path?",
    "What is __pycache__?",
    "What is the use of if __name__ == '__main__'?",
]


def pick_random_student(student_names):
    if not student_names:
        raise ValueError("Student list cannot be empty.")
    return random.choice(student_names)


def generate_module_question():
    return random.choice(MODULE_QUESTIONS)
