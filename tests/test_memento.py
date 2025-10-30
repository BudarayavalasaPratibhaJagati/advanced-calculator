from app.calculator_memento import CalculatorState, Memento, Caretaker
from app.calculation import Calculation

def _calc(op='add', a=1, b=2, res=3, ts='t'):
    return Calculation(op, a, b, res, ts)

def test_memento_undo_redo_roundtrip():
    initial = CalculatorState([_calc('add',1,2,3,'t1')])
    ct = Caretaker()

    # push snapshot, then change current state to 2 items
    ct.push(Memento(initial))
    current = CalculatorState(initial.history + [_calc('mul',2,3,6,'t2')])

    # undo -> back to 1 item
    state_after_undo = ct.undo(current)
    assert len(state_after_undo.history) == 1

    # redo -> forward to 2 items
    state_after_redo = ct.redo(state_after_undo)
    assert len(state_after_redo.history) == 2
