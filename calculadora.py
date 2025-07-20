# calculadora.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def potencia(a, b):
    return a ** b

if __name__ == "__main__":
    print("Suma:", sumar(10, 5))
    print("Resta:", restar(10, 5))
    print("Multiplicación:", multiplicar(10, 5))
    print("División:", dividir(10, 5))
    print("Potencia",potencia(2,7))