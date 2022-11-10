
a = ['rojo', 'verde', 'azul', 'amarillo', 'gris', 'blanco', 'negro']
b = ['amarillo', 'cafe', 'blanco']

#inciso 5
filterOut = lambda lista, retirar: [element for element in lista if element not in retirar]


#Inciso 4
reverse = lambda lista: [element[::-1] for element in lista]
print(reverse(a))

#Inciso 2
power = lambda lista, pwr: [element**pwr for element in lista]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
