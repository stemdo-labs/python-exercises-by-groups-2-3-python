# Pedir al usuario que ingrese dos palabras
palabra1 = input("Por favor, ingresa una palabra: ")
palabra2 = input("Ahora, ingresa otra palabra: ")

# Combinar las palabras para formar el nombre de la cerveza
nombre_cerveza = palabra1 + " " + palabra2

# Mostrar el nombre de la cerveza entre comillas en dos líneas
print("\nEl nombre de tu cerveza creativa es:")
print('"' + nombre_cerveza + '"')