import pygame as pg

from .filter import random_static
from .scene import Scene
from .settings import WIN_WIDTH, WIN_HEIGHT

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pg.SCALED | pg.FULLSCREEN)
pg.display.set_caption("The Story of Krampus")
clock = pg.time.Clock()
font = pg.font.Font("assets/font/vhs.ttf", 28)

title_lines = [["THE STORY", "white", -25],
              ["OF", "white", 0],
              ["KRAMPUS", "red", 25]]
text_list = []
for line in title_lines:
    title_surf = font.render(line[0], True, line[1])
    title_rect = title_surf.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2 + line[2]))
    text_list.append([title_surf, title_rect])

scene = Scene()


def get_active(events):
    for ev in events:
        if ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE:
            return False
    return True


def main():
    menu = True
    run = True
    while run:
        dt = clock.tick(30) / 1000
        events = pg.event.get()
        for ev in events:
            if ev.type == pg.KEYDOWN and ev.key == pg.K_RETURN:
                menu = False
        run = get_active(events)
        if scene.dead:
            run = False

        screen.fill((10, 10, 10))

        if menu:
            for txt in text_list:
                screen.blit(txt[0], txt[1])
        else:
            scene.update(dt)
            scene.draw(screen)

        screen.blit(random_static(), (0, 0))
        pg.display.flip()
