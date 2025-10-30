from app.calculator import Calculator, LoggingObserver, AutoSaveObserver
from app.input_validators import two_numbers

def test_calculate_and_history():
    c = Calculator()
    c.register(LoggingObserver())
    c.register(AutoSaveObserver(c.history))
    a,b = two_numbers('2','3')
    res = c.calculate('add', a,b, round)
    assert res.result == 5
    assert len(c.history.items) == 1
    c.undo(); assert len(c.history.items) == 0
    c.redo(); assert len(c.history.items) == 1
