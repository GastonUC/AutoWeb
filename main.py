# import AutoWeb
import math


var = 8
pos = []

for x in range(var):
    pos.append(x+1) #Llenando la list con la cantidad de valores entregados por "var"
    # print(pos)

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

print("Array sorted: ")
print(pos)