# Calcular el promedio de un alumno que tiene 70calificaciones en calculo 

n=7 
suma=0 
for i in range(n): 
    nota = int(input('Ingrese nota ' + str(i) +  ': ')) 
    suma= suma + nota 

    promedio= suma/n
    print('Promedio:',promedio) 
