import pygame as pg
from support import import_folder


class OpponentElf(pg.sprite.Sprite):
    def __init__(self, groups: pg.sprite.Group, pos: tuple, speed: int):
        super().__init__(groups)

        self.frame_list = import_folder("res/red")
        self.pos = pg.Vector2(pos)

        self.current_frame = 0
        self.anim_speed = 0.05
        self.img = self.frame_list[self.current_frame]

        self.speed = speed

    def animate(self, dt):
        self.current_frame += self.anim_speed * self.speed * dt
        if self.current_frame > len(self.frame_list):
            self.current_frame = 0
        self.img = self.frame_list[int(self.current_frame)]

    def run(self, dt: float):
        self.pos.x += self.speed * dt

    def draw(self, screen: pg.Surface):
        screen.blit(self.img, self.pos)
