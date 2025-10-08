import os

def main():
    os.chdir("Tema 0/Ficheros/Ejercicio3")

    fichero = open("datos.txt", "a")

    datos = (input("Introduce el nombre: "), input("Introduce la edad: "))

    fichero.write(datos[0] + " " + datos[1] + "\n")

if __name__ == "__main__":
    main()