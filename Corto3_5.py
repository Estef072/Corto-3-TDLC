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

E = [
    {'restaurant': 'McDonalds', 'year': 1940},
    {'restaurant': 'Burger King', 'year': 1954},
    {'restaurant': 'Panda Express', 'year': 1983},
    {'restaurant': 'Carls Jr.', 'year': 1056}
    ]

F = [
    {'brand': 'BMW', 'model': 'Z4 Roadster', 'year': 2009},
    {'brand': 'Audi', 'model': 'Audi Q3', 'year': 2023},
    {'brand': 'Bentley', 'model': 'Mulliner', 'year': 2013},
    {'brand': 'Mercedes Benz', 'model': 'GLE Coupes', 'year': 2021}
    ]

ordenar = lambda lista, llave: sorted(lista, key = lambda k: k[llave])

print("Ejercicio 1 \n", ordenar(D, 'model'), "\n")
print("Ejercicio 2 \n", ordenar(E, 'restaurant'), "\n")
print("Ejercicio 3 \n", ordenar(F, 'year'), "\n")

"""
Inciso 2
Calcular la n-esima potencia de cada elemento en una lista
"""
print("Inciso 2=======================================")

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
e = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

power = lambda lista, pwr: [element**pwr for element in lista]

print("Ejercicio 1, n = 3 \n", c, "\n",power(c, 3), "\n")
print("Ejercicio 2, n = 2 \n", d, "\n",power(d, 2), "\n")
print("Ejercicio 3, n = 3\n", e," \n",power(e, 3), "\n")

""" 
Inciso 3
Dada una matriz lista de listas calcular la transpuesta de la matriz
"""
print("Inciso 3=======================================")

X = [[1, 2, 3, 1],
     [4, 5, 6, 0],
     [7, 8, 9, -1]]

Y = [[2, 1, -3, 2],
     [-4, 2, 4, -1],
     [-2, 1, 1, 4]]

Z = [[5, 6],
     [7, 8]]
     
transpuesta = lambda lista: list(map(list, zip(*lista)))

print("Ejercicio 1", X,"\n",transpuesta(X), "\n")
print("Ejercicio 2", Y,"\n",transpuesta(Y), "\n")
print("Ejercicio 3", Z,"\n",transpuesta(Z), "\n")

"""
Inciso 4
Revertir todos los strings en una lista
"""
print("Inciso 4=======================================")

cuatro = ['rojo', 'verde', 'aZul', 'Blanco', 'negro']
cinco = ['hola', 'como', 'estas', 'Espero', 'QUE', 'bIen']
seis = ['laboratorio', 'de', 'teoría', 'con', 'corto']

reverse = lambda lista: [element[::-1] for element in lista]

print("Ejercicio 1", cuatro,"\n",reverse(cuatro), "\n")
print("Ejercicio 2", cinco,"\n",reverse(cinco), "\n")
print("Ejercicio 3", seis,"\n",reverse(seis), "\n")

""" 
Inciso 5
Borrar una lista de elementos de otra lista
"""
print("Inciso 5=======================================")

a = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
b = ['amarillo', 'cafe', 'blanco']

f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
g = [2, 4, 6, 8, 10]

h = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
i = ['marzo', 'mayo']

filterOut = lambda lista, retirar: [element for element in lista if element not in retirar]

print("Ejercicio 1", a,"\n",b,"\n",filterOut(a, b), "\n")
print("Ejercicio 2", f,"\n",g,"\n",filterOut(f, g), "\n")
print("Ejercicio 3", h,"\n",i,"\n",filterOut(h, i), "\n")
