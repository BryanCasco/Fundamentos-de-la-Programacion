#Dada la fecha de hoy 
# Calcular la fecha del sia siguiente 
#Suponer que el año no es bisiesto 
d=int(input("Introduce el dia: "))
m=int(input("Introduce el mes: "))
a=int(input("Introduce el año: "))

if a%4==0 and a%100!=0 or a%400==0:
    print(a," es un año bisiesto")
else:
    print(a," no es un año bisiesto")

if m<=0 or m>12 or d<=0 or d>31 or a<0: 
    print("Fecha incorrecta")
elif m in [1, 3, 5, 7, 8, 10, 12]: 
    if d==31 and m==12: 
        a=a+1  
        m=1
        d=1
    elif d==31 and m!=12: 
        m=m+1  
        d=1    
    else: 
        d=d+1 
    print("La fecha siguiente es {}/{}/{}".format(d,m,a))
elif m in [4, 6, 9, 11] and d<=30: 
    if d==30: 
        m=m+1 
        d=1
    else: 
        d=d+1 
    print("La fecha siguiente es {}/{}/{}".format(d,m,a))
elif m==2 and d<=29: 
    if d==29: 
        m=m+1
        d=1
    else: 
        d=d+1 
    print("La fecha siguiente es {}/{}/{}".format(d,m,a))
else:
    print("Fecha incorrecta")

