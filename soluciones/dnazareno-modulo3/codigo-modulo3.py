#@dnazareno
#booleanos1
prueba = 10 > 5

#booleanos2
print(17834/34 > 87*56)

#booleanos3
import math
print(math.sqrt(25) == 5)

#diccionario1
diccionario = {'nombre':'Karen','apellido':'Jurgens','edad':35,'ocupacion':'Periodista'}
print(diccionario)

#diccionario2
#no esta el diccionario en el ejercicio asi que invento uno
points2 = {'c1':100,'c2':300,'c3':500}
print(points2['c2'])

#diccionario3
diccionario['edad'] = 36
diccionario['ocupacion'] = "Editora"
diccionario['pais'] = "Colombia"
print(diccionario)

#lista1
mi_lista = ["hola",10,True,3.1415]
print(mi_lista)

#lista2
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
print(medios_transporte)

#lista3
frutas = ["manzana","banana","mango","cereza","sandia"]
print(frutas)
frutas.pop(2)
print(frutas)

#metodoindex1
#A diferencia de lo que dice en Udemy en la teoria, el metodo index pide que el primer parametro sea siempre un string, por lo que resuelvo el ejercicio de otra forma
palabra = "ordeNador"
print(palabra[4])

#metodoindex2
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase.index("práctica")

#metodoindex3
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase.rindex("práctica")

#metodostring1
print("Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar.".upper())

#metodostring2
lista_palabras = ["La","legibilidad","cuenta."]
print(" ".join(lista_palabras))

#metodostring3
frase2 = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase2)
frase2 = frase2.replace("difícil","fácil")
frase2 = frase2.replace("mala","buena")
print(frase2)

#propiedadesstring1
print("Repetición"*15)

#propiedadesstring2
haiku = """Tierra mojada,

mis recuerdos de viaje

entre las lluvias"""

print("agua" in haiku)

#propiedadesstring3
print(len("electroencefalografista"))

#tuples1
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

#tuples2
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
type(mi_tupla)
mi_lista = list(mi_tupla)
type(mi_lista)

#tuples3
mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla
print(a,b,c,d)

#set1
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)
print(mi_set_3)

#set2
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()
print(sorteo)

#set3
sorteo2 = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
print(sorteo2)
sorteo2.add("Damián")
print(sorteo2)

#substring1
frase = "Controlar la complejidad es la esencia de la programación"
frase[0:9]

#substring2
frase2 = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
frase2[9::3]
print(frase2)

#substring3
frase3 = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(frase3[::-1])

#practicafinal
texto = input("Ingrese un texto: ")
print("\nIngrese 3 letras")
letra1 = input("Primera letra: ")
letra2 = input("Segunda letra: ")
letra3 = input("Tercera letra: ")
contarLetra1 = texto.lower().count(letra1.lower())
contarLetra2 = texto.lower().count(letra2.lower())
contarLetra3 = texto.lower().count(letra3.lower())
listaTexto = texto.split()
contarPalabras = len(listaTexto)
primerLetra = texto[0]
ultimaLetra = texto[-1]
textoInvertido = " ".join(listaTexto[::-1])

print(f'El texto ingresado fue: "{texto}"')
print(f"Las letras ingresadas fueron {letra1}, {letra2} y {letra3}\n")
print(f"Se ha encontrado {contarLetra1} veces la letra {letra1}")
print(f"Se ha encontrado {contarLetra2} veces la letra {letra2}")
print(f"Se ha encontrado {contarLetra3} veces la letra {letra3}")
print(f"Se han encontrado {contarPalabras} palabras en el texto")
print(f"La primera y ultima letra del texto son {primerLetra} y {ultimaLetra}, respectivamente")
print(f"El texto invertido resulta: {textoInvertido}")
print(f'La palabra "Python"{" " if "Python" in texto else " no"} se encuentra en el texto')