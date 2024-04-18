#@dnazareno
#Conversiones1
num1 = 3.5
num1 = int(num1)
print(num1)
print(type(num1))

#Conversiones2
num2 = 4
num2 = float(num2)
print(num2)
print(type(num2))

#Conversiones3
print(num1 + num2)

#Float
num_decimal = 3.1415
print(num_decimal)

#FormatearCadenas1
nombre = "David"
nro_asoc = 123456
print(f"Estimado/a {nombre}, su numero de asociado es: {nro_asoc}")

#FormatearCadenas2
puntos = 3
puntos_totales = 50
print(f"Has ganado {puntos} puntos! En total, acumulas {puntos_totales} puntos")

#FormatearCadenas3
puntos = 2
punto_anteriores = 3
print(f"Has ganado {puntos} puntos! En total, acumulas {puntos + punto_anteriores} puntos")

#Integer
num_entero = 10
print(num_entero)

#Redondeo1
print(round(10/3,2))

#Redondeo2
print(round(10.676767))

#Redondeo3
import math
print(round(math.sqrt(5),4))

#num_data
num1 = 7.5
num2 = 2.5
print(num1 + num2)
type(num1 + num2)

#variables1
nombre = "Tony Soprano"
edad = 51
print(nombre)
print(edad)

#variable2
nombre = "David"
apellido = "Boffelli"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

#variable3
curso = "Python"
print("Estas tomando un curso de " + curso)

#practicafinal
nombre= input("Ingreser su nombre: ")
monto = input("Ingrese el monto de ventas: ")
monto = float(monto)
comision = monto * 0.13
print(f"El vendedor {nombre} obtendra una comision de {round(comision,2)} euros")