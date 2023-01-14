import pygame as pg
from random import randint
from constants import *
from player import Santa
from chimney import Chimney

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Flappy Deer")
clock = pg.time.Clock()

wallpaper = pg.image.load("res/wallpaper.png")
wallpaper = pg.transform.scale(wallpaper, (WIN_WIDTH, WIN_HEIGHT)).convert()
chimney_img = pg.image.load("res/chimney.png").convert_alpha()

santa = Santa()

chimney_group = pg.sprite.Group()
spawn_chimney = pg.USEREVENT + 1
pg.time.set_timer(spawn_chimney, 2000)


def main():
    random_height = randint(100, WIN_HEIGHT - 300)
    Chimney(chimney_group, True, random_height, chimney_img)
    Chimney(chimney_group, False, random_height, chimney_img)

    run = True
    while run:
        dt = clock.tick() / 100
        events = pg.event.get()

        for ev in events:
            if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE):
                run = False
            if ev.type == spawn_chimney:
                random_height = randint(100, WIN_HEIGHT - 300)
                Chimney(chimney_group, True, random_height, chimney_img)
                Chimney(chimney_group, False, random_height, chimney_img)

        santa.rotate(dt)
        santa.jump(events, dt)
        santa.bound()
        if santa.rect.top > WIN_HEIGHT:
            run = False

        screen.blit(wallpaper, (0, 0))

        for ch in chimney_group:
            if santa.mask is not None and ch.mask is not None:
                if pg.sprite.collide_mask(santa, ch):
                    run = False
            ch.move(dt)
            ch.draw(screen)

        santa.draw(screen)
        pg.display.flip()


if __name__ == '__main__':
    main()
