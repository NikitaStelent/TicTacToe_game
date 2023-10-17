from random import randint
from settings.constants import INF


def bot_move(game_field, player):
    # Проверяем, есть ли у бота выигрышная комбинация
    for row in range(3):
        for col in range(3):
            if game_field[row][col] == INF:
                game_field[row][col] = player
                if bot_wins(game_field, player):
                    return
                game_field[row][col] = INF

    # Проверяем, может ли бот заблокировать выигрыш соперника
    for row in range(3):
        for col in range(3):
            if game_field[row][col] == INF:
                game_field[row][col] = player
                if bot_wins(game_field, not player):
                    return
                game_field[row][col] = INF

    # Если у бота нет выигрышной комбинации и он не может заблокировать выигрыш соперника,
    # бот делает случайный ход
    y, x = randint(0, 2), randint(0, 2)
    while game_field[y][x] != INF:
        y, x = randint(0, 2), randint(0, 2)

    game_field[y][x] = player


def bot_wins(game_field, player):
    """ Проверяет, выиграл ли игрок с заданным знаком. """

    for i in range(3):
        if game_field[i][0] == game_field[i][1] == game_field[i][2] == player:
            return True

    for j in range(3):
        if game_field[0][j] == game_field[1][j] == game_field[2][j] == player:
            return True

    if game_field[0][0] == game_field[1][1] == game_field[2][2] == player:
        return True

    if game_field[0][2] == game_field[1][1] == game_field[2][0] == player:
        return True

    return False
