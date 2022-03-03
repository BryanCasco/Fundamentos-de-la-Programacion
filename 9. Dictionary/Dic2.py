# Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas 
# # claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

n = int(input("Escribe un número:"))
c = {}

for num in range(1,n+1):
    c[num] = num ** 2
for num, valor in c.items():
    print("%d -> %d" % (num,valor))
