import random

guess = 0 # Preguntar a Elena si es buena práctica inicializar la variable a 0 para que el usuario no pueda ingresar texto después
secretNumber = random.randint(1, 100)

guess = int(input("Ingrese un número: "))

while guess != -1 and guess != secretNumber:
    if guess > secretNumber:
        print("El número es menor")
    elif guess < secretNumber:
        print("El número es mayor")

    guess = int(input("Ingrese otro número: "))

print("¡El número es correcto!")