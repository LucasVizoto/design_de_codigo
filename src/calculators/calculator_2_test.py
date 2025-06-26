from .calculator_2 import Calculator2
from pytest import raises

class MockRequest:
    def __init__(self, body: dict) -> None:
        self.json = body

def test_calculate():
    mock = MockRequest({ 
        "numbers":[2.12, 4.65,8.65]
        })
    
    calculator2 = Calculator2()
    formated_response = calculator2.calculate(mock)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result':(0.04)}}


def test_calculate_with_errors():
    mock_error = MockRequest({ 
    "num":[2.12, 4.65,8.65]
    })
    calculator_2 = Calculator2()

    with raises(Exception) as excinfo:
        calculator_2.calculate(mock_error)
   
    assert str(excinfo.value) == "Bad Request"