# Class Flow

## Part 1: Why modules are needed

Start with the problem of one large file:

```text
main.py
├── marks logic
├── attendance logic
├── quiz logic
├── storage logic
└── report logic
```

Problems:

- Hard to read
- Hard to debug
- Hard to test
- Hard to reuse
- Hard to extend

Then introduce modular design:

```text
student_toolkit/
├── cli.py
├── config.py
├── services/
├── storage/
└── utils/
```

## Part 2: Module basics

Cover:

- What is a `.py` module?
- Standard library module
- User-defined module
- Third-party module
- Import styles

## Part 3: Import system

Cover:

- `sys.path`
- `sys.modules`
- `__pycache__`
- file name shadowing
- circular imports

## Part 4: Package design

Cover:

- `student_toolkit/`
- `__init__.py`
- `__main__.py`
- absolute imports
- relative imports

## Part 5: Build order

1. `config.py`
2. `validators.py`
3. `logger.py`
4. `grade_service.py`
5. `attendance_service.py`
6. `quiz_service.py`
7. `json_storage.py`
8. `report_service.py`
9. `csv_exporter.py`
10. `cli.py`
11. `main.py`
12. `__main__.py`

## Part 6: Testing

Cover why modules are easier to test and run `pytest` for grade, attendance, and quiz modules.

## Part 7: Extension tasks

Students add `fee_service.py`, `search_service.py`, `backup_storage.py`, and tests for new modules.
