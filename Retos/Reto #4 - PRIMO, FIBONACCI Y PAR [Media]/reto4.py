# Reto 4: PRIMO, FIBONACCI Y PAR 

'''
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
'''

def prime (n:int):
    if n > 1:
        for i in range(2,n):
            if (n%i) == 0:
             return False
    else:
        return False

    return True



def fibonacci (n:int):
    count = 0
    n1 = 1
    n2 = 1
    while count < n+2:
        if n == n1:
            return True
        else:    
            nth = n1 + n2
            n1 = n2
            n2 = nth
        count += 1
    return False



def pair (n:int):
    if n % 2 == 0:
        return True
    else:
        return False



def pfp (num: int):
    # Inicializamos las variables booleanas
    #primo = False
    #fibo = False
    #par = False

    primo = prime(num)
    fibo = fibonacci(num)
    par = pair(num)        
    salida = f"{num} "


    # ifs separados para mejor comprension
    '''
    if primo:
        salida += "es primo"
    else:
        salida += "no es primo"

    if fibo:
        salida += ", es fibonacci"
    else:
        salida += ", no es fibonacci"

    if par:
        salida += " y es par"
    else:
        salida += " y es impar"
    '''

    # ifs en una sola linea en python
    # mas elegante 

    salida += "es primo" if primo else "no es primo"
    salida += ", es fibonacci" if fibo else ", no es fibonacci"
    salida += " y es par" if par else " y es impar"

    print (salida)


# ejecucion principal

pfp (0)
pfp (1)
pfp (2)
pfp (3)
pfp (4)
pfp (5)
pfp (7)
pfp (144)


