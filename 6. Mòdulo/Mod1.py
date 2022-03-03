#Un año es bisiesto si es divisible por 4 y no es por 100, o si es divisible por 400.
# Escribe un programa que lea un año y devuelva si es bisiesto o no. 

b=int(input("INTRODUCE EL AÑO: "))
if b%4==0 and b%100!=0 or b%400==0:
    print("ES UN AÑO BISIESTO")
else:
    print("NO ES UN AÑO BISIESTO")

 