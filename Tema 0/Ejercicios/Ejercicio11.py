# Función para comprobar si un carácter es una vocal
def isVowel(char):
    vowels = "aeiouAEIOU"
    return char in vowels

# Solicitar al usuario que introduzca un carácter
char = input("Introduce un carácter: ")

# Comprobar si el carácter es una vocal y mostrar el resultado
print("El carácter " + "es vocal" if isVowel(char) else "no es vocal")