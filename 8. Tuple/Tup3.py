#Escribe números y después selecciona cual es el máximo y cuál es el mínimo 
numeros = (5,4,3,-2,1,6,455,3,6,6,6,6,6)
 
maximo = numeros[0]
minimo = numeros[0]
 
for i in numeros:
    if i > maximo:
        maximo = i
 
    if i < minimo:
        minimo = i
 
print("El maximo es ",maximo)
print("El minimo es ",minimo)