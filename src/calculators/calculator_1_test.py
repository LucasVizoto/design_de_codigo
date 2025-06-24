from .calculator_1 import Calculator1
from pytest import raises

class MockRequest:
    def __init__(self, body: dict) -> None:
        self.json = body
#fazendo um mock dos dados fingindo ser a request enviada

def test_calculate():
    mock_request = MockRequest(body={"number": 1})

    calculator_1 = Calculator1()

    response = calculator_1.calculate(mock_request)

    # formato da resposta
    assert "data" in response
    assert "Calculator" in response['data']
    assert "result" in response['data']

    # assertividade da resposta (caso retorne um ponto diferente vai apontar erro)
    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1


def test_calculate_with_body_error():
    mock_response = MockRequest(body={"something": 1})
    calculator_1 = Calculator1()

    with raises(Exception) as excinfo: # caso seja levantada essa exceção
        calculator_1.calculate(mock_response)
    
    assert str(excinfo.value) == "Bad Request"