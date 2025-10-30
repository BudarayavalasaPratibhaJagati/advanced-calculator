from pathlib import Path
from app.history import History

def test_history_load_nonexistent(tmp_path: Path):
    h = History()
    assert len(h.items) == 0
    missing = tmp_path / 'does_not_exist.csv'
    h.load_csv(str(missing))  # should just return without error
    assert len(h.items) == 0
