#Digita un numero e imprime sus múltiplos
 
numero = int(input("Dame un numero: "))
 
lista = []
 
for i in range(1,11):
    lista.append(i*numero)
 
print(lista)

