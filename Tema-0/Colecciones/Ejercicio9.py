# Declaramos un diccionario vacío para almacenar las letras y sus conteos
letters = {}

# Solicitamos al usuario que introduzca una palabra
word = input("Introduce una palabra: ")

# Recorrer la palabra letra a letra
# Comprobar si la letra ya está en el diccionario
# Si está, incrementar su conteo
# Si no está, añadirla al diccionario con un conteo de 1
for letter in word:
    if letter in letters:
        letters[letter] += 1
    else:
        letters[letter] = 1

# Mostramos el resultado
for letter, count in letters.items():
    print(f"La letra '{letter}' aparece {count} veces.")
