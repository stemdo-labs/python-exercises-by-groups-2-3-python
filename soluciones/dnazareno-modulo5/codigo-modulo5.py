#@dnazareno
#argumentos1
def suma_cuadrados(*args):
    '''función que tome una cantidad indeterminada de argumentos numéricos, 
    y que retorne la suma de sus valores al cuadrado'''
    
    total = 0
    for a in args:
        total += (a*a)
    return total

print(suma_cuadrados(1,2,3))

#argumentos2
def suma_absolutos(*args):
    '''función que tome un conjunto de argumentos de cualquier extensión, 
    y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, 
    o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).'''

    total = 0
    for a in args:
        total += abs(a)
    return total

print(suma_absolutos(1,2,-3))

#argumentos3
def numeros_persona(nombre,*args):
    '''función que reciba, como primer argumento, un nombre, 
    y a continuación, una cantidad indefinida de números.
    La función debe devolver el siguiente mensaje:
    "{nombre}, la suma de tus números es {suma_numeros}"'''

    total = 0
    for a in args:
        total += a
    return nombre + ", la suma de tus números es " + str(total)

print(numeros_persona("David",1,2,3))

#funciones
def cuadrado(un_numero):
    '''función que toma como argumento un número cualquiera, 
    y que cada vez que es llamada, imprime en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).
    El nombre del argumento que toma dicha función es un_numero'''

    return un_numero*un_numero

un_numero = 3.1415
print(cuadrado(un_numero))

