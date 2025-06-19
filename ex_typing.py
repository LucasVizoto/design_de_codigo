# essa tipagem nn necessáriamente faz com que seja obrigatpriamente esse tipo
# ele apenas indica o funcionamento correto da função 

def add(elem1: int, elem2: float) -> dict:
    response = elem1+ elem2
    return { "sum" : response}


val1 = add(1,3)
val2 = add(2.34, 12.35)
val3 = add('hello', 'world')

print(val1)
print(val2)
print(val3)

# int, float, str, bool = True
# Dict, List, tuple 