from dataclasses import dataclass
from datetime import datetime

@dataclass
class Calculation:
    operation: str
    a: float
    b: float
    result: float
    timestamp: str

    @staticmethod
    def from_now(operation, a, b, result) -> 'Calculation':
        return Calculation(operation, a, b, result, datetime.utcnow().isoformat())
