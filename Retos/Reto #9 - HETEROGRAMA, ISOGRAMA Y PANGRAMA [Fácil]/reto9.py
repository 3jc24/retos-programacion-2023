# Reto #9: Heterograma, isograma y pangrama
#### Dificultad: Fácil | Publicación: 27/02/23 | Corrección: 06/03/23

## Enunciado

'''
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
'''

# creamos una funcion para contar el numero de veces que aparece cada letra en la frase
# la usaremos en las 3 funciones pedidas
def cuenta_letras (frase: str) -> dict [str, int]:
    cuenta = dict()
    for caracter in frase:
        if caracter in cuenta.keys():
            cuenta[caracter] += 1
        else:
            cuenta[caracter] = 1
    #quitamos el espacio
    del (cuenta[" "])
    return cuenta

# funcion para imprimir el diccionario con las letras y sus apariciones
def imprimir (cuenta: dict[str, int]):
    for i in cuenta:
        print (f"la letra {i} aparece {cuenta[i]} veces")
    print ("Letras Diferentes: ", len(cuenta.keys()))


# Un heterograma es una palabra o frase que no contiene ninguna letra repetida.
def heterograma (frase: str) -> bool:
    diccionario = cuenta_letras(frase)
    for numero in diccionario.values():
        if numero != 1:
            return False
    return True


# Un isograma es una palabra o frase en la que cada letra aparece el mismo número de veces.
def isograma (frase: str) -> bool:
    diccionario = cuenta_letras(frase)
    order = 0
    for counter in diccionario.values():
        if order == 0:
            order = counter
        if order is not counter:
            return False
    return True



# la frase mínima que utiliza todas las letras del alfabeto de un determinado idioma
# Ejemplo:
# "La cigüeña tocaba el saxofón detrás del palenque de paja"
# "Fabio me exige, sin tapujos, que añada cerveza al whisky".
# el diccionario castellano tiene 27 letras
def pangrama (frase: str) -> bool:
    diccionario = cuenta_letras (frase)
    if  len(diccionario.keys()) != 27 :
        return False
    else:
        return True
    


# flujo principal donde llamamos a las 3 funciones pedidas
# como prueba llamamos a otras funciones creadas
if __name__ == '__main__':
    #frase = "qwertyuiopqwertyuiop"
    frase = "Fabio me exige sin tapujos que añada cerveza al whisky"
    imprimir(cuenta_letras (frase))
    print ("Heterograma: ", heterograma(frase))
    print ("Isograma: ", isograma (frase))
    print("Pangrama: ", pangrama (frase))
