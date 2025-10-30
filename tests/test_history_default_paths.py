import importlib, os
from pathlib import Path

def test_history_default_paths(monkeypatch, tmp_path: Path):
    # Point history dir/file to a temp location
    monkeypatch.setenv('CALCULATOR_HISTORY_DIR', str(tmp_path))
    monkeypatch.setenv('CALCULATOR_HISTORY_FILE', 'hist.csv')

    # Reload config & history so they pick up new env
    import app.calculator_config as cfg
    importlib.reload(cfg)
    import app.history as hist
    importlib.reload(hist)

    h = hist.History()
    # Add a fake item by writing directly
    from app.calculation import Calculation
    h._items = [Calculation('add', 2, 3, 5, 't')]

    # save with no path -> uses defaults
    h.save_csv()
    assert (tmp_path / 'hist.csv').exists()

    # clear and load with no path -> uses defaults
    h.clear()
    h.load_csv()
    assert len(h.items) == 1
