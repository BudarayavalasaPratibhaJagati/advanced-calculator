from dataclasses import dataclass
from typing import List
from .calculation import Calculation

@dataclass
class CalculatorState:
    history: List[Calculation]

class Memento:
    def __init__(self, state: CalculatorState):
        self._state = CalculatorState(list(state.history))
    def get_state(self) -> CalculatorState:
        return CalculatorState(list(self._state.history))

class Caretaker:
    def __init__(self):
        self._undo_stack: List[Memento] = []
        self._redo_stack: List[Memento] = []
    def push(self, mem: Memento):
        self._undo_stack.append(mem); self._redo_stack.clear()
    def undo(self, current_state: CalculatorState) -> CalculatorState:
        if not self._undo_stack: return current_state
        m = self._undo_stack.pop()
        self._redo_stack.append(Memento(current_state))
        return m.get_state()
    def redo(self, current_state: CalculatorState) -> CalculatorState:
        if not self._redo_stack: return current_state
        m = self._redo_stack.pop()
        self._undo_stack.append(Memento(current_state))
        return m.get_state()
