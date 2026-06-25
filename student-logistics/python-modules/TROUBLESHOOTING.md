# Troubleshooting Guide

## Problem: `ModuleNotFoundError`

Example:

```text
ModuleNotFoundError: No module named 'student_toolkit'
```

Fix:

Run commands from the project root:

```bash
cd student-logistics/python-modules/starter_project/student_toolkit_pro
python main.py
```

## Problem: Virtual environment not activated

Activate on macOS or Linux:

```bash
source .venv/bin/activate
```

Activate on Windows:

```bash
.venv\Scripts\activate
```

## Problem: `pytest` not found

Fix:

```bash
pip install pytest
```

## Problem: File name shadowing

Avoid creating files with these names:

```text
random.py
json.py
csv.py
math.py
logging.py
statistics.py
pathlib.py
```

Rename the file and delete `__pycache__`.

## Problem: Circular import

Bad pattern:

```text
a.py imports b.py
b.py imports a.py
```

Fix:

Move shared logic to a third module such as `common.py`.

## Problem: Data file not created

The app creates `data/students.json` only after saving at least one student.

Run:

```bash
python main.py
```

Choose option `1. Add Student`.
