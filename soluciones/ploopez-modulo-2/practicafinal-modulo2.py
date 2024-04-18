nombre = input("Introduzca su nombre: ")
monto = input("Introduzca el monto de ventas del mes: ")
monto = float(monto)
monto = monto * 0.13
monto= round(monto,2)

print(f"{nombre}, ha obtenido una comisión en ventas de {monto}")
