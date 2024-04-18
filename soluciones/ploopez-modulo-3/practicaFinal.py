texto = input("Por favor, ingresa un texto: ")
letras = input("Por favor, ingresa tres letras separadas por espacios: ").split()

texto = texto.lower()
letras = [letra.lower() for letra in letras]

###################
conteo_letras = {letra: texto.count(letra) for letra in letras}

###################
cantidad_palabras = len(texto.split())

###################
primera_letra = texto[0]
ultima_letra = texto[-1]

###################
palabras_invertidas = ' '.join(texto.split()[::-1])

###################
esta_python = "python" in texto

#Resultados
print("Análisis del texto:")
print("Conteo de letras en el texto:", conteo_letras)
print("Cantidad total de palabras en el texto:", cantidad_palabras)
print("Primera letra del texto:", primera_letra)
print("Última letra del texto:", ultima_letra)
print("Texto con las palabras invertidas:", palabras_invertidas)
print("¿La palabra 'Python' está presente en el texto?", esta_python)
