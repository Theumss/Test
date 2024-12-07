# test_example.py

def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5  # Test que l'addition de 2 et 3 donne bien 5
    assert add(-1, 1) == 0  # Test que l'addition de -1 et 1 donne bien 0
    assert add(0, 0) == 0   # Test que l'addition de 0 et 0 donne bien 0
