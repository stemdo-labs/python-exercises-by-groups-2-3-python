#@dnazareno
#atributos1
class Casa:
    def __init__(self,color,cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca=Casa("blanco",4)

print(casa_blanca.color)
print(casa_blanca.cantidad_pisos)

#atributos2
class Cubo:
    caras = 6
    def __init__(self,color):
        self.color=color

cubo_rojo=Cubo("rojo")

print(cubo_rojo.color)
print(cubo_rojo.caras)

#clases1
class PlataformaStreaming:
    pass

netflix=PlataformaStreaming()
hbo_max=PlataformaStreaming()
amazon_prime_video=PlataformaStreaming()

#herencia1
class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

class Alumno(Persona):
    pass

david=Alumno("David",32)

print(david.nombre)
print(david.edad)

#herencia2
#igual a herencia1

#Metodos1
class Mascota:

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

Mascota.respirar()

#Metodos2
class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo=True

print(Jugador.vivo)
Jugador.revivir()
print(Jugador.vivo)

#Polimorfismo1
lista=["Pedro",["a","b"],(1,2,3)]
for l in lista:
    print(len(l))

#Polimorfismo2
class Arquero:
    def atacar(self):
        print('El arquero ha usado "True Shot"')

class Mago:
    def atacar(self):
        print('El arquero ha usado "Frozen Orb"')

class Samurai:
    def atacar(self):
        print('El samurai ha usado "Mortal Strike"')

kreynest=Arquero()
eternelle=Mago()
baffi=Samurai()

personajes=[kreynest,eternelle,baffi]

for p in personajes:
    p.atacar()