#Solicitar al usuario la inicial del dia de la semana y
# mostrar el nombre del dia completo 

dia= input("INGRESE EL DIA: ") 

dia = dia.lower()

if dia == "l": 
    print("Lunes")
elif dia == "m": 
    print("Martes")
elif dia == "x": 
    print("Miercoles") 
elif dia == "j": 
    print("Jueves") 
elif dia == "v": 
    print("Viernes") 
elif dia == "s": 
    print("Sabado") 
elif dia == "d": 
    print("Domingo")
else: 
    print("Dia incorrecto")
    