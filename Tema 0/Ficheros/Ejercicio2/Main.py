import os

def main():
    os.chdir("Tema 0/Ficheros/Ejercicio2")

    fichero = open("Cadenas.txt", "w")

    cadena = input("Introduce una cadena (escribe fin para terminar): ")

    while cadena != "fin":
        fichero.write(cadena + "\n")

        cadena = input("Introduce otra cadena: ")

    fichero.close()

if __name__ == "__main__":
    main()