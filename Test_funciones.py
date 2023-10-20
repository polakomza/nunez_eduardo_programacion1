import pytest
from funciones import sum_digit

@pytest.mark.parametrize("number,result", [
    (32, 5),
    (-5-5, -10),
    (352, 10),
    (59438, 29),
])

def test_sum_digit(number, result):
    assert sum_digit(number) == result