#Ingresa un tipo de moneda y que imprima el signo de la moneda que escribiste

monedas = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))
