# Declaramos un diccionario vacío para almacenar las letras y sus conteos
letters = {}

# Solicitamos al usuario que introduzca una palabra
word = input("Introduce una palabra: ")

# Recorremos cada letra en la palabra y contamos sus apariciones
for i in range(len(word)):
    letters[word[i]] = word.count(word[i])

# Mostramos el resultado
for letter, count in letters.items():
    print(f"La letra '{letter}' aparece {count} veces.")
