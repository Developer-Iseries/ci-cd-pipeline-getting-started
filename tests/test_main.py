from src.main import add


def test_add_function():
    assert add(3, 5) == 8
    assert add(3, 3) == 6
    assert add(3, 2) == 5
    assert add(3, 1) == 4
    assert add(3, 7) == 10
    assert add(2, 2) == 4