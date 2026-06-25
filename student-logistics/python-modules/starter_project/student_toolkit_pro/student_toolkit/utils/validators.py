def validate_positive_number(value, field_name):
    if value <= 0:
        raise ValueError(f"{field_name} must be greater than zero.")


def validate_non_empty_text(value, field_name):
    if not value.strip():
        raise ValueError(f"{field_name} cannot be empty.")
