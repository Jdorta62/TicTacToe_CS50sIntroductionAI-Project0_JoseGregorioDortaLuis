"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    empty_count = sum(row.count(EMPTY) for row in board)
    return O if empty_count % 2 == 0 else X
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Acción inválida: la posición no está disponible en el tablero.")
    current_player = player(board)
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Lista de todas las combinaciones posibles de victoria (filas, columnas y diagonales)
    winning_combinations = [
        # Filas
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Columnas
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonales
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    # Verifica si alguna combinación ganadora tiene el mismo jugador en todas las posiciones
    for combination in winning_combinations:
        first_cell = board[combination[0][0]][combination[0][1]]
        if first_cell is not None and all(board[i][j] == first_cell for i, j in combination):
            return first_cell

    # Si no hay ganador, retorna None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or sum(row.count(EMPTY) for row in board) == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    if winner_player == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None  # No hay acción posible en un tablero terminal

    current_player = player(board)

    if current_player == X:
        # Maximizar para X
        max_utility = -math.inf
        optimal_action = None
        for action in actions(board):
            action_utility = min_value(result(board, action))
            if action_utility > max_utility:
                max_utility = action_utility
                optimal_action = action
        return optimal_action
    else:
        # Minimizar para O
        min_utility = math.inf
        optimal_action = None
        for action in actions(board):
            action_utility = max_value(result(board, action))
            if action_utility < min_utility:
                min_utility = action_utility
                optimal_action = action
        return optimal_action

def max_value(board):
    # Caso base: si el juego terminó, retorna la utilidad del tablero
    if terminal(board):
        return utility(board)
    max_utility = -math.inf
    for action in actions(board):
        # Calcula el valor mínimo que el oponente puede obtener en el siguiente turno
        max_utility = max(max_utility, min_value(result(board, action)))
    return max_utility

def min_value(board):
    # Caso base: si el juego terminó, retorna la utilidad del tablero
    if terminal(board):
        return utility(board)
    min_utility = math.inf
    for action in actions(board):
        # Calcula el valor máximo que el oponente puede obtener en el siguiente turno
        min_utility = min(min_utility, max_value(result(board, action)))
    return min_utility
