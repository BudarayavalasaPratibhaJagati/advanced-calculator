import importlib, os
from app.calculator import Calculator

def test_history_trims_when_exceeds_max(monkeypatch):
    # set max history size to 2, then reload modules to pick up the env
    monkeypatch.setenv('CALCULATOR_MAX_HISTORY_SIZE', '2')
    import app.calculator_config as cfg; importlib.reload(cfg)
    import app.history as hist; importlib.reload(hist)
    import app.calculator as calcmod; importlib.reload(calcmod)

    c = calcmod.Calculator()
    # do 3 calculations -> first should be popped (exercises pop(0) line)
    c.calculate('add', 1, 1, round)
    c.calculate('add', 2, 2, round)
    c.calculate('add', 3, 3, round)
    # only the last 2 remain
    assert len(c.history.items) == 2
    assert c.history.items[0].a == 2 and c.history.items[1].a == 3
