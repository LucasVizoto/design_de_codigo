from pytest import raises

from .calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
    def __init__(self, body:dict) -> None:
        self.json = body

class MockDriverHandlerError:
    def variance(self, numbers:list[float])-> float:
        return 3

class MockDriverHandler:
    def variance(self, numbers:list[float])-> float:
        return 10000000

def test_calculate_integration():
    numpy_handler = NumpyHandler()
    mock_request = MockRequest({"numbers":[1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(numpy_handler)
    response = calculator_3.calculate(mock_request)

    assert response == {'data': {'Calculator': 3, 'value': 1568.16, 'Success': True}}


def test_calculator_with_variance_error():
    mock_request = MockRequest({
        "numbers":[1, 2, 3, 4, 5]
        })
    calculator_3 = Calculator3(NumpyHandler())
    with raises(Exception) as excepinfo:
        calculator_3.calculate(mock_request)
    
    assert str(excepinfo.value) == "Falha no Processo: Variancia menor que multiplicação"
