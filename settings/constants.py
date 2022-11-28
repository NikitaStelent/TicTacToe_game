import pygame as pg

WIN_SIZE = 900
CELL_SIZE = WIN_SIZE // 3
INF = float('inf')
vec2 = pg.math.Vector2  # Вектор для 2D
CELL_CENTER = vec2(CELL_SIZE / 2)

# Индексы для win condition
CONDITION_INDICES = [[(0, 0), (0, 1), (0, 2)],
                     [(1, 0), (1, 1), (1, 2)],
                     [(2, 0), (2, 1), (2, 2)],
                     [(0, 0), (1, 0), (2, 0)],
                     [(0, 1), (1, 1), (2, 1)],
                     [(0, 2), (1, 2), (2, 2)],
                     [(0, 0), (1, 1), (2, 2)],
                     [(0, 2), (1, 1), (2, 0)]]


