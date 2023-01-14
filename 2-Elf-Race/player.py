import pygame as pg
from support import import_folder


class PlayerElf:
    def __init__(self, pos: tuple):
        self.frame_list = import_folder("res/green")
        self.pos = pg.Vector2(pos)

        self.current_frame = 0
        self.anim_speed = 50
        self.img = self.frame_list[self.current_frame]

        self.speed = 0
        self.friction = 1

    def animate(self, dt):
        self.current_frame += self.anim_speed * self.speed * dt
        if self.current_frame > len(self.frame_list):
            self.current_frame = 0
        self.img = self.frame_list[int(self.current_frame)]

    def run(self, events, dt: float):
        for ev in events:
            if ev.type == pg.KEYDOWN and ev.key == pg.K_SPACE:
                self.speed += 0.1

        self.speed -= self.friction * dt
        if self.speed < 0:
            self.speed = 0

        self.pos.x += self.speed

    def draw(self, screen: pg.Surface):
        screen.blit(self.img, self.pos)
