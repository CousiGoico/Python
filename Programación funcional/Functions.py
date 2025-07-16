def sumar(a, b, c, d):
    return a + b + c + d

def restar(a, b):
    return a - b    

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

