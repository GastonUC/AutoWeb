# import AutoWeb
import math


var = 4
pos = []

for x in range(var):
    pos.append(x+1) #Llenando la list con la cantidad de valores entregados por "var"

print("Array completo: ") 
print(pos) #Muestra el contenido del array

med = math.trunc(len(pos)/2)
print(med) #Muestra la mitad del array, en caso de ser float lo aproxima.

if(var == 4) or (var == 6) or (var == 8): #Solución mala al primer cambio de los items.
    med = med - 1

print(med)

posIni = pos[0]
posMed = pos[med]
pos[med] = posIni   #Cambio '1' de posición 0 a posición del medio, guardando el número del medio en variable "posMed" para luego llevarlo a posición 0.
pos[0] = posMed

print("Array with one item sorted: ")
print(pos)

posF = var - 1 #Guarda el index del valor final del array.
posFin = pos[posF] #Guarda el valor de la posición final.
posFinSor = med - 1 #Guarda el index del valor antes del '1'.
pos2 = pos[posFinSor] #Guarda el valor de la posición antes del '1'.
pos[posFinSor] = posFin
pos[posF] = pos2

print("Array with second item sorted:")
print(pos)

## Páginas abiertas:
# -https://www.geeksforgeeks.org/sort-the-array-in-a-given-index-range/
# -