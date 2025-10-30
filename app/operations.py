from dataclasses import dataclass
from .exceptions import OperationError

@dataclass
class Operation:
    name: str
    def compute(self, a: float, b: float) -> float:  # pragma: no cover
        raise NotImplementedError

class Add(Operation):
    def __init__(self): 
        super().__init__('add')
    def compute(self, a, b):
        return a + b

class Subtract(Operation):
    def __init__(self): 
        super().__init__('subtract')
    def compute(self, a, b):
        return a - b

class Multiply(Operation):
    def __init__(self): 
        super().__init__('multiply')
    def compute(self, a, b):
        return a * b

class Divide(Operation):
    def __init__(self): 
        super().__init__('divide')
    def compute(self, a, b):
        if b == 0:
            raise OperationError('Division by zero')
        return a / b

class Power(Operation):
    def __init__(self): 
        super().__init__('power')
    def compute(self, a, b):
        return a ** b

class Root(Operation):
    def __init__(self): 
        super().__init__('root')
    def compute(self, a, b):
        if b == 0:
            raise OperationError('Zero root not defined')
        if a < 0 and int(b) % 2 == 0:
            raise OperationError('Even root of negative not real')
        return a ** (1.0 / b)

class Modulus(Operation):
    def __init__(self): 
        super().__init__('modulus')
    def compute(self, a, b):
        if b == 0:
            raise OperationError('Mod by zero')
        return a % b

class IntDivide(Operation):
    def __init__(self): 
        super().__init__('int_divide')
    def compute(self, a, b):
        if b == 0:
            raise OperationError('Int divide by zero')
        return int(a // b)

class Percent(Operation):
    def __init__(self): 
        super().__init__('percent')
    def compute(self, a, b):
        if b == 0:
            raise OperationError('Percent base zero')
        return (a / b) * 100.0

class AbsDiff(Operation):
    def __init__(self): 
        super().__init__('abs_diff')
    def compute(self, a, b):
        return abs(a - b)

_FACTORY = {  # pragma: no cover
    'add': Add, 'subtract': Subtract, 'multiply': Multiply, 'divide': Divide,
    'power': Power, 'root': Root, 'modulus': Modulus, 'int_divide': IntDivide,
    'percent': Percent, 'abs_diff': AbsDiff,
}

def create_operation(name: str) -> Operation:
    key = name.lower()
    if key not in _FACTORY:
        raise OperationError(f'Unknown operation: {name}')
    return _FACTORY[key]()
