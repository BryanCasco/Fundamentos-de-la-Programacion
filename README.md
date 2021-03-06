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
while = 2
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


# Tomando decisiones

## Sentencia if
La sentencia condicional if nos permite comprobar si se cumple una cierta condición con el fin de ejecutar un proceso u otro. En su forma más simple se utiliza la palabra reservada if seguida de la condición a evaluar y dos puntos. Es decir, la estructura de esta sentencia es, por lo tanto, la condición es una expresión que devuelve un booleano (True/False). Por ejemplo:

```
n = 2 
if n == 2: 
print('Es un dos') 
[Output] Es un dos 
``` 

Si queremos especificar qué código hay que ejecutar en el caso de que la condición no se cumpla podemos añadir la sentencia "else".En este código estamos comprobando si n toma el valor 2. En caso de que sea así, se ejecuta la función print que muestra el texto "Es un dos". Si no se cumple, se ejecuta la función print que muestra el texto "No es un dos". 

``` 
n = 2 
if n == 2: 
print('Es un dos') 
else: 
print('No es un dos') 
[Output] No es un dos
``` 

Podemos añadir tantas instrucciones elif como deseemos. Se evaluarán en orden y así que se cumpla una de las condiciones, se ejecutará el código sangrado que la sigue.

## Ciclo For 
La sentencia iterativa for nos permite ejecutar un proceso un número determinado de veces o para un conjunto determinado de valores. 
Si quisiéramos leer esta instrucción sería algo como "para cada valor que hay en serie de valores, asigna dicho valor a 'variable' y ejecuta el código que le sigue". Es decir, se va a ejecutar el código una vez para cada uno de los elementos en "serie-de-valores". Comencemos por el ejemplo más simple, cuando la serie de valores son números:

```
for n in [1,2,3] 
print(n) 
[Output] 1 2 3 
``` 
En un caso como éste, en lugar de incluir la lista explícita de valores que va a tomar la variable n puede utilizarse una función como range. Esta genera un conjunto de números entre dos valores, pudiendo especificarse el incremento entre los valores. Simplemente se crea un "objeto range" que irá generando ese millón de números cuando se soliciten.

``` 
for n in range (1,4): 
print(n) 
[Output] 0 1 2 3  
``` 


## Ciclo While
Los bucles while no se repiten un número determinado de veces, sino mientras se cumpla una condición. Si quisiéramos leerlo sería algo como "Mientras se cumpla la condición, ejecuta el código y vuelve a evaluar si se sigue cumpliendo la condición". La condición es una expresión que devuelve un booleano (True/False). Y, nuevamente, el código que deseamos ejecutar dentro del bucle deberá aparecer sangrado con cuatro espacios en blanco o un tabulador. Por ejemplo: 

```
n = 1 
while n < 8: 
print(n)
n = n + n  
[Output] 1 2 4
``` 

Veamos con detalle cómo se ejecutaría este código:

- Inicialmente n toma el valor 1 (primera línea del código).
- Llegamos al bucle while y la primera línea del mismo (while n < 8) comprueba si se cumple la condición "¿es n menor que 8?". Sí, se cumple, de forma que se ejecuta el código     que hay en el interior del bucle, imprimiendo n y asignando a n un nuevo valor resultante de sumar a n su propio valor. Es decir, ahora n vale 2.
- Y volvemos al comienzo del bucle y volvemos a preguntarnos si la condición se sigue cumpliendo "¿es n menor que 8?" Sí, por lo que se vuelve a ejecutar el código del bucle y     se asigna a n el nuevo valor de 4 (= 2 + 2).
- Vuelve a cumplirse la condición de ser n menor que 8, por lo que se vuelve a ejecutar el código del bucle. Y se asigna a n el nuevo valor de 8 (= 4 + 4).
- Y volvemos al comienzo del bucle y a preguntarnos "¿es n menor que 8?" Y ahora la respuesta es negativa (8 no es menor que 8), por lo que no se ejecuta el código del bucle y     el programa continuaría ejecutando las instrucciones que hubiese a continuación.


## Break
Los bucles for y while pueden ser interrumpidos con la sentencia break: cuando se ejecuta, el programa sale del bucle y continúa ejecutando el resto del código: 

```
for n in range (1000): 
print(n) 
if n == 3: 
break 
[Output] 0 1 2 3 
``` 


## Continue
La sentencia continue, cuando se ejecuta, obliga a Python a dejar de ejecutar el código que haya dentro del bucle y a iniciar una nueva iteración (es decir, a volver al comienzo del bucle y seguir con la ejecución del programa):

```
for n in range (5): 
if n == 3: 
continue
[Output] 0 1 3 4 
``` 

