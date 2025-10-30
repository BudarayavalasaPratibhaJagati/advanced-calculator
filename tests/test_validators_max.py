import os, importlib, pytest
from app.exceptions import ValidationError

def test_to_number_exceeds_max(monkeypatch):
    # make the max really small, then reload validators to pick it up
    monkeypatch.setenv('CALCULATOR_MAX_INPUT_VALUE', '1')
    import app.input_validators as iv
    importlib.reload(iv)
    with pytest.raises(ValidationError):
        iv.to_number('5')  # exceeds the max of 1
