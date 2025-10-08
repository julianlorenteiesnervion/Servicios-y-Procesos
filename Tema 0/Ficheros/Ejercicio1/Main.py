import os

def main():
    os.chdir("Tema 0/Ficheros/Ejercicio1")

    fichero = open("Alumnos.txt", "rt")

    for linea in fichero:
        print(linea, end="")

    fichero.close()

if __name__ == "__main__":
    main()