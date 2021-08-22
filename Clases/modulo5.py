#Códigos y ejercicios del modulo 5
#Módulos
import math #Manera de llamar un módulo
print(math.sin(math.pi/2))

#Pueden coexistir variables con el mismo nombre que un módulo
import math

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))

#Otra forma de llamar un módulo
from math import sin, pi

print(sin(pi/2))

#Coexistencia de variables con nombres de metodos de un módulo
from math import sin, pi

print(sin(pi/2))

pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi/2))

#Otro forma de importar un módulo
from math import * #Importa todos los métodos de un módulo

#Importa todos los métodos de un módulo con un alias
import math as mate 

#Aplicando las palabras reservadas import, from, as
from math import pi as PI, sin as sine

print(sine(PI/2))

#Funcion dir()
import math

#Imprime una lista con los nombres de los métodos y variables disponibles en un módulo
for name in dir(math):
    print(name, end="\t")

#Conociendo los métodos trigonométricos del módulo math
from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)

#Conociendo los métodos de exponenciales del módulo math
from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

#Funciones de proposito general en el módulo de math
from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

#Conociendo el módulo random
from random import random, seed

for i in range(5):
    print(random())
    
seed(0)
for i in range(5):
    print(random())

#Otras funciones de random
from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

from random import randint

for i in range(10):
    print(randint(1, 10), end=',')
    
from random import choice, sample

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(lst))
print(sample(lst, 5))
print(sample(lst, 10))

#Módulo platform, para conocer las capas del sistema operativo
from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))

#Función Machine, para conocer el nombre génerico del procesador
from platform import machine
print(machine())

#Función processor, para conocer el nombre del procesador
from platform import processor
print(processor())

#Función system, para conocer el nombre del sistema operativo
from platform import system
print(system())

#Función version, para conocer la versión del sistema operativo
from platform import version
print(version())

#Funciones para conocer la versión de Python
from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

#Para importar módulos de Python que no se encuentren en la misma carpeta que el main
from sys import path
path.append('Dirección del modulo')

#Manejo de errores try y except
try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh cielos, algo salio mal...")

print("3")

#Manje de errores más específicos
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salio mal...")

print("THE END.")

#Jerarquía de excepciones
try:
    y = 1 / 0
except ZeroDivisionError: #ArithmeticError, Exception, BaseException
    print("Uuuppsss...")

print("FIN.")

#Manejo de excepciones en funciones
def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema aritmético!")
    return None

badFun(0)

print("FIN.")

def badFun(n):
    return 1 / n

try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¡Se lanzo una excepción!")

print("FIN.")

#Palabra raise sirve para simular errores del tipo que se quiera
def badFun(n):
    raise ZeroDivisionError

try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")

#Raise dentro del except, genera la misma excepción
def badFun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise

try:
    badFun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")

#Palabra assert, genera un error si no se cumple la condición
import math

x = float(input("Ingresa un numero: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)

#Ejercicio
def readint(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print("Error: entrada incorrecta")
        if ok:
            ok = value >= min and value <= max
        if not ok:
            print("Error: el valor no esta dentro del rango permitido (" + str(min) + ".." + str(max) + ")")
    return value;

v = readint("Ingresa un número entre -10 a 10: ", -10, 10)

print("El numero es:", v)

#Cadenas: Como crear una cadena multilinea
multiLinea = '''Linea #1
Linea #2'''

print(len(multiLinea))

#Concateción y replicas de cadenas
str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

# Demostrando la función ord ()

ch1 = 'a' 
ch2 = ' ' # espacio

print(ord(ch1))
print(ord(ch2))

# Demostrando la función chr()

print(chr(97)) # a
print(chr(945)) # alpha o ñ

