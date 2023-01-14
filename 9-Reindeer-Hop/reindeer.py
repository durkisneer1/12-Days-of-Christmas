import pygame as pg
from constants import *


class Reindeer:
    def __init__(self, frame_list, spawn_type, ground_rect):
        self.frame_list = frame_list

        self.current_frame = 0
        self.img = self.frame_list[self.current_frame]
        self.rect = self.img.get_rect()
        self.mask = pg.mask.from_surface(self.img)

        if spawn_type == "ground":
            y_pos = ground_rect.top
        elif spawn_type == "air":
            y_pos = WIN_HEIGHT / 2
        self.pos = pg.Vector2(WIN_WIDTH, y_pos)  # NOQA

        self.speed = 20

    def animate(self, dt):
        self.current_frame += dt
        try:
            self.img = self.frame_list[int(self.current_frame)]
            self.mask = pg.mask.from_surface(self.img)
        except IndexError:
            self.current_frame = 0

    def move(self, dt):
        self.rect.bottomleft = self.pos
        self.pos.x -= self.speed * dt

    def draw(self, screen):
        screen.blit(self.img, self.rect)