#Comparaciones / operador igual ==
2 == 2 #True
2 == 2. #True
1 == 2 #False

var = 0
print(var == 0)

var = 1
print(var == 0)

#Desigualdad !=
var = 0
print(var != 0)

var = 1
print(var != 0)

#Mayor que >
3 > 1

#Mayor o igual que >=
3 >= 3

#Menor que <
3 < 5

#Menor o igual que <=
5 <= 5

#Obtener un número mayor o igual que 100
n = int(input("Ingresa un número: "))
print(n >= 100)

#if-else y elif
#¿Cuál es el número más grande?
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

if numero1> numero2:
    nmasGrande = numero1
else:
    nmasGrande = numero2

print("El número más grande es:", nmasGrande)

#Pequeña curiosidad, si solo se ejecuta una línea en el if y/o else se puede escribir después de los : de la condicional y else
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))

if numero1 > numero2: nmasGrande = numero1
else: nmasGrande = numero2

print("El número más grande es: ", nmasGrande)

#¿cuál es el número mayor de 3
numero1 = int (input("Ingresa el primer número:"))
numero2 = int (input("Ingresa el segundo número:"))
numero3 = int (input("Ingresa el tercer número:"))

#Asumimos temporalmente que el primer número es el más grande lo verificaremos pronto
nmasGrande = numero1

if numero2 > nmasGrande:
    nmasGrande = numero2

if numero3 > nmasGrande:
    nmasGrande = numero3

print("El número más grande es:", nmasGrande)

#Uso de las condicionales e input()
nombre = input("Ingresa un nombre: ")

if nombre == "Espatifilio":
    print("Si, ¡El Espatifilo es la mejor planta de todos los tiempos!")
elif nombre == "espatifilio":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("¡Espatifilo! ¡No " + nombre + " !")

#Calculadora de impuestos
ingreso=float(input("Ingrese el ingreso anual:"))

if ingreso <= 85_528:
    impuesto = ingreso * 0.18 -556.2
else:
    excedente = (ingreso - 85_528) * 0.32
    impuesto = excedente + 14_839.2

if impuesto < 0:
    impuesto = 0.0

impuesto = round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")

#Año bisiesto
año = int(input("Introduzca un año: "))

if año >= 1582: #Comprueba si el año ingresado es permitido por el calendario
    if (año % 4) != 0:
        print("Año común")
    else:
        if (año % 100) != 0:
            print("Año Bisiesto")
        else:
            if (año % 400) != 0:
                print("Año Común")
            else:
                print("Año Bisiesto")
else:
    print("No dentro del período del calendario gregoriano")

#Puntos clave del If-Else
x = 5
y = 10
z = 8

print(x > y) #False
print(y > z) #True

x, y, z = 5, 10, 8

print(x > z) #False
print((y - 5) == x) #True

x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z) #True
print((y - 5) == x) #False

x = 10

if x == 10: #True
    print(x == 10) 
if x > 5: #True
    print(x > 5)
if x < 10: #False
    print(x < 10)
else: #No entra
    print("else") 

x = "1"

if x == 1: #False
    print("uno")
elif x == "1": #True
    if int (x) > 1: #False
        print("dos")
    elif int (x) < 1: #False
        print("tres")
    else: #Aquí entra
        print("cuatro")
if int (x) == 1: #True
    print("cinco")
else: #Aquí no entra
    print("seis") 

x = 1
y = 1.0
z = "1"

if x == y: #True
    print("uno")
if y == int (z): #True
    print("dos")
elif x == y: #No entra ya que el anterior if es correcto
    print("tres")
else: #Tampoco entra
    print("cuatro")

#Ciclo While
# Almacenaremos el número más grande actual aquí
numeroMayor = -999999999

# Ingresa el primer valor
numero = int(input ("Introduzca un número o escriba -1 para detener:"))

# Si el número no es igual a -1, continuaremos
while numero != -1:
   # ¿Es el número más grande que el número más grande?
   if numero > numeroMayor:
       # Sí si, actualiza el mayor númeroNúmero
       numeroMayor = numero
   # Ingresa el siguiente número
   numero = int (input("Introduce un número o escribe -1 para detener:"))

# Imprimir el número más grande
print("El número más grande es:", numeroMayor)

#Ejemplo ciclo while
# programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares
# programa termina cuando se ingresa cero

numerosImpares = 0
numerosPares = 0

# lee el primer número
numero = int (input ("Introduce un número o escriba 0 para detener:"))

# 0 termina la ejecución
while numero:
    # verificar si el número es impar
    if numero % 2:
        # aumentar el contador de números impares
        numerosImpares += 1
    else:
        # aumentar el contador de números pares
        numerosPares += 1
    # lee el siguiente número
    numero = int (input ("Introduce un número o escriba 0 para detener:"))

# imprimir resultados
print("Números impares: ", numerosImpares)
print("Números pares: ", numerosPares)

#Diferentes formas de utilizar el while
contador = 5
while contador != 0:
    print("Dentro del ciclo: ", contador)
    contador -= 1
print("Fuera del ciclo", contador)

contador = 5
while contador:
    print("Dentro del ciclo.", contador)
    contador -= 1
print("Fuera del ciclo", contador)

#Ejercicio del ciclo while
numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
numero = int(input())

while numero != numeroSecreto:
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    numero = int(input("Te daré otra oportunidad: "))
print("¡Bien hecho, muggle! Eres libre ahora")

#Ciclo For
for i in range(10):
    print("El valor de i es actualmente", i)

for i in range (2, 8):
    print("El valor de i es actualmente", i)

pow = 1
for exp in range(16):
    print ("2 a la potencia de", exp, "es", pow)
    pow *= 2 

#Ejercicio For: contar con Mississippis
import time

for cuenta in range(1,6):
    print(str(cuenta) + " Mississippi")
    time.sleep (1)
print("¡Listo o no, ahí voy!")

# break - ejemplo

print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continua - ejemplo

print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

#Ejemplo de número mayor con break
numeroMayor = -99999999
contador = 0

while True:
    numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))
    if numero == -1:
        break
    contador = 1
    if numero > numeroMayor:
        numeroMayor = numero

if contador != 0:
    print("El número más grande es", numeroMayor)
else:
    print("No ha ingresado ningún número") 

#Ejemplo de número mayor con continue
numeroMayor = -99999999
contador = 0

numero = int (input("Ingresa un número o escribe -1 para finalizar el programa: "))

while numero != -1:
    if numero == -1:
        continue
    contador = 1

    if numero > numeroMayor:
        numeroMayor = numero
    numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa: "))

if contador:
    print("El número más grande es", numeroMayor)
else:
    print("No ha ingresado ningún número")

#Ejercicio de break
secretWord = "chupacabras"
while True:
    word = input("Ingresa la palabra secreta: ")
    if (word == secretWord):
        break
    
print("¡Has dejado el ciclo con éxito")

#Ejercicio continue
userWord = input("Ingresa una palabra: ")
userWord = userWord.upper()

for letra in userWord:
    if (letra == "A"):
        continue
    elif (letra == "E"):
        continue
    elif (letra == "I"):
        continue
    elif (letra == "O"):
        continue
    elif (letra == "U"):
        continue
    else:
        print(letra)

palabraSinVocal = ""
userWord = input("Ingresa una palabra: ").upper()

for letra in userWord:
    
    if (letra == "A"):
        continue
    elif (letra == "E"):
        continue
    elif (letra == "I"):
        continue
    elif (letra == "O"):
        continue
    elif (letra == "U"):
        continue
    else:
        palabraSinVocal += letra
    
print(palabraSinVocal)

#While con else
i = 1
while i < 5:
    print (i)
    i += 1
else:
    print("else:", i)

#For con else
for i in range(5):
    print(i)
else:
    print("else:", i)

#Ejercicio de while
bloques = int(input("Ingrese el número de bloques: "))
altura = 0

while (bloques > 0):
    altura += 1
    bloques -= altura
    
    if(bloques < 0):
        altura -= 1

print("La altura de la pirámide:", altura)

c0 = int(input("Ingresa un número entero: "))
pasos = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
    pasos += 1
    print(c0)
print("pasos = " + str(pasos))

#Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla.
for i in range(1, 11):
    if (i % 2) != 0:
        print("Número: " + str(i))

#Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla.
x = 1
while x < 11:
    if (x % 2) != 0:
        print("Número: " + str(x))
    x += 1

#Crea un programa con un bucle for y una declaración break. El programa debe iterar sobre los caracteres en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea.
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end = "")

#Crea un programa con un bucle for y una declaracióncontinue. El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla.
for digit in "0165031806510":
    if digit == "0":
        print("x", end = "")
        continue
    print(digit, end = "")

#Desplazamiento Binario
var = 17
varRight = var >> 1
varLeft = var << 2
print(var, varLeft, varRight)

#Listas
#Introducción
numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros) # imprimiendo contenido de la lista original.

numeros[0] = 111
print("\nPrevio contenido de la lista:", numeros) # imprimiendo contenido de la lista anterior.

numeros[1] = numeros[4]  # copiando el valor del quinto elemento al segundo
print("Nuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual.

print("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista

del numeros[1] # eliminando el segundo elemento de la lista
print("Longitud de la nueva lista:", len(numeros)) # imprimiendo nueva longitud de la lista
print("\nNuevo contenido de la lista:", numeros) # imprimiendo el contenido de la lista actual

#Índices negativos
print(numeros[-1])
print(numeros[-2])
print(numeros[-4])

#Ejercicio de listas
listaSombrero = [1, 2, 3, 4, 5] # Esta es una lista existente de números ocultos en el sombrero.

listaSombrero[2] = int(input("Ingresa un número entero: "))

del listaSombrero[4]

print(len(listaSombrero))

print(listaSombrero)

#Listas y métodos
numeros = [111, 7, 2, 1]
print(len(numeros))
print(numeros)

numeros.append(4)
print(len(numeros))
print(numeros)

numeros.insert(0,222)
print(len(numeros))
print(numeros)

numeros.insert(1,333)
print(len(numeros))
print(numeros)

#Uso de los métodos append e insert
miLista = [] 

for i in range (5):
    miLista.append (i + 1)

print(miLista)

miLista = []

for i in range(5):
    miLista.insert(0, i + 1)

print(miLista)

#Manejos de usar el for con listas
miLista = [10, 1, 8, 3, 5]
suma = 0

for i in range(len(miLista)):
    suma += miLista[i]

print(suma)

miLista = [10, 1, 8, 3, 5]
suma = 0

for i in miLista:
    suma += i

print(suma) 

#Listas en acción
variable1 = 1
variable2 = 2

variable1, variable2 = variable2, variable1

#Formas de invertir el orden de una lista
miLista = [10, 1, 8, 3, 5]

miLista [0], miLista [4] = miLista [4], miLista [0]
miLista [1], miLista [3] = miLista [3], miLista [1]

print(miLista) 

miLista = [10, 1, 8, 3, 5]
longitud = len(miLista)

for i in range (longitud // 2):
    miLista[i], miLista[longitud-i-1] = miLista[longitud-i-1], miLista[i]

print(miLista)

#Ejercicio de listas
beatles = []
print("Paso 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

for i in range(2):
    integrante = input("Inserta un nuevo miembro: ")
    beatles.append(integrante)
print("Paso 3:", beatles)

del beatles[4]
del beatles[3]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fab", len(beatles))

#¿Cuál es la salida del siguiente fragmento de código?

lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)

print(lst)  #[6, 2, 3, 4, 5, 1]

#¿Cuál es la salida del siguiente fragmento de código?

lst = [1, 2, 3, 4, 5]
lst2 = []
agregar = 0

for number in lst:
    agregar += number
    lst2.append (agregar)

print(lst2) # [1, 3, 6, 10, 15]

#¿Cuál es la salida del siguiente fragmento de código?

lst = [1, [2, 3], 4]
print(lst[1]) # [2, 3]
print(len(lst)) # 3

#Ordenamiento Burbuja
miLista = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print(miLista) # [2, 4, 6, 8, 10]

#Ordenamiento interactivo
miLista = []
swapped = True
num = int (input("¿Cuántos elementos deseas ordenar?:"))

for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)

while swapped:
    swapped = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            swapped = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista)

#¿Cuál es la salida del siguiente fragmento de código?
lst = ["D", "F", "A", "Z"]
lst.sort ()

print(lst) #[A, D, F, Z]

#¿Cuál es la salida del siguiente fragmento de código?

a = 3
b = 1
c = 2

lst = [a, c, b]
lst.sort ()

print(lst) #[1, 2, 3]

#¿Cuál es la salida del siguiente fragmento de código?

a = "A"
b = "B"
c = "C"
d = ""

lst = [a, b, c, d]
lst.reverse ()

print(lst) #[ , C, B, A]