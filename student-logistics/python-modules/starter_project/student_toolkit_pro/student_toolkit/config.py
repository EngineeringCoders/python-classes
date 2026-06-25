from pathlib import Path

BASE_DIR = Path.cwd()

DATA_DIR = BASE_DIR / "data"
EXPORT_DIR = BASE_DIR / "exports"
LOG_DIR = BASE_DIR / "logs"

STUDENT_DATA_FILE = DATA_DIR / "students.json"
STUDENT_REPORT_FILE = EXPORT_DIR / "students_report.csv"
APP_LOG_FILE = LOG_DIR / "app.log"

PASS_PERCENTAGE = 40
ATTENDANCE_ELIGIBILITY_PERCENTAGE = 75
