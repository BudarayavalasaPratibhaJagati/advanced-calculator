from typing import List
import os
import pandas as pd
from .calculation import Calculation
from .calculator_config import load_config

_config = load_config()

class History:
    def __init__(self):
        self._items: List[Calculation] = []

    @property
    def items(self) -> List[Calculation]:
        return list(self._items)

    def add(self, calc: Calculation):
        self._items.append(calc)
        if len(self._items) > _config.max_history_size:
            self._items.pop(0)

    def clear(self):
        self._items.clear()

    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame([c.__dict__ for c in self._items])

    def save_csv(self, path: str = None):
        if path is None:
            path = os.path.join(_config.history_dir, _config.history_file)
        df = self.to_dataframe()
        df.to_csv(path, index=False, encoding=_config.default_encoding)

    def load_csv(self, path: str = None):
        if path is None:
            path = os.path.join(_config.history_dir, _config.history_file)
        if not os.path.exists(path):  # pragma: no cover
            return
        df = pd.read_csv(path, encoding=_config.default_encoding)
        self._items = [
            Calculation(row['operation'], float(row['a']), float(row['b']),
                        float(row['result']), str(row['timestamp']))
            for _, row in df.iterrows()
        ]
