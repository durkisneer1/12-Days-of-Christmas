import pygame as pg

from .filter import random_static
from .scene import Scene
from .settings import WIN_WIDTH, WIN_HEIGHT

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pg.SCALED | pg.FULLSCREEN)
pg.display.set_caption("The Story of Krampus")
clock = pg.time.Clock()
font = pg.font.Font("assets/font/vhs.ttf", 28)

title1_surf = font.render("THE STORY", True, "white")
title1_rect = title1_surf.get_rect(
    center=(WIN_WIDTH / 2, WIN_HEIGHT / 2 - title1_surf.get_height())
)
title2_surf = font.render("OF", True, "white")
title2_rect = title2_surf.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))
title3_surf = font.render("KRAMPUS", True, "red")
title3_rect = title3_surf.get_rect(
    center=(WIN_WIDTH / 2, WIN_HEIGHT / 2 + title3_surf.get_height())
)

scene = Scene()


def get_active(events):
    for ev in events:
        if ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE:
            return False
    return True


def show_title():
    screen.blit(title1_surf, title1_rect)
    screen.blit(title2_surf, title2_rect)
    screen.blit(title3_surf, title3_rect)


def main():
    menu = True
    run = True
    while run:
        dt = clock.tick(30) / 1000
        events = pg.event.get()
        for ev in events:
            if ev.type == pg.MOUSEBUTTONDOWN and ev.button == 1:
                menu = False
        run = get_active(events)
        if scene.dead:
            run = False

        screen.fill((10, 10, 10))

        if menu:
            show_title()
        else:
            scene.update(dt)
            scene.draw(screen)

        screen.blit(random_static(), (0, 0))
        pg.display.flip()
