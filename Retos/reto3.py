# Reto 3: EL GENERADOR DE CONTRASEÑAS 

'''
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */ 

'''
import random 

def generador (longitud = 8, mayusculas = False, numeros = False, simbolos = False):

    caracter = list(range(97, 123))
    if mayusculas:
        caracter += list(range(65, 91))

    if numeros:
        caracter += list(range(48, 58))

    if simbolos:
        caracter += list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97))  

    password = ""
    longitud = 8 if longitud < 8 else 16 if longitud > 16 else longitud
    while len(password) < longitud:
        password += chr(random.choice(caracter))
    return password




passwd = generador (12,True, True, False)
print (passwd)
