import pytest
from funciones import sum_digit
from funciones import validation
from funciones import count_digits
from funciones import potency
#Testeo de la funcion que suma los digitos de un numero ingresado
@pytest.mark.parametrize("number,result", [
    (32, 5),
    (-5-5, -10),
    (352, 10),
    (59438, 29),
])
def test_sum_digit(number, result):
    assert sum_digit(number) == result

#Testeo de la funcion validation que analiza si un dni es valido o no
@pytest.mark.parametrize("number1, expected",[
        (37625208,True),
        (987064, False),
        (321456789, False)
])
def test_validation(number1, expected):
    assert validation(number1) == expected

#Testeo de la funcion que cuenta los digitos de un numero de forma recursiva
@pytest.mark.parametrize("number, result",[
    (353,3),
    (20,2),
    (5,1)
])
def test_count_digits(number, result):
    assert count_digits(number) == result

#Testeo de la funcion para saber si n es potencia de b de manera recursiva
@pytest.mark.parametrize("n,b,result",[
    (8,2,True),
    (1,2,False)
])
def test_potency(n,b,result):
    assert potency(n,b) == result