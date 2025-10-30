from pathlib import Path
from app.calculator import Calculator, LoggingObserver, AutoSaveObserver

def test_history_save_and_load(tmp_path: Path):
    c = Calculator()
    c.register(LoggingObserver())
    c.register(AutoSaveObserver(c.history))

    # do a calc to add one history entry
    c.calculate('add', 2, 3, round)
    assert len(c.history.items) == 1

    # save to a temp CSV (covers History.save_csv and to_dataframe)
    csv_path = tmp_path / 'hist.csv'
    c.history.save_csv(str(csv_path))
    assert csv_path.exists()

    # clear and load back (covers History.load_csv)
    c.history.clear()
    assert len(c.history.items) == 0
    c.history.load_csv(str(csv_path))
    assert len(c.history.items) == 1
