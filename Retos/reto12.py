# Reto #12: Viernes 13
#### Dificultad: Fácil | Publicación: 20/03/23 | Corrección: 27/03/23

## Enunciado

'''
/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
'''

import datetime, time
def viernes_13 (ano:int, mes:int)-> bool:
    date = datetime.date(ano,mes,13)
    if date.weekday() == 4:
        return True
    return False
    # lo mismo en 1 sola linea:
    # return date.weekday() == 4


print (viernes_13 (2023,10))
