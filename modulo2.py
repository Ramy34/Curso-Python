#Códigos y ejercicios del Modulo 2
#Ejemplo
print("¡Hola, Mundo!")

#Ejercicio: Aprender a utilizar la función print()
print("Ramsés")
#print(¡Hola, Mundo!)
#print "¡Hola, Mundo!"
print('¡Hola, Mundo!')

#Ejecutando dos print en un mismo código
print("La Witsi Witsi Araña subió a su telaraña.")
print("Vino la lluvia y se la llevó.")

#Observando que ocurre con un print vacío
print("La Witsi Witsi Araña subió a su telaraña.")
print()    
print("Vino la lluvia y se la llevó.")

#Otras formas de hacer un salto de línea
print("La Witsi Witsi Araña\nsubió a su telaraña.\n")
print()    
print("Vino la lluvia\ny se la llevó.")

#Observando que ocurre con la función print con más de 1 argumento
print("La Witsi Witsi Arañar" , "subió" , "a su telaraña.")

#Observando la manera posicional de los argumentos
print("Mi nombre es", "Python.")
print("Monty Python.")

#Print() con argumentos de palabras clave
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")

#Argumento de palabra clave end vacía
print("Mi nombre es ", end="")
print("Monty Python.")

#Argumento de palabra clave sep
print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

#Mezclando argumentos de palabras claves
print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

#Ejercicio: Familiarizarte con las palabras claves
print("Fundamentos","Programación","en",sep="***",end="...")
print("Python")

#Ejercicio: Flecha en una sola línea
print("    *", "   * *", "  *   *", " *     *", "***   ***", "  *   *", "  *   *", "  *****",sep="\n")

#Palabras claves de la función print()
#end -> Modifica la acción que realiza al terminal la función, por defecto está en \n
#sep -> Modifica la unión cuando de mandan 2 o mas cadenas en la función, por defecto está en espacio

#Literales
print("2")
print(2)

#Enteros: Separaciones, octales y hexadecimales
print(11_111_111)
print(0o123)
print(0x123)

#Codificando cadenas
print("I'm Monty Python")
print('I\'m Monty Python')

#Probando los booleanos
print(True > False)
print(True < False)

#Ejercicio: Codificación de caracteres
print('"Estoy"','""aprendiendo""','"""python"""',sep="\n")

#Python como calculadora
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 / 2)

#Exponentes
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#Multiplicación
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

#División
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

#División entera
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(6 // 4)
print(6. // 4)

print(-6 // 4)
print(6. // -4)

#Residuo (Módulo)
print(14 % 4)
print(12 % 4.5)

#Suma
print(-4 + 4)
print(-4. + 8)

#Resta
print(-4 - 4)
print(4. - 8)

#Negación
print(-1.1)

#Identidad
print(+2)

#Operadores y enlaces
#Izquierda
print(9 % 6 % 2)

#Derecha
print(2 ** 2 ** 3)

#Variables - Creación de una variable
var = 1
print(var)

var = 1
balance_cuenta = 1000.0
nombreCliente = 'John Doe'
print(var, balance_cuenta, nombreCliente)

#Reasignar el valor de una variable
var = 1
print(var)
var = var + 1
print(var)

#Pitágoras
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

#Familiarizarse con las variables
juan = 3
maria = 5
adan = 6
mensaje = "Número Total de Manzanas:"
totalManzanas = juan + maria + adan

print(juan, maria, adan, sep=",")
print(totalManzanas)
print(mensaje, totalManzanas)

#Operadores abreviados
x = oveja = 1
x *= 2
oveja += 1

#Conversión de distancias
kilometros = 12.25
millas = 7.38

millas_a_kilometros = millas * 1.61
kilometros_a_millas = kilometros / 1.61

print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")

#Operadores y expresiones
# codifica aquí tus datos de prueba.
x = float(-1)
# escribe tu código aquí.
y = (3 * x ** 3) - (2 * x ** 2) + (3 * x) - 1
print("y =", y)

#Cometarios

#Este programa fue escrito hace dos días
#Este programa calcula los segundos en cierto número de horas determinadas 

horas = 2
segundosHora = 3600

print("Horas: ", horas) #imprime el numero de horas
print("Segundos en horas: ", horas * segundosHora) # se imprime el numero de segundos en determinado numero de horas

print("Adiós")

#Input sin argumentos
print("Dime algo...")
algo = input()
print("Mmm...", algo, "...¿en serio?")

#Input con argumentos
algo = input("Dime algo...")
print("Mmm...", algo, "...¿En serio?")

#Input con casteo
algo = float(input("Inserta un número: "))
resultado = algo ** 2.0
print(algo, "al cuadrado es", resultado)

cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto "))
print("La longitud de la hipotenusa es: ", (cateto_a**2 + cateto_b**2) ** .5)

#Concatenación
nom = input("¿Me puedes dar tu nombre por favor? ")
ape = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + nom + " " + ape + ".")

#Replica
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#str()
cateto_a = float(input("Ingresa la longitud del primer cateto: "))
cateto_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es: " + str((cateto_a**2 + cateto_b**2) ** .5))

#Uso de las 4 operaciones básicas
numero1 = float(input("Ingrea el primer valor: "))
numero2 = float(input("Ingrea el segundo valor: "))

print("El resultado de la suma es: " + str(numero1 + numero2))
print("El resultado de la resta es: " + str(numero1 - numero2))
print("El resultado de la multiplicación es: " + str(numero1 * numero2))
print("El resultado de la división es: " + str(numero1 / numero2))

print("\n¡Eso es todo, amigos!")

#Precedencia y asociatividad
x = float(input("Ingresa el valor para x: "))
y = 1 / (x + (1 / (x + (1 / (x + (1 / x))))))
print("y =", y)

#Fenómenos del día a día en términos de un lenguaje de programación
hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

minFinal = (min + dura) % 60 #Obtenemos el minuto en el que termina el evento
horasExtras = (min + dura) // 60 #Obtenemos el desborde de las horas
horaFinal = (hora + horasExtras) % 24 #Obtenemos la hora final del evento

print("El evento inicia " + str(hora) + ":" + str(min))
print("El evento termina " + str(horaFinal) + ":" + str(minFinal))
