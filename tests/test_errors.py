import pytest
from app.operations import create_operation
from app.exceptions import OperationError

@pytest.mark.parametrize('name,a,b,msg', [
    ('divide', 1, 0, 'Division by zero'),
    ('modulus', 5, 0, 'Mod by zero'),
    ('int_divide', 5, 0, 'Int divide by zero'),
    ('percent', 10, 0, 'Percent base zero'),
])
def test_operation_zero_errors(name, a, b, msg):
    with pytest.raises(OperationError) as e:
        create_operation(name).compute(a,b)
    assert msg in str(e.value)

def test_even_root_negative_error():
    with pytest.raises(OperationError):
        create_operation('root').compute(-8, 2)

def test_unknown_operation_error():
    with pytest.raises(OperationError):
        create_operation('no_such_op')
