# Importa la librería random para generar números aleatorios
import random

# Variable para guardar el número ingresado por el usuario
guess = 0 # Preguntar a Elena si es buena práctica inicializar la variable a 0 para que el usuario no pueda ingresar texto después

# Genera un número aleatorio entre 1 y 100
secretNumber = random.randint(1, 100)

# Pide al usuario que ingrese un número
guess = int(input("Ingrese un número: "))

# Mientras el número ingresado no sea -1 (para salir) y no sea igual al número secreto
while guess != -1 and guess != secretNumber:
    # Indica si el número es mayor o menor que el número secreto
    if guess > secretNumber:
        print("El número es menor")
    elif guess < secretNumber:
        print("El número es mayor")

    # Pide al usuario que ingrese otro número
    guess = int(input("Ingrese otro número: "))

# Si el usuario adivinó el número, felicítalo; si ingresó -1, indica que salió del juego
if guess == secretNumber:
    print("¡El número es correcto!")
else:
    print("Has salido del juego.")
