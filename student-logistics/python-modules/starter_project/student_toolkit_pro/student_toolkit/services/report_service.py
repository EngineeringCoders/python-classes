from statistics import mean


def generate_summary(students):
    if not students:
        return {
            "total_students": 0,
            "average_percentage": 0,
            "highest_percentage": 0,
            "lowest_percentage": 0,
        }

    percentages = [student["percentage"] for student in students]

    return {
        "total_students": len(students),
        "average_percentage": mean(percentages),
        "highest_percentage": max(percentages),
        "lowest_percentage": min(percentages),
    }


def format_summary(summary):
    return f"""
Class Report
------------
Total Students      : {summary["total_students"]}
Average Percentage  : {summary["average_percentage"]:.2f}
Highest Percentage  : {summary["highest_percentage"]:.2f}
Lowest Percentage   : {summary["lowest_percentage"]:.2f}
"""
