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

#Ejercicio ciclo while
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

