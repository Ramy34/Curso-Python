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

# Indexando cadenas
exampleString = 'silly walks'

for ix in range(len(exampleString)):
    print(exampleString[ix], end=' ')

print()

# Iterando a través de una cadena
exampleString = 'silly walks'

for ch in exampleString:
    print(ch, end=' ')

print()

# Rodajas o rebanadas de cadenas
alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

#Operadores In y Not In en cadenas
alpfabeto = "abcdefghijklmnopqrstuvwxyz"

print("f" in alpfabeto)
print("F" in alpfabeto)
print("1" in alpfabeto)
print("ghi" in alpfabeto)
print("Xyz" in alpfabeto)

alfabeto = "abcdefghijklmnopqrstuvwxyz"
print("f" not in alfabeto)
print("F" not in alfabeto)
print("1" not in alfabeto)
print("ghi" not in alfabeto)
print("Xyz" not in alfabeto)

#Cadenas inmutables
alfabeto = "abcdefghijklmnopqrstuvwxyz"

#del alfabeto[0] es un error
del alfabeto #Elimina la cadena

#alfabeto.append("A") es un error
alfabeto += "A" #Agrega una letra al final de la cadena

#alfabeto.insert(0, "A") es un error

# Demonstrando min() - Ejemplo 1
print(min("aAbByYzZ")) # a


# Demonstrando min() - Examplos 2 y 3
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']') # [ ]

t = [0, 1, 2]
print(min(t)) # 0

# Demostrando max() - Ejemplo 1
print(max("aAbByYzZ")) # z

# Demonstrando max() - Examplos 2 y 3
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + max(t) + ']') # [ ]

t = [0, 1, 2]
print(max(t)) # 2

# Demonstrando el método index()
print("aAbByYzZaA".index("b")) # 2
print("aAbByYzZaA".index("Z")) # 7
print("aAbByYzZaA".index("A")) # 1

# Demostrando la función list()
print(list("abcabc")) # ['a', 'b', 'c']

# Demostrando el método count()
print("abcabc".count("b")) # 2
print('abcabc'.count("d")) # 0

# Demostración del método capitalize()
print('aBcD'.capitalize()) # Abcd
print('123'.capitalize()) # 123
print("αβγδ".capitalize()) # Αβγδ

# Demostración del método center()
print('[' + 'alfa'.center(10) + ']') # [alfa]
print('[' + 'Beta'.center(2) + ']') # [Beta]
print('[' + 'Beta'.center(4) + ']') # [Beta]
print('[' + 'Beta'.center(6) + ']') # [Beta]
print('[' + 'gamma'.center(20, '*') + ']') # [gamma********]

# Demostración del método endswith()
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")
    
t = "zeta"
print(t.endswith("a")) # False
print(t.endswith("A")) # True
print(t.endswith("et")) # False
print(t.endswith("eta")) # True

# Demostración del método find()
print("Eta".find("ta")) # 2
print("Eta".find("mma")) # -1
print('kappa'.find('a', 2)) # 2

print('kappa'.find('a', 1, 4)) # 3
print('kappa'.find('a', 2, 4)) # -1

# Demostración del método the isalnum()
print('lambda30'.isalnum()) # True
print('lambda'.isalnum()) # False
print('30'.isalnum()) # False
print('@'.isalnum()) # False
print('lambda_30'.isalnum()) # False
print(''.isalnum()) # False

t = 'Six lambdas'
print(t.isalnum()) # True

t = 'ΑβΓδ'
print(t.isalnum()) # True

t = '20E1'
print(t.isalnum()) # False

# Ejemplo 1: Demostración del método isapha() letras
print("Moooo".isalpha()) # False
print('Mu40'.isalpha()) # True

# Ejemplo 2: Demostración del método isdigit() numeros
    
print('2018'.isdigit()) # True
print("Año2019".isdigit()) # False

# Ejemplo 1: Demostración del método islower() minusculas
print("Moooo".islower()) # True
print('moooo'.islower()) # True

# Ejemplo 2: Demostración del método isspace() espacio
print(' \n '.isspace()) # True
print(" ".isspace()) # True
print("mooo mooo mooo".isspace()) # False

# Ejemplo 3: Demostración del método isupper() mayusculas
print("Moooo".isupper()) # False
print('moooo'.isupper()) # False
print('MOOOO'.isupper()) # True

# Demostración del método join()
print(",".join(["omicron", "pi", "rho"])) # omicron,pi,rho

# Demostración del método lower() pasa las mayusculas a minusculas
print("SiGmA=60".lower()) # sigma=60

# Demostración del método the lstrip()
print("[" + " tau ".lstrip() + "]") # [tau ]
print("www.cisco.com".lstrip("w.")) # ww.cisco.com
print("pythoninstitute.org".lstrip(".org")) # pythoninstitute

# Demostración del método replace()
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org")) # www.pythoninstitute.org
print("This is it!".replace("is", "are")) # This are it!
print("Apple juice".replace("juice", "")) # Apple
print("This is it!".replace("is", "are", 1)) # This are it!
print("This is it!".replace("is", "are", 2)) # This are it!

# Demostración del método rfind()
print("tau tau tau".rfind("ta")) # 8
print("tau tau tau".rfind("ta", 9)) # -1
print("tau tau tau".rfind("ta", 3, 9)) # 4

# Demostración del método rstrip()
print("[" + " upsilon ".rstrip() + "]") # [ upsilon]
print("cisco.com".rstrip(".com")) # cisco

# Demostración del método split()
print("phi       chi\npsi".split()) # ['phi', 'chi', 'psi']

# Demostración del método startswith()
print("omega".startswith("meg")) # False
print("omega".startswith("om")) # True

# Demostración del método strip() 
print("[" + "   aleph   ".strip() + "]") # [aleph]

# Demostración del método swapcase()
print("Yo sé que no sé nada.".swapcase()) # yO SÉ QUE NO SÉ NADA.

print()

# Demostración del método title()
print("Yo sé que no sé nada. Parte 1.".title()) # Yo Sé Que No Sé Nada. Parte 1.

print()

# Demostración del método upper()
print("Yo sé que no sé nada. Parte 2.".upper()) # YO SÉ QUE NO SÉ NADA. PARTE 2.

#Ejercicio
def misplit(string):
    lista = []
    tmp = ""
    for ch in string:
        if(ch == " "):
            if(tmp != ""):
                lista.append(tmp)
                tmp = ""
        else:
            tmp += ch
    if(tmp != ""):
        lista.append(tmp)
    return lista

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))

#Comparación de cadenas
print('alfa' == 'alfa') # True
print('alfa' != 'Alfa') # True
print('alfa' < 'alfabeto') # True
print('beta' > 'Beta') # True

print('10' == '010') # False
print('10' > '010') # True
print('10' > '8') # False
print('20' < '8') # True
print('20' < '80') # True

print('10' == 10) # False
print('10' != 10) # True
print('10' == 1) # False
print('10' != 1) #True
# print('10' > 10) error

# Demostración de la función sorted(), crea una nueva lista
firstGreek = ['omega', 'alfa', 'pi', 'gama']
firstGreek2 = sorted(firstGreek)

print(firstGreek) # ['omega', 'alfa', 'pi', 'gama']
print(firstGreek2) # ['alfa', 'gama', 'omega', 'pi']

# Demostración del método sort(), no crea una lista nueva modifica la original
secondGreek = ['omega', 'alfa', 'pi', 'gama']
print(secondGreek) # ['omega', 'alfa', 'pi', 'gama']

secondGreek.sort()
print(secondGreek) # ['alfa', 'gama', 'omega', 'pi']

#Convirtiendo numeros a cadenas
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf) # 13 1.3

#Convirtiendo cadenas a numeros
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt) # 14.3

#Ejercicio
digitos=['1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]
def printNumero(num):
	global digitos
	digs = str(num)
	lineas = [ '' for l in range(5) ]
	for d in digs:
		segs = [ [' ',' ',' '] for l in range(5) ]
		ptrn = digitos[ord(d) - ord('0')]
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for l in range(5):
			lineas[l] += ''.join(segs[l]) + ' '
	for l in lineas:
		print(l)

printNumero(int(input("Ingresa el número que deseas mostrar: ")))

# Cifrado César
text = input("Ingresa tu mensaje: ")
cifrado = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cifrado += chr(code)

print(cifrado)

# Cifrado César - descifrar un mensaje
cifrado = input('Ingresa tu criptograma: ')
text = ''
for char in cifrado:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

#Procesador de números
linea = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = linea.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")

# Validador IBAN

iban = input("Ingresa IBAN, por favor: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("Has introducido caracteres no válidos.")
elif len(iban) < 15:
    print("El IBAN ingresado es demasiado corto.")
elif len(iban) > 31:
    print("El IBAN ingresado es demasiado largo.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    ibann = int(iban2)
    if ibann % 97 == 1:
        print("El IBAN ingresado es válido.")
    else:
        print("El IBAN ingresado no es válido.")

#Cifrado Cesar con un valor de cambio variable
mensaje = input("Escribe tu mensaje a cifrar: ") #Pedimos el mensaje a cifrar
mensajeCifrado = '' #Inicializamos la variable que contendra el mensaje cifrado
while True:
    tamano = input("Ingresa el valor de cambio de 1 a 25: ") #Pedimos el valor de cambio
    if tamano.isdigit(): #Comprobamos si es un int
        tamano = int(tamano) #Convertimos a int
        if tamano > 0 and tamano < 26: #Comprobamos que es mayor que 0 y menor que 26
            break #Se ha cumplido la condicion y se sale del bucle
    print("Valor no válido!") #Si no se cumple la condicion se imprime esta mensaje y se vuelve a pedir el valor

for char in mensaje: #Creamos un bucle para recorrer el mensaje
    if not char.isalpha(): #Comprobamos si es una letra
        mensajeCifrado += char #Si no es una letra se añade a la variable que contendra el mensaje cifrado
        continue #Y se vuelve a ejecutar el bucle
    code = ord(char) + tamano #Obtenemos el valor ascii del caracter y le sumamos el valor de cambio
    if char.isupper(): #Revisa si el caracter es mayuscula
        if code > ord('Z'): #Comprobamos si el valor ascii es mayor que el valor ascii de Z
            code -= 26 #Si es mayor se resta 26 para que el valor ascii sea igual al de una letra mayuscula
    else: #Si no es mayuscula
        if code > ord('z'): #Comprobamos si el valor ascii es mayor que el valor ascii de z
            code -= 26 #Si es mayor se resta 26 para que el valor ascii sea igual al de una letra minuscula
    mensajeCifrado += chr(code) #Añadimos el caracter cifrado a la variable que contendra el mensaje cifrado

print(mensajeCifrado) #Imprimimos el mensaje cifrado

#Palíndromos
palabra = input("Ingresa una palabra: ") # Se le pide al usuario que ingrese una palabra
if palabra == '': # Revisamos si la cadena ingresada es vacía
    print("No es un palíndromo")
else: 
    palabra = palabra.lower() # Se convierte la palabra a minusculas
    palabra = palabra.replace(' ','') # Se elimina los espacios
    if palabra == palabra[::-1]: # Se compara la palabra ingresada con su inversa
        print("Es palíndromo")
    else:
        print("No es palíndromo")

#Anagramas
def acomodar(palabra):
    return sorted(palabra.lower().replace(" ", ""))

palabra = input("Ingrese una palabra: ") # Se le pide al usuario ingresar una palabra
anagrama = input("Ingrese una palabra anagrama: ") # Se le pide al usuario ingresar una palabra anagrama de la que se desea comparar
if len(palabra) != 0 or len(anagrama) != 0 or len(palabra) == len(anagrama): # Se comprueba que la longitud de ambas palabras sea la misma y que no estén vacías
    palabra = acomodar(palabra) # Se acomoda la palabra ingresada para que sea más fácil compararla
    anagrama = acomodar(anagrama) # Se acomoda la palabra ingresada para que sea más fácil compararla
    if palabra == anagrama:
        print("Es anagrama")
    else:
        print("No es anagrama")
else:
    print("No son anagramas") # Si no se cumplen las condiciones, se imprime que no son anagramas

#Digito de la vida
def formato(fecha): #Función que nos ayuda a formatear la fecha
    return fecha.replace(" ","")

digitoVida = 0 #Inicializamos la variable que contendrá el digito de la vida
fecha = input("Ingresa tu fecha de nacimiento en números: ") # Se le pide al usuario ingresar una fecha
fecha = formato(fecha) # Se formatea la fecha
if fecha.isdigit() and len(fecha) >= 6 and len(fecha) <= 8: # Se comprueba que la fecha sea correcta
    while True:
        for num in fecha: # Se recorre la fecha
            digitoVida += int(num) # Se suma el valor de cada dígito de la fecha
        if (len(str(digitoVida)) == 1): # Se revisa el que el digito de la vida sea un valor de 0 a 9
            print(digitoVida) # Se imprime el digito de la vida
            break;
        else: # Si no es un valor de 0 a 9
            fecha = str(digitoVida) # Se guarda como cadena el digito de la vida en fecha
            digitoVida = 0 # Se reinicializa la variable
else:
    print("Error, fecha no válida")

