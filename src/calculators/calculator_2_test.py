from .calculator_2 import Calculator2
from pytest import raises

from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: list[float]) -> float:
        return 3
    # a lógica desse mock é criar um elemento fictício e controlado
    # para testar não a integração entre a Calc2 e o Numpy, mas sim a 
    # lógica implementada por trás da calc2, por isso o retono é simplemente 3   

# Esse etste na verdade está testando a integração ente a
# Calculator2 e o NumpyHandler 
def test_calculate_integration():
    mock = MockRequest({ 
        "numbers":[2.12, 4.65,8.65]
        })
    
    driver = NumpyHandler()
    calculator2 = Calculator2(driver)
    formated_response = calculator2.calculate(mock)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result':(0.04)}}


def test_calculate():
    mock = MockRequest({ 
        "numbers":[2.12, 4.65,8.65]
        })
    
    driver = MockDriverHandler()
    calculator2 = Calculator2(driver)
    formated_response = calculator2.calculate(mock)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result':(0.33)}}


def test_calculate_with_errors():
    mock_error = MockRequest({ 
    "num":[2.12, 4.65,8.65]
    })
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)

    with raises(Exception) as excinfo:
        calculator_2.calculate(mock_error)
   
    assert str(excinfo.value) == "Bad Request"