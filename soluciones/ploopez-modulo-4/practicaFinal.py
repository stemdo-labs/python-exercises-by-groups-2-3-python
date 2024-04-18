import random

nombre= input("Introduce tu nombre: ")

numero_secreto = random.randint(1, 100)
print("¡Se ha generado un número secreto entre 1 y 100!")
print("Tienes 8 intentos para adivinarlo.")

intentos = 8
while intentos > 0:
    # Solicitar al usuario que ingrese un número
    intento = input("Intenta adivinar el número: ")

    # Validar si el número ingresado es un número válido
    if not intento.isdigit() or int(intento) < 1 or int(intento) > 100:
        print("Por favor, ingresa un número válido entre 1 y 100.")
        continue

    intento = int(intento)

    # Verificar si el intento del usuario es correcto
    if intento == numero_secreto:
        intentos_utilizados = 8 - intentos + 1
        print("¡Felicidades,", nombre + "! Has adivinado el número secreto en", intentos_utilizados, "intentos.")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor que", intento)
    else:
        print("El número secreto es menor que", intento)

    # Reducir el número de intentos restantes
    intentos -= 1

# Si el usuario no adivina el número en 8 intentos, mostrar el número secreto
if intentos == 0:
    print("¡Lo siento, has agotado tus 8 intentos! El número secreto era", numero_secreto)