"""
Corto 3 de Teoría de la Computación
__author__ = ["Estefania Elvira","Priscilla Gonzales","Cayetano Molina","Jose Monzon"]
"""

""" 
Inciso 1
Dada una lista de diccionarios, ordenar los diccionatios por la clave dada:
"""
print("Inciso 1=======================================")

D = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Apple', 'model': 2, 'color': 'Silver'},
    {'make': 'Huawei', 'model': 50, 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
    ]

ordenar = lambda lista, llave: sorted(lista, key = lambda k: k[llave])

print(D,"\n",ordenar(D, 'model'))

"""
Inciso 2
Calcular la n-esima potencia de cada elemento en una lista
"""
print("Inciso 2=======================================")

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

power = lambda lista, pwr: [element**pwr for element in lista]

print(c,"\n",power(c, 3))

""" 
Inciso 3
Dada una matriz lista de listas calcular la transpuesta de la matriz
"""
print("Inciso 3=======================================")

X = [[1, 2, 3, 1],
     [4, 5, 6, 0],
     [7, 8, 9, -1]]

transpuesta = lambda lista: list(map(list, zip(*lista)))

print(X,"\n",transpuesta(X))

"""
Inciso 4
Revertir todos los strings en una lista
"""
print("Inciso 4=======================================")

cuatro = ['rojo', 'verde', 'aZul', 'Blanco', 'negro']

reverse = lambda lista: [element[::-1] for element in lista]

print(cuatro,"\n",reverse(cuatro))

""" 
Inciso 5
Borrar una lista de elementos de otra lista
"""
print("Inciso 5=======================================")

a = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
b = ['amarillo', 'cafe', 'blanco']

filterOut = lambda lista, retirar: [element for element in lista if element not in retirar]

print(a,"\n",b,"\n",filterOut(a, b))
