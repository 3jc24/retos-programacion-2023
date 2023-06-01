# Reto #2: EL PARTIDO DE TENIS

'''
/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

'''

from enum import Enum 

class Player(Enum):
    P1 = 1
    P2 = 2

def tennis (points: list):
    game = ["love", "15", "30", "40"]
    player1_points = 0
    player2_points = 0
    finished = False

    for player in points:
        error = finished

        if player == Player.P1:
            player1_points += 1
        else: 0

        if player == Player.P2:
            player2_points += 1
        else: 0

        if (player1_points >= 3 and player2_points >= 3):
            if not finished and abs(player1_points - player2_points) <= 1:
                if (player1_points == player2_points): 
                    print ("Deuce")
                elif player1_points > player2_points:
                    print ("Ventaja P1")
                else:
                    print ("Ventaja P2")
            else:
                finished = True
        else:
            if (player1_points < 4 or player2_points < 4):
                print (f"{game[player1_points]} - {game[player2_points]}")
            else: 
                finished = True

    if error:
        print ("Los puntos no son corretos")
    elif player1_points > player2_points:
        print ("Ha ganado el P1 ")
    else:
        print ("Ha ganado el P2")


tennis ([Player.P2,Player.P2,Player.P2,Player.P1,Player.P1,Player.P1,Player.P1,Player.P1])
