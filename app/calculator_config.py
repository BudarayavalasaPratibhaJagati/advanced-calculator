from dataclasses import dataclass
from dotenv import load_dotenv
import os
from .exceptions import ConfigError

load_dotenv()

@dataclass(frozen=True)
class CalculatorConfig:
    log_dir: str
    history_dir: str
    log_file: str
    history_file: str
    max_history_size: int
    auto_save: bool
    precision: int
    max_input_value: float
    default_encoding: str

def _getenv(name, default=None):
    val = os.getenv(name, default)
    if val is None:
        raise ConfigError(f'Missing env: {name}')
    return val

def load_config() -> CalculatorConfig:
    log_dir = _getenv('CALCULATOR_LOG_DIR', 'logs')
    history_dir = _getenv('CALCULATOR_HISTORY_DIR', 'data')
    log_file = _getenv('CALCULATOR_LOG_FILE', 'calculator.log')
    history_file = _getenv('CALCULATOR_HISTORY_FILE', 'history.csv')
    max_history_size = int(_getenv('CALCULATOR_MAX_HISTORY_SIZE', '1000'))
    auto_save = _getenv('CALCULATOR_AUTO_SAVE', 'true').lower() == 'true'
    precision = int(_getenv('CALCULATOR_PRECISION', '4'))
    max_input_value = float(_getenv('CALCULATOR_MAX_INPUT_VALUE', '1e12'))
    encoding = _getenv('CALCULATOR_DEFAULT_ENCODING', 'utf-8')

    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(history_dir, exist_ok=True)

    return CalculatorConfig(
        log_dir, history_dir, log_file, history_file,
        max_history_size, auto_save, precision, max_input_value, encoding
    )
