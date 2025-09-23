def printArray(array):
    message = "Los números ordenados son: "
    for i in array:
        message += str(i) + " "
    print(message)

number1 = int(input("Ingrese el primer numero: "))
number2 = int(input("Ingrese el segundo numero: "))

numbers = [number1, number2]

printArray(sorted(numbers))