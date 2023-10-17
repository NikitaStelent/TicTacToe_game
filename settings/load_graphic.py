import pygame as pg


def get_image(path, res):
    """Получаем исходные изображения.
    Растягиваем их до размера 'res' """
    img = pg.image.load(path)
    return pg.transform.smoothscale(img, res)
