import pytest
from app.operations import create_operation
from app.exceptions import OperationError

@pytest.mark.parametrize('name,a,b,expected', [
    ('add', 2, 3, 5),
    ('subtract', 5, 2, 3),
    ('multiply', 3, 4, 12),
    ('divide', 8, 2, 4),
    ('power', 2, 3, 8),
    ('root', 9, 2, 3),
    ('modulus', 8, 3, 2),
    ('int_divide', 7, 2, 3),
    ('percent', 50, 200, 25),
    ('abs_diff', 5, 9, 4),
])
def test_ops(name, a, b, expected):
    op = create_operation(name)
    assert op.compute(a,b) == pytest.approx(expected)

def test_divide_by_zero():
    with pytest.raises(OperationError):
        create_operation('divide').compute(1,0)

def test_unknown():
    with pytest.raises(OperationError):
        create_operation('nope')
