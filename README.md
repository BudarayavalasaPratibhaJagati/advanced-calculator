# Advanced CLI Calculator

Run:
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m app.calculator_repl
Tests:
pytest --cov=app --cov-fail-under=90
