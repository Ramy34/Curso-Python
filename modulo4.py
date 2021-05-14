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