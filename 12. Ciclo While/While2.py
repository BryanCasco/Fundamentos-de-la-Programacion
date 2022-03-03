#Escriba una contraseña y luego a escribir, si escribe de forma correcta el prgrama se cierra
#pero si lo hace de forma incorrecta el programa sigue
def main():
    print("CONFIRME SU CONTRASEÑA")
    password_1 = input("Escriba su contraseña: ")
    password_2 = input("Escriba de nuevo su contraseña: ")

    while password_1 != password_2:
        print("Las contraseñas no coinciden. Inténtelo de nuevo.")
        password_1 = input("Escriba su contraseña: ")
        password_2 = input("Escriba de nuevo su contraseña: ")

    print("Contraseña confirmada. ¡Hasta la vista!")


if __name__ == "__main__":
  main()