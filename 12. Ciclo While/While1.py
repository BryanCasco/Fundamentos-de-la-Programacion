#Realizar una pregunta donde para finalizar el progama debera responder SI
def main():
    print("DIGA SI PARA TERMINAR")
    respuesta = input("¿Desea terminar el programa?: ")

    while respuesta != "SI":
        respuesta = input("¿Desea terminar el programa?: ")

    print("¡Hasta la vista!")


if __name__ == "__main__":
    main()