import numpy

class NumpyHandler:
    def __init__(self)->None:
        self.__np = numpy
    
    #estou criando uma classe handler para calcular o desvio padrão
    # e caso necessário vou instanciando essa classe  
    def standard_derivation(self, numbers: list[float]) -> float:
        return self.__np.std(numbers)
'''
Caso em meu projeto seja necessário que eu crie um outro método para
o uso de um parametro extremamente específico, fazer da seguinte forma

    def standard_derivation_with_another_param(self, numbers: list[float]) -> float:
        return self.__np.std(numbers, axis=[])
    
'''
    