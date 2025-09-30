# Declaramos el texto
text = "Hola qué tal estás. Hola muy bien. Estás."

# Mostramos la frecuencia de cada palabra en el texto
# Dividimos el texto en palabras
words = text.split()

# Contar la frecuencia de cada palabra
word_count = {}

# Recorremos cada palabra en la lista
for word in words:
    # Limpiamos signos de puntuación y convertimos a minúsculas
    word = word.strip(".,").lower()

    # Actualizamos el conteo de la palabra
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Mostramos la frecuencia de cada palabra
print("Frecuencia de cada palabra:")
for word, count in word_count.items():
    print(f"{word}: {count}")
