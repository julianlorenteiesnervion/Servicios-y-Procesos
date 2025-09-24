# Función calculadora que realiza operaciones básicas
def calculadora(number1: int, number2: int, operation: int):
    result = 0

    # Realizar la operación según la elección del usuario
    # 1: Suma, 2: Resta, 3: Multiplicación, 4: División
    if operation == 1:
        result = number1 + number2
    elif operation == 2:
        result = number1 - number2
    elif operation == 3:
        result = number1 * number2
    elif operation == 4:
        result = number1 / number2
    else:
        print("Operación no válida")

    return result

# Solicitar al usuario los números
print("Calculadora")
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

# Mostrar el menú de operaciones
print("Elige la operación a realizar:")
print("1. Suma\n2. Resta\n3. Multiplicación\n4. División")

# Solicitar al usuario la operación
op = int(input("Operación (1/2/3/4): "))

# Calcular y mostrar el resultado
resultado = calculadora(num1, num2, op)
print(f"El resultado es: {resultado}")