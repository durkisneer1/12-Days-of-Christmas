import pygame as pg
import numpy as np
import cv2

from .settings import WIN_WIDTH, WIN_HEIGHT


def random_static() -> pg.Surface:
    arr = np.random.randint(0, 255, (WIN_WIDTH, WIN_HEIGHT, 3)).astype(np.uint8)
    grayscale = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)  # NOQA
    arr[:] = np.reshape(grayscale, grayscale.shape + (1,))

    surf = pg.surfarray.make_surface(arr)
    surf.set_alpha(15)

    return surf
