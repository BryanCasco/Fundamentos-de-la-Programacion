# ¿Qué es Python?
Pyhon es un lenguaje de programación de alto nivel, orientados a objetos, con una semántica dinámica, integrada principalmente para el desarrollo web y de aplicaciones informáticas.


# ¿Qué es una variable?
Una variable se puede entender como una especie de caja en la que se puede guardar un valor (por ejemplo, un valor numérico). Esa caja suele corresponder a una posición de memoria en la memoria del ordenador.Las variables se representan también mediante letras o palabras completas: x, y, a, b, nombre, apellidos, edad, etc.


## Nombrando una variable
- El nombre de una variable debe empezar por una letra o por un guion bajo (_) y puede seguir con más letras, números o guiones bajos.   

- Los nombres de variables no pueden incluir espacios en blanco.

- Los nombres de variables pueden contener cualquier carácter alfabético (los del alfabeto inglés, pero también ñ, ç o vocales acentuadas) aunque lo más recomendado es que uses   solo caracteres en inglés. 
```
a = 2
nombre = "Bryan Casco"
```


## Asignando valores a una variable
Para asignar un valor a una variable se utiliza el operador de igualdad (=). A la izquierda de la igualdad se escribe el nombre de la variable y a la derecha el valor que se  quiere dar a la variable. No utilizar los nombres de las funciones de python como variables.
```
FORMA CORRECTA DE ASIGNAR VALORES 
b = 0 
fecha_de_nacimiento: 10/10/21
```
```
FORMA INCORRECTA DE ASIGNAR VALORES 
0 = b 
if = 2
```

## Operadores básicos

### Suma
El signo (+) es el operador de suma. Se utiliza para sumar 2 valores.

```
a1 = 2
a2 = 3

sum = a1 + a2

print(sum)

[Output] 5
```

### Resta
El signo (-) es el operador de sustracción. Se utiliza para restar el segundo valor del primer valor.

```
a1 = 2
a2 = 3

res = a1 - a2

print(res)

[Output] -1
```

### Multiplicación
El signo (*) es el operador de multiplicación. Se utiliza para encontrar el producto de 2 valores.

```
a1 = 2
a2 = 3

mul = a1 * a2

print(mul)

[Output] 6
```

### División
El signo (/) es el operador de división. Se utiliza para encontrar el cociente cuando el primer operando se divide por el segundo.

```
a1 = 3
a2 = 2

div = a1 / a2

print(div)

[Output] 1.5
```

### Módulo
El signo (%) es el operador de módulo. Se utiliza para encontrar el resto cuando el primer operando se divide por el segundo.

```
a1 = 2
a2 = 3

mod = a1 % a2

print(mod)

[Output] 1
```

# Tipos de datos en Python

## Integer
Los enteros en Python o también conocidos como int, son un tipo de datos que permite representar números enteros, es decir, positivos y negativos no decimales.
```
a = 2
print(a)          
print(type(a))   #Class "int"
[Output] 2
```

## Float
Float permite representar un número positivo o negativo con decimales, es decir, números reales. 
```
a = 0.10093
print(a)       
print(type(a))   #Class "float"
[Output] 0.10093
```


## String
Las cadenas en Python o strings son un tipo inmutable que permite almacenar secuencias de caracteres. Para crear una, es necesario incluir el texto entre comillas dobles "
```
a = "Hola Mundo"     #a = 'Hola Mundo'
print(a)       
print(type(a))       #Class "str", tambièn es valido comillas simples ''
[Output] Hola Mundo
```


## Casting en Python
Hacer un cast o casting significa convertir un tipo de dato a otro. Anteriormente hemos visto tipos como los int, string o float. Pues bien, es posible convertir de un tipo a otro. 

- Conversión implícita: Es realizada automáticamente por Python. Sucede cuando realizamos ciertas operaciones con dos tipos distintos.
```
a = 1      # Class 'int'
b = 2.3    # Class 'float'

a = a + b
print(a)       
print(type(a)) # Class 'float'
[Output] 3.3 
``` 
Si intentamos sumar un int a un string, tendremos un error TypeError, es lógico que esto sea así, ya que en este caso b era "2.3", pero si fuera "Hola". ¿Cómo se podría sumar eso? No tiene sentido.

```
a = 1
b = "2.3"

c = a + b    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

- Conversión explicita. Por otro lado, podemos hacer conversiones entre tipos o cast de manera explícita haciendo uso de diferentes funciones que nos proporciona Python. 

Convertir float a int

Para convertir de "float a int" debemos usar float(). Pero mucho cuidado, ya que el tipo entero no puede almacena decimales, por lo que perderemos lo que haya después de la coma.
```
a = 3.5
a = int(a)
print(a)
[Output] 3
```
Convertir float a string

Podemos convertir un "float a string" con str(). Podemos ver en el siguiente código como cambia el tipo de a después de hacer el cast.
```
a = 3.5
print(type(a)) # CLass "float"
a = str(a)
print(type(a)) # Class "str"
```
Convertir string a float

Podemos convertir un "string a float" usando float(). Es importante notar que se usa el . como separador.
```
a = "35.5"
print(float(a))
[Output] 35.5
``` 

## List
Las listas en Python son un tipo de dato que permite almacenar datos de cualquier tipo. Son mutables y dinámicas, lo cual es la principal diferencia con los sets y las tuplas.

- Crear listas Python

Son uno de los tipos o estructuras de datos más versátiles del lenguaje, ya que permiten almacenar un conjunto arbitrario de datos. Es decir, podemos guardar en ellas prácticamente lo que sea. Si vienes de otros lenguajes de programación, se podría decir que son similares a los arrays.
```
lista = [1, 2, 3, 4]
``` 

También se puede crear usando list y pasando un objeto iterable.
```
lista = list("1234")
```
Una lista sea crea con [] separando sus elementos con comas ,. Una gran ventaja es que pueden almacenar tipos de datos distintos.
```
lista = [1, "Hola", 3.67, [1, 2, 3]]
``` 

## Tuple
Las tuplas en Python son un tipo o estructura de datos que permite almacenar datos de una manera muy parecida a las listas, con la salvedad de que son inmutables.

- Crear tupla Python

Son inmutables, lo que significa que no pueden ser modificadas una vez declaradas, y en vez de inicializarse con corchetes se hace con (). Dependiendo de lo que queramos hacer, las tuplas pueden ser más rápidas.
```
tupla = (1, 2, 3)
print(tupla) 
[Output] 1, 2, 3
```
También pueden declararse sin (), separando por , todos sus elementos.
```
tupla = 1, 2, 3
print(type(tupla))     #Class "tuple"
print(tupla)       
[Output] 1, 2, 3
``` 

## Dictionary
Los diccionarios en Python son una estructura de datos que permite almacenar su contenido en forma de llave y valor.

- Crear diccionario Python

Un diccionario en Python es una colección de elementos, donde cada uno tiene una llave key y un valor value. Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par key: value. En el siguiente ejemplo tenemos tres keys que son el nombre, la edad y el documento.
```
a = {
  "Nombre": "Bryan",
  "Edad": 17,
  "Documento": 11526362
}
print(a)
#{'Nombre': 'Bryan', 'Edad': 17, 'Documento': 11526362}
```
## List

## Tuple

## Dictionary

# Tomando decisiones

## Sentencia if

## Ciclo For

## Ciclo While

## Break

## Continue
