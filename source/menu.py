from calculator import Calculator


def menu():
    print("Operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Factorial")
    print("0. Salir")

def ejecutar_calculadora():
    calc = Calculator()

    while True:
        menu()
        opcion = input("Ingrese su opción: ")

        if opcion == '0':
            print("Hasta pronto...")
            break

        a = float(input("Ingrese el primer número: "))

        if opcion in ['1', '2', '3', '4', '5']:
            b = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print("Resultado:", calc.suma(a, b))
        elif opcion == '2':
            print("Resultado:", calc.resta(a, b))
        elif opcion == '3':
            print("Resultado:", calc.multiplicacion(a, b))
        elif opcion == '4':
            print("Resultado:", calc.division(a, b))
        elif opcion == '5':
            print("Resultado:", calc.potencia(a, b))
        elif opcion == '6':
            a = int(input("Ingrese el número: "))
            print("Resultado:", calc.factorial(a))
        else:
            print("Opción no válida")

if __name__ == '__main__':
    ejecutar_calculadora()
