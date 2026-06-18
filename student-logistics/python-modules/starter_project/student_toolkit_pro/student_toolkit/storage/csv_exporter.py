from student_toolkit.config import STUDENT_REPORT_FILE
from student_toolkit.utils.logger import get_logger

logger = get_logger(__name__)


def export_students_to_csv(students):
    logger.info("CSV export requested for %s students", len(students))
    return STUDENT_REPORT_FILE
