import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src import app


def test_add():
    assert app.add(2, 3) == 5


def test_sub():
    assert app.sub(5, 3) == 2
