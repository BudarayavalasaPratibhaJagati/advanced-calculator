import pytest
from app.input_validators import to_number, two_numbers
from app.exceptions import ValidationError

def test_to_number_ok():
    assert to_number('3.5') == 3.5

def test_to_number_fail():
    with pytest.raises(ValidationError):
        to_number('abc')

def test_two_numbers():
    a,b = two_numbers('2', '5')
    assert a == 2 and b == 5
