import pygame as pg


class SnowBall:
    def __init__(self, spawn_pos, direction):
        self.direction = direction
        self.pos = pg.Vector2(spawn_pos)
        self.rect = pg.Rect(self.pos, (10, 10))
        self.speed = 15

    def move(self, dt):
        if self.direction == 1:
            self.pos.x += self.speed * dt
        elif self.direction == 2:
            self.pos.x -= self.speed * dt

    def draw(self, screen):
        pg.draw.circle(screen, "black", self.pos, 6)
        self.rect = pg.draw.circle(screen, "white", self.pos, 5)
