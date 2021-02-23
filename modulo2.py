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




















