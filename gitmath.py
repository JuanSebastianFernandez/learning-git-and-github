import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a*b

def exponente(a, b):
    return a**b

def division(a, b):
    if b == 0:
        return "Error: Please write a different number to 0 -- Division By zero is not possible"
    return a/b

def raiz_2(a):
    return math.sqrt(a)

def logaritmo_n(a):
    return math.log(a)