class Calculator():
    def __init__(self):
        #inicializamos la calculadora
        self.value=0
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero ")
        return a / b

    def potencia(self, a, b):
        return a ** b

    #Añadimos  función factorial
    def factorial(self, n):
        if n < 0:
            raise ValueError("Introduzca un num positivo ")
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado