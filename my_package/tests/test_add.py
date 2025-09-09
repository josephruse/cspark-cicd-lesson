from app_joeruse import app_joeruse

def test_add():
    assert app_joeruse.add(1,1) == 2
name: Install dependencies
  run: |
    python -m pip install --upgrade pip
    pip install pytest pytest-cov
    pytest --doctest-modules --junitxml=junit/test-results.xml --cov=com --cov-report=xml --cov-report=html