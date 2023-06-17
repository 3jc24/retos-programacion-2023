# Reto 6: Piedra, Papel, Tijera, Lagarto, Spock

'''
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */ 
'''

# Matriz o diccionario de jugadas con las reglas
# cada indice tiene de elementos a quien gana
rules = {"🗿":["✂️ ", "🦎"],
         "📄":["🗿", "🖖"],
         "✂️,":["📄", "🦎"],
         "🦎":["🖖", "📄"],
         "🖖":["🗿", "✂️,"]
    }


def game (jugadas):
    #contador de partidas ganadas
    player_one = 0
    player_two = 0

    for jugada in jugadas:
        player_one_jugado = jugada[0]
        player_two_jugado = jugada[1]
        if player_one_jugado != player_two_jugado:
            if player_two_jugado in rules[player_one_jugado]:
                player_one += 1
            else: 
                player_two += 1

    print (player_one,player_two)
    return "Tie" if player_one == player_two else "Player 1" if player_one > player_two else "Player 2"



# flujo principal del programa
print (game ([("🗿","✂️ "), ("✂️,","🗿"), ("📄","✂️ "), ("🗿","✂️ ")]))
print (game ([("🗿","✂️ ")]))
print (game ([("🗿","✂️ "), ("✂️,","🗿"), ("📄","✂️ ")]))
