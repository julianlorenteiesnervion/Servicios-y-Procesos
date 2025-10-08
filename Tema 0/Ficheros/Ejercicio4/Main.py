import os

def main():
    os.chdir("Tema 0/Ficheros/Ejercicio4")

    fichero = open("numeros.txt", "rt")

    numeros = []

    for linea in fichero:
        numeros.append(linea)

    print(numeros)

if __name__ == "__main__":
    main()