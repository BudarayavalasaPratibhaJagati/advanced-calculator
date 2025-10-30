import pytest
from app.operations import create_operation
from app.exceptions import OperationError

def test_root_zero_degree_raises():
    with pytest.raises(OperationError):
        create_operation('root').compute(9, 0)
