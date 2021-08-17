#Todo esto se ejecuta en el script main.py
"""modulo.py - un ejemplo de modulos de python"""
#contador = 0
#if __name__== "__main__":
#    print("Yo prefiero ser un módulo")
#else:
#    print("Me gusta ser un módulo")

__counter = 0
def sum1(lista):
    global __counter
    __counter += 1
    sum = 0
    for el in lista:
        sum += el
    return sum

def prod1(lista):
    global __counter
    __counter += 1
    prod = 1
    for el in lista:
        prod *= el
    return prod

if __name__ == "__main__":
    print("Yo prefiero ser un módulo, pero te puedo ayudar con tus pruebas")
    l = [i + 1 for i in range(5)]
    print(sum1(l) == 15)
    print(prod1(l) == 120)