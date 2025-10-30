from typing import Protocol, List, Callable
from .operations import create_operation
from .calculation import Calculation
from .history import History
from .calculator_memento import CalculatorState, Memento, Caretaker
from .logger import get_logger
from .calculator_config import load_config

_config = load_config()
log = get_logger('calculator')

class Observer(Protocol):
    def notify(self, calc: Calculation) -> None: ...

class LoggingObserver:
    def notify(self, calc: Calculation) -> None:
        log.info(f'{calc.operation} | a={calc.a} b={calc.b} result={calc.result}')

class AutoSaveObserver:
    def __init__(self, history: History): self.history = history
    def notify(self, calc: Calculation) -> None:
        if _config.auto_save: self.history.save_csv()

class Calculator:
    def __init__(self):
        self.history = History()
        self.observers: List[Observer] = []
        self._caretaker = Caretaker()
    def register(self, observer: Observer): self.observers.append(observer)
    def _snapshot(self):
        state = CalculatorState(self.history.items)
        self._caretaker.push(Memento(state))
    def calculate(self, op_name: str, a: float, b: float, rounder: Callable[[float], float]) -> Calculation:
        self._snapshot()
        op = create_operation(op_name)
        result = rounder(op.compute(a, b))
        calc = Calculation.from_now(op.name, a, b, result)
        self.history.add(calc)
        for ob in self.observers: ob.notify(calc)
        return calc
    def undo(self):
        state = self._caretaker.undo(CalculatorState(self.history.items))
        self.history._items = state.history
    def redo(self):
        state = self._caretaker.redo(CalculatorState(self.history.items))
        self.history._items = state.history
