# Reto #10: La API
#### Dificultad: Media | Publicación: 06/03/23 | Corrección: 13/03/23

## Enunciado

'''
/*
 * Llamar a una API es una de las tareas más comunes en programación.
 *
 * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
 * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
 *
 * Aquí tienes un listado de posibles APIs: 
 * https://github.com/public-apis/public-apis
 */
'''

import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=151"
response = requests.get (url)
json = response.json()
results = json["results"]
for index, pokemon in enumerate(json["results"]):
    pokemon_name = pokemon["name"]
    print(f"#{index + 1} {pokemon_name}")
