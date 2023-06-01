# Reto #11: URL params
#### Dificultad: Fácil | Publicación: 13/03/23 | Corrección: 20/03/23

## Enunciado

'''
/*
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 *
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
 * los parámetros serían ["2023", "0"]
 */
'''

def parametros (url: str)-> list:
    dividir = url.split("&")
    lista = list()
    for i in dividir:
        if len(i.split("=")) == 2 and  (i.split("=")[1]) != "":
            lista.append(i.split("=")[1])
    return lista

url = "https://retosdeprogramacion.com?year=2023&challenge=0&hola=1234&jj=1024"
#url =  "https://retosdeprogramacion.com?year=2023&challenge=0"
#url = "https://elpais.com"
print (parametros (url))

'''
# Solución con una expresión regular

regex = r"=([a-zA-Z0-9._%-]+)"
params = re.findall(regex, url)
print(params)


'''
