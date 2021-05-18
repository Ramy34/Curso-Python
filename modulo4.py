#Códigos y ejercicios del Modulo 4
#Funciones
def mensaje():
    print("Ingresa un valor: ")

print("Se comienza aquí.")
mensaje()
print("Se termina aquí.")

#Funciones con parámetros
def mensaje(numero):
    print("Ingresa un número:", numero)

mensaje(1)

def mensaje(que, numero):
    print("Ingresa", que, "número", numero)

mensaje("teléfono", 11)
mensaje("precio", 5)
mensaje("número", "número")

#Funciones con argumentos por posición
def presentar(primerNombre, segundoNombre):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar("Luke", "Skywalker")
presentar("Jesse", "Quick")
presentar("Clark", "Kent")

#Funciones con argumentos en clave
def presentar (primerNombre, segundoNombre):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar(primerNombre = "James", segundoNombre = "Bond")
presentar(segundoNombre = "Skywalker", primerNombre = "Luke")

#Funciones con argumentos mixtos
def suma(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

suma(3, c = 1, b = 2)

#Funciones con argumentos opcionales
def presentar(primerNombre, segundoNombre="Smith"):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar("Jorge", "Pérez")
presentar("Enrique")
presentar (primerNombre="Guillermo")

#¿Cuál es la salida del siguiente código?

def intro(a="James Bond", b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro() #Mi nombre es Bond. James Bond.

#¿Cuál es la salida del siguiente código?

def intro(a="James Bond", b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro(b="Sergio López") #Mi nombre es Sergio López. James Bond.

#¿Cuál es la salida del siguiente fragmento de código?

def intro(a, b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro("Susan") #Mi nombre es Bond. Susan.

#Funciones con retorno
def funcion_aburrida():
    return 123

x = funcion_aburrida()

print ("La funcion_aburrida ha devuelto su resultado. Es: ", x)

#Valor None
valor = None
if valor == None:
    print("Lo siento, no tienes ningún valor") 

#Funciones y None
def strangeFunction(n):
    if(n % 2 == 0):
        return True
        
print(strangeFunction(2)) #True
print(strangeFunction(1)) #None

#Funciones y listas como argumentos
def sumaDeLista(lst):
    sum = 0
    
    for elem in lst:
        sum += elem
    
    return sum
    
print(sumaDeLista([5, 4, 3])) #12

#Funciones y listas como regreso
def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(5))

#Ejercicio
def isYearLeap(año):
    if año >= 1582:
        if (año % 4) != 0:
            estado = False
        else:
            if (año % 100) != 0:
                estado = True
            else:
                if (año % 400) != 0:
                    estado = False
                else:
                    estado = True
    else:
        print("No dentro del período del calendario gregoriano")
    return estado
    

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")

#Ejercicio
def isYearLeap(año):
    if año >= 1582:
        if (año % 4) != 0:
            estado = False
        else:
            if (año % 100) != 0:
                estado = True
            else:
                if (año % 400) != 0:
                    estado = False
                else:
                    estado = True
    else:
        print("No dentro del período del calendario gregoriano")
    return estado

def daysInMonth(year, month):
    meses31 = [1,3,5,7,8,10,12]
    meses30 = [4,6,9,11]
    
    #Identificar meses con 31
    if month in meses31:
        dias = 31
    elif month in meses30:
        dias = 30
    else:
        if isYearLeap(year):
            dias = 29
        else:
            dias = 28
    return dias

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")

#Ejercicio
def isYearLeap(año):
    if año >= 1582:
        if (año % 4) != 0:
            estado = False
        else:
            if (año % 100) != 0:
                estado = True
            else:
                if (año % 400) != 0:
                    estado = False
                else:
                    estado = True
    else:
        print("No dentro del período del calendario gregoriano")
    return estado

def daysInMonth(year, month):
    meses31 = [1,3,5,7,8,10,12]
    meses30 = [4,6,9,11]
    
    #Identificar meses con 31
    if month in meses31:
        dias = 31
    elif month in meses30:
        dias = 30
    else:
        if isYearLeap(year):
            dias = 29
        else:
            dias = 28
    return dias

def dayOfYear(year, month, day):
    diasActuales = day
    for i in range(month-1):
        diasActuales += daysInMonth(year, i+1)
    return diasActuales

print(dayOfYear(2000, 12, 31))

#Ejercicio
def isPrime(num):
    if num == 2 or num == 3:
        estado = True
    else:
        if (num % 2) == 0 or (num % 3) == 0:
            estado = False
        else:
            estado = True
    return estado

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()

# Convertidor de consumo de combustible
def l100kmtompg(liters):
    galon = liters / 3.785411784
    millas = 100000 / 1609.344
    total = (millas / galon)
    return total

def mpgtol100km(miles):
    metros = miles * 1609.344
    kmetros = metros * 0.001
    litros = 3.785411784
    total = (litros / kmetros) * 100
    return total
    
print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))

#¿Cuál es la salida del siguiente fragmento de código?

def hola():
    return
    print("¡Hola!")

hola() #La salida es None

#¿Cuál es la salida del siguiente fragmento de código?
def isInt(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False 
    
print(isInt(5)) #True
print(isInt(5.0)) #False
print(isInt("5")) #None

#¿Cuál es la salida del siguiente fragmento de código?
def evenNumLst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(evenNumLst(11)) #[0,2,4,6,8,10]

#¿Cuál es la salida del siguiente fragmento de código?
def listUpdater(lst):
    updList = []
    for elem in lst:
        elem **= 2
        updList.append(elem)
    return updList

l = [1, 2, 3, 4, 5]
print(listUpdater(l)) #[1, 4, 9, 16, 25]

#Alcances de las variables 
def miFuncion():
    print("¿Conozco a la variable?", var) #1

var = 1
miFuncion()
print(var) #1

#Utilizando global
def miFuncion():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var) #2

var = 1
miFuncion()
print(var) #2

#Alcances con listas como parámetros
def miFuncion(miLista1):
    print(miLista1) #[2, 3]
    del miLista1[0]

miLista2 = [2, 3]
miFuncion(miLista2)
print(miLista2) #[3]

#¿Cuál es la salida del siguiente fragmento de código?
a = 1

def fun():
    a = 2
    print(a) #2

fun()
print(a) #1

#¿Cuál es la salida del siguiente fragmento de código?
a = 1

def fun():
    global a
    a = 2
    print(a) #2

fun()
a = 3
print(a) #3

#¿Cuál es la salida del siguiente fragmento de código?
a = 1

def fun():
    global a
    a = 2
    print(a) #2

a = 3
fun()
print(a) #2

