# Corto 3 - Teoria de la Computacion
Este corte tiene el objetivo de verificar los conocimientos sobre las funciones lambda.

## Funciones
- Ordenar un diccionario dada una key
```python
ordenar = lambda lista, llave: sorted(lista, key = lambda k: k[llave])
```
- Elevar los elementos de una lista a una potencia
```python
power = lambda lista, pwr: [element**pwr for element in lista]
```
- Encontrar la transpuesta de una matriz
```python
transpuesta = lambda lista: list(map(list, zip(*lista)))
```
- Revertir todos los strings de una lista
```python
reverse = lambda lista: [element[::-1] for element in lista]
```
- Eliminar elementos en una lista de otra
```python
filterOut = lambda lista, retirar: [element for element in lista if element not in retirar]
```
