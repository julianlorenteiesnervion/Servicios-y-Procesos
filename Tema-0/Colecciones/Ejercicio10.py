# Codifica una frase según un diccionario
def encode(text, dictionary):
    encoded_text = ""
    for char in text:
        if char in dictionary:
            encoded_text += dictionary[char]
        else:
            encoded_text += char
    return encoded_text

# Diccionario
dictionary = {
    "e": "p",
    "i": "v",
    "k": "i",
    "m": "u",
    "p": "m",
    "q": "t",
    "r": "e",
    "s": "r",
    "t": "k",
    "u": "q",
    "v": "s"
}

# Solicitar frase al usuario
phrase = input("Introduce una frase: ")

# Codificar la frase
encoded_phrase = encode(phrase, dictionary)

# Mostrar la frase codificada
print("Frase codificada:", encoded_phrase)