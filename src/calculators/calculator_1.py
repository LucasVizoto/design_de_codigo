from flask import request as FlaskRequest

class Calculator1:
    def calculate(self, request:FlaskRequest)-> dict:
        
        
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data/3

        first_process_result = self.__first_procedd(splited_number)

        

    def __validate_body(self, body: dict) -> float:
        if "number" not in body:
            raise Exception("Bad Request")
        
        input_data = body["number"]
        return input_data
    
    def __first_procedd(self, first_part: float) -> float:
        first_part = (first_part/4)+7
        second_part = (first_part**2)*0.257
        return second_part