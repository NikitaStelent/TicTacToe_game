from random import randint
from core import views
from settings.constants import *
from settings.load_graphic import get_image
from core.bot_logic import bot_move


class TicTacToe:
    def __init__(self, game):
        self.game = game
        self.field_image = get_image(path='resources/field.png', res=[WIN_SIZE] * 2)
        self.O_image = get_image(path='resources/o.png', res=[CELL_SIZE] * 2)
        self.X_image = get_image(path='resources/x.png', res=[CELL_SIZE] * 2)

        self.game_field = [[INF for _ in range(3)] for _ in range(3)]  # Генерация и заполнение игрового поля 3 x 3
        self.player = randint(0, 1)

        self.win_condition_indices = CONDITION_INDICES
        self.winner = None

        self.game_steps = 0  # Считаем сколько ходов было сделано. Если 9, то это ничья.
        self.font = pg.font.SysFont('Consolas', CELL_SIZE // 5, True)

    def check_winner(self):
        """Функция проверки победителя"""
        for line_indices in self.win_condition_indices:
            sum_line = sum([self.game_field[i][j] for i, j in line_indices])
            if sum_line in {0, 3}:
                self.winner = ['Player', 'BOT'][sum_line == 0]
                self.winner_line = [vec2(line_indices[0][::-1]) * CELL_SIZE + CELL_CENTER,
                                    # Координаты для корректной отрисовки линии, при победе.
                                    vec2(line_indices[2][::-1]) * CELL_SIZE + CELL_CENTER]

    def run_game_process(self):
        if self.player == 1:  # Если ходит игрок
            current_cell = vec2(pg.mouse.get_pos()) // CELL_SIZE
            col, row = map(int, current_cell)
            left_click = pg.mouse.get_pressed()[0]  # С помощью get_pos() в current_cell получаем позицию курсора и
            # сохраняем в переменную, когда кликнута

            if left_click and self.game_field[row][col] == INF and not self.winner:  # Если кликаем в ячейку по
                # координатам row col, там пусто и еще не определен победитель:
                self.game_field[row][col] = self.player  # то ставим наш знак
                self.player = not self.player
                self.game_steps += 1
                self.check_winner()

        else:  # Если ходит бот
            bot_move(self.game_field, self.player)
            self.player = not self.player
            self.game_steps += 1
            self.check_winner()

    def draw_objects(self):
        """Рисуем X или O в определенной ячейке, по координатам x, y.
        Если она не пустая, т.е мы поставили знак.
        Умножаем на CELL SIZE для растяжения на весь размер ячейки"""
        for y, row in enumerate(self.game_field):
            for x, obj in enumerate(row):
                if obj != INF:  # С помощью enumerate ищем координаты ячейки.
                    self.game.screen.blit(self.X_image if obj else self.O_image, vec2(x, y) * CELL_SIZE)

    def draw_winner(self):
        """Отображает победителя, если удовлетворен win condition"""
        if self.winner:
            pg.draw.line(self.game.screen, 'cyan', *self.winner_line,
                         CELL_SIZE // 8)  # Рисует линию на комбинации победителя
            label = self.font.render(f'"{self.winner}" wins!', True, 'white', 'black')
            self.game.screen.blit(label, (WIN_SIZE // 2 - label.get_width() // 2, WIN_SIZE // 4))
        elif self.game_steps == 9:
            label = self.font.render(views.show_tie()[:11], True, 'white', 'black')
            self.game.screen.blit(label, (WIN_SIZE // 2 - label.get_width() // 2, WIN_SIZE // 8))

    def draw(self):
        """Главная функция рисования, вызывающая остальные"""
        self.game.screen.blit(self.field_image, (0, 0))
        self.draw_objects()
        self.draw_winner()

    def print_caption(self):
        pg.display.set_caption(views.show_turn(self.player))
        if self.winner:
            pg.display.set_caption(views.show_winner(self.winner))
        elif self.game_steps == 9:
            pg.display.set_caption(views.show_tie())

    def run(self):
        self.print_caption()
        self.draw()
        self.run_game_process()
