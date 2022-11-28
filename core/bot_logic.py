from random import randint
from settings.constants import INF


def bot_move(game_field, player):
    if game_field[1][1] == INF:
        game_field[1][1] = player
        return

    if game_field[0][2] == 0 and game_field[1][1] == 0 and game_field[2][2] == 1 and game_field[2][1] == 1:
        if game_field[2][0] == INF:
            game_field[2][0] = player
            return

    if game_field[0][0] == 0 and game_field[0][2] == 0:
        if game_field[0][1] == INF:
            game_field[0][1] = player
            return

    if game_field[0][2] == 0 and game_field[1][1] == 0:
        if game_field[2][1] == INF:
            game_field[2][1] = player
            return

    if game_field[1][0] == 0 and game_field[1][1] == 0 and game_field[1][2] == INF:
        game_field[1][2] = player
        return

    if game_field[0][1] == 1 or game_field[1][0] == 1 or game_field[1][2] == 1 or game_field[2][1] == 1:
        if game_field[0][0] == 0 and game_field[1][1] == 0:
            if game_field[2][2] == INF:
                game_field[2][2] = player
                return
        else:
            if game_field[0][0] == INF:
                game_field[0][0] = player
                return

        if game_field[2][2] == 0 and game_field[1][1] == 0:
            if game_field[0][0] == INF:
                game_field[0][0] = player
                return
            else:
                if game_field[2][2] == INF:
                    game_field[2][2] = player
                    return

        if game_field[0][2] == 0 and game_field[1][1] == 0:
            if game_field[2][0] == INF:
                game_field[2][0] = player
                return

        if game_field[2][0] == 0 and game_field[1][1] == 0:
            if game_field[0][2] == INF:
                game_field[0][2] = player
                return

        if game_field[0][1] == 0 and game_field[1][1] == 0:
            if game_field[1][2] == INF:
                game_field[1][2] = player
                return

        if game_field[1][2] == 0 and game_field[1][1] == 0:
            if game_field[1][0] == INF:
                game_field[1][0] = player
                return

        if game_field[0][1] == 0 and game_field[1][1] == 0:
            if game_field[2][1] == INF:
                game_field[2][1] = player
                return

        if game_field[2][1] == 0 and game_field[1][1] == 0:
            if game_field[0][1] == INF:
                game_field[0][1] = player
                return

    if game_field[0][0] == 1 or game_field[0][2] == 1 or game_field[2][0] == 1 or game_field[2][2] == 1:
        if game_field[0][0] == 1:
            if game_field[0][1] == 1 and game_field[0][2] == INF:
                game_field[0][2] = player
                return
            elif game_field[1][0] == 1 and game_field[2][0] == INF:
                game_field[2][0] = player
                return

        if game_field[0][2] == 1:
            if game_field[0][1] == 1 and game_field[0][0] == INF:
                game_field[0][0] = player
                return
            elif game_field[1][2] == 1 and game_field[2][2] == INF:
                game_field[2][2] = player
                return

        if game_field[2][0] == 1:
            if game_field[1][0] == 1 and game_field[0][0] == INF:
                game_field[0][0] = player
                return
            elif game_field[2][1] == 1 and game_field[2][2] == INF:
                game_field[2][2] = player
                return

        if game_field[0][0] == 1:
            if game_field[2][0] == 1 and game_field[1][0] == INF:
                game_field[1][0] = player
                return

        if game_field[1][2] == 0 and game_field[1][1] == 0:
            if game_field[1][0] == INF:
                game_field[1][0] = player
                return

        if game_field[0][0] == 1:
            if game_field[0][2] == 1 and game_field[0][1] == INF:
                game_field[0][1] = player
                return

        if game_field[0][2] == 1:
            if game_field[2][2] == 1 and game_field[1][2] == INF:
                game_field[1][2] = player
                return

        if game_field[2][2] == 1:
            if game_field[2][0] == 1 and game_field[2][1] == INF:
                game_field[2][1] = player
                return

        if game_field[0][2] == 1:
            if game_field[1][2] == INF:
                game_field[1][2] = player
                return
            elif game_field[0][1] == INF:
                game_field[0][1] = player
                return

        if game_field[2][0] == 1:
            if game_field[1][0] == INF:
                game_field[1][0] = player
                return
            elif game_field[2][1] == INF:
                game_field[2][1] = player
                return

        if game_field[0][0] == 1:
            if game_field[1][0] == INF:
                game_field[1][0] = player
                return
            elif game_field[0][1] == INF:
                game_field[0][1] = player
                return

        if game_field[0][0] == 1:
            if game_field[1][0] == INF:
                game_field[1][0] = player
                return
            elif game_field[0][1] == INF:
                game_field[0][1] = player
                return

    if game_field[0][2] == INF:
        game_field[0][2] = player
        return
    if game_field[2][0] == INF:
        game_field[2][0] = player
        return
    if game_field[2][2] == INF:
        game_field[2][2] = player
        return

    else:
        go_random = True
        while go_random:
            y, x = randint(0, 2), randint(0, 2)
            if game_field[y][x] == INF:
                game_field[y][x] = player
                go_random = False