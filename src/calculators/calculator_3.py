from flask import request as FlaskRequest

from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handle = driver_handler

    def calculate(self, request: FlaskRequest) -> dict: #type:ignore
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_result(variance, multiplication)

        formated_response = self.__format_response(variance)
        return formated_response

    def __validate_body(self, body: dict) -> list[float]:
        if "numbers" not in body:
            raise Exception("Bad Request")
        input_data = body["numbers"]
        return input_data
    
    def __calculate_variance(self, numbers: list[float]) -> float:
        variance = self.__driver_handle.variance(numbers)
        return variance
    
    def __calculate_multiplication(self, numbers: list[float]) -> float:
        multiplication = 1
        for num in numbers: multiplication *= num
        
        return multiplication
    
    def __verify_result(self, variance: float, multiplication:float)->None:
        if variance < multiplication:
            raise Exception('Falha no Processo: Variancia menor que multiplicação')

    def __format_response(self, variance: float) -> dict:
        return {
            "data" : {
                "Calculator": 3,
                "value" : variance,
                "Success": True
            }
        }