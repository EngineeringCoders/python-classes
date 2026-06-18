# Assignments

## Assignment 1: Create a greeting module

Create:

```text
student_toolkit/services/greeting_service.py
```

Code:

```python
def welcome_student(name):
    return f"Welcome {name}, happy learning!"
```

Use it from `cli.py`.

## Assignment 2: Create a fee module

Create:

```text
student_toolkit/services/fee_service.py
```

Code:

```python
def calculate_pending_fee(total_fee, paid_fee):
    return total_fee - paid_fee
```

Add it to the CLI menu.

## Assignment 3: Search student by name

Create:

```text
student_toolkit/services/search_service.py
```

Requirements:

- Accept a list of student dictionaries.
- Accept a search name.
- Return matching student if found.
- Return `None` if not found.

## Assignment 4: Backup student data

Create:

```text
student_toolkit/storage/backup_storage.py
```

Requirements:

- Copy `students.json` into a backup file.
- Include timestamp in the backup file name.
- Use `datetime` and `pathlib`.

## Assignment 5: Write tests

Write tests for:

- `fee_service.py`
- `search_service.py`
- `grade_service.py`
- `attendance_service.py`

Run:

```bash
pytest
```

## Submission checklist

- Project runs using `python main.py`.
- Project runs using `python -m student_toolkit`.
- At least three students can be added.
- CSV export works.
- Tests pass.
- No `__pycache__` or `.venv` committed.
