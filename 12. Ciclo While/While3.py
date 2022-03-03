#Escriba un programa donde la ùnica forma para que termine el programa es escribir
#la palabra chao
def main():
    print("DIGA chao PARA TERMINAR")
    respuesta = input("¿Desea continuar el programa?: ")

    while respuesta != "chao":
        respuesta = input("¿Desea continuar el programa?: ")

    print("¡Hasta la vista!")


if __name__ == "__main__":
    main()