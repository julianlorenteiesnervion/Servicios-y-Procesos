number = 0
sum = 0

while number >= 0:
    sum += number
    number = int(input("Ingrese un numero: "))

print("La suma de los números positivos es: " + str(sum))