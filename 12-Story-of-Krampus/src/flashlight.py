import pygame as pg


class Flashlight:
    def __init__(self):
        self.pos = pg.Vector2()
        self.active = False

    def update(self, mouse_pressed):
        self.active = False
        if mouse_pressed[0]:
            self.pos = pg.mouse.get_pos()
            self.active = True

    def draw(self, screen):
        if self.active:
            pg.draw.circle(screen, (0, 0, 0, 120), self.pos, 14)
            for i in range(13, 9, -1):
                alpha = (i - 4) * 10
                pg.draw.circle(screen, (0, 0, 0, alpha), self.pos, i)
            pg.draw.circle(screen, (0, 0, 0, 50), self.pos, 5)
