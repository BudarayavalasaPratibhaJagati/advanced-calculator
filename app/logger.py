import logging, os
from .calculator_config import load_config
_config = load_config()
def get_logger(name='calculator'):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(os.path.join(_config.log_dir, _config.log_file), encoding=_config.default_encoding)
        fh.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))
        logger.addHandler(fh)
    return logger
