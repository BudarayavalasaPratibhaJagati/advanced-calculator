from .exceptions import ValidationError
from .calculator_config import load_config
_config = load_config()

def to_number(x):
    try:
        v = float(x)
    except Exception:
        raise ValidationError(f'Input ""{x}"" is not a number')
    if abs(v) > _config.max_input_value:
        raise ValidationError(f'Input {v} exceeds max allowed value')
    return v

def two_numbers(a, b):
    return to_number(a), to_number(b)
