import uuid
from typing import Union


def generate_unique_id(prefix: str = "") -> str:
    """
    Generate a unique ID with an optional prefix.
    Example: generate_unique_id("qr") -> "qr-550e8400-e29b-41d4-a716-446655440000"
    """
    return f"{prefix}-{uuid.uuid4()}" if prefix else str(uuid.uuid4())


def format_currency(amount: Union[int, float], currency_symbol: str = "$") -> str:
    """
    Format a number as currency
    Example: format_currency(150) -> "$150.00"
    """
    return f"{currency_symbol}{amount:,.2f}"


def validate_positive_number(value: Union[int, float], field_name: str = "") -> bool:
    """
    Validate that a number is positive
    """
    if value < 0:
        raise ValueError(f"{field_name or 'Value'} must be positive. Got: {value}")
    return True


def clamp_value(value: Union[int, float], min_value: Union[int, float], max_value: Union[int, float]) -> Union[int, float]:
    """
    Clamp a value between min_value and max_value
    """
    return max(min_value, min(value, max_value))


# Example usage:
# print(generate_unique_id("qr"))
# print(format_currency(199.99))
# validate_positive_number(150, "Base Rate")
# print(clamp_value(25, 10, 20))  # returns 20
