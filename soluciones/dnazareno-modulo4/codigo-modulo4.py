# @dnazareno
#comparacion1
num1 = 36
num2 = 17
mi_bool = num1 >= num2
print(mi_bool)

#comparacion2
import math
num1 = math.sqrt(25)
num2 = 5
mi_bool2 = num1 == num2
print(mi_bool2)

#comparacion3
num1 = 64*3
num2 = 24*8
mi_bool3 = num1 != num2
print(mi_bool3)

#operadoreslogicos1
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 and num1 < num3
print(mi_bool)

#operadoreslogicos2
num1 = 36
num2 = 72/2
num3 = 48
mi_bool = num1 > num2 or num1 < num3
print(mi_bool)

#practicafinal
import random
nombre = input("Ingrese su nombre: ")
print("He pensado en un numero del 1 al 100\nIntente adivinarlo. Tiene 8 intentos.")
aleatorio = random.randint(1,100)
intentos_restantes = 8

while intentos_restantes > 0:
    print("-------------------------------")
    print(f"Intento nro {9 - intentos_restantes}")
    intento = input("¿En qué número estoy pensando? Numero: ")
    intento = int(intento)
    if intento < 1 or intento > 100:
        print("Recuerde que estoy pensando en uno entre el 1 y el 100. A ingresado un número que está fuera del rango.")
    if intento >= 1 and intento < aleatorio:
        print("Ese no es el número en el que estoy pensando. Usted pensó en un número demasiado pequeño.")
    if intento <= 100 and intento > aleatorio:
        print("Ese no es el número en el que estoy pensando. Usted pensó en un número muy grande.")
    if intento == aleatorio:
        print("Correcto!!!")
        print(f"Lo consiguó en {9 - intentos_restantes} intentos")
        break
    intentos_restantes -= 1
else:
    print(f"El nro en el que estaba pensando era el {aleatorio}")
