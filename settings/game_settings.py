import sys
from core.model import TicTacToe
from settings.constants import *
import pygame as pg
sys.path.append('..')


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([WIN_SIZE] * 2)  # Ширина игрового окна = количество пикселей указанных в constants * 2
        self.clock = pg.time.Clock()
        self.tic_tac_toe = TicTacToe(self)  # После создания игрового дисплея, запускается сама игра.

    def new_game(self):
        self.tic_tac_toe = TicTacToe(self)

    def check_events(self):
        for event in pg.event.get():  # Проходим циклом по списку событий.
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:  # Если эвент равен нажатию клавиши и она пробел, то начинаем новую игру.
                if event.key == pg.K_SPACE:
                    self.new_game()

    def run(self):
        while True:
            self.tic_tac_toe.run()
            self.check_events()
            pg.display.update()  # Обновляет экран после действия, отображает изменения
            self.clock.tick(60)  # Сколько FPS. Тиков\частоты обновления экрана в секунду



