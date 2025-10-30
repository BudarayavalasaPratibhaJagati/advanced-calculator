import pytest
from app.calculator_config import _getenv
from app.exceptions import ConfigError

def test_getenv_missing_raises():
    with pytest.raises(ConfigError):
        _getenv('THIS_ENV_VAR_SHOULD_NOT_EXIST_AND_HAS_NO_DEFAULT')
