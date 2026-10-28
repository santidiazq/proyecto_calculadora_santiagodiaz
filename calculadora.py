# calculadora.py

def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    if num2 == 0:
        raise ValueError("No es posible dividir entre cero.")
    return num1 / num2


def potencia(num1, num2):
    return num1 ** num2


def main():
    while True:
        print("\n=== CALCULADORA EN PYTHON ===")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "0":
            print("Programa finalizado.")
            break

        if opcion not in ["1", "2", "3", "4", "5"]:
            print("Opción no válida.")
            continue

        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if opcion == "1":
                resultado = suma(num1, num2)
                operacion = "Suma"
            elif opcion == "2":
                resultado = resta(num1, num2)
                operacion = "Resta"
            elif opcion == "3":
                resultado = multiplicar(num1, num2)
                operacion = "Multiplicación"
            elif opcion == "4":
                resultado = dividir(num1, num2)
                operacion = "División"
            else:
                resultado = potencia(num1, num2)
                operacion = "Potencia"

            print("\n------------------------------")
            print("Operación:", operacion)
            print("Resultado:", resultado)
            print("------------------------------")

        except ValueError as error:
            print("Error:", error)

        except OverflowError:
            print("Error: el resultado es demasiado grande.")


if __name__ == "__main__":
    main()