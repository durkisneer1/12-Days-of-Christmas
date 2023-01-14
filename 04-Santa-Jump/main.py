import pygame as pg
from constants import *
from bouncer import BouncePlatform
from player import Player

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Santa Jump")
clock = pg.time.Clock()

all_group = pg.sprite.Group()
platform_group = pg.sprite.Group()
for i in range(WIN_HEIGHT // 100):
    platform_spawn = i * 100
    BouncePlatform([platform_group, all_group], platform_spawn)

player = Player(all_group)


def main():
    run = True
    while run:
        dt = clock.tick() / 100
        keys = pg.key.get_pressed()
        for ev in pg.event.get():
            if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE):
                run = False
        if player.dead():
            run = False

        screen.fill((50, 10, 120))
        for plat in platform_group:
            plat.move(dt)
            plat.draw(screen)
            if plat.rect.colliderect(player.rect) and not player.up:
                if player.rect.bottom < plat.rect.bottom:
                    player.bounce()

        if player.pos.y < WIN_HEIGHT / 2:
            y_offset = player.pos.y - WIN_HEIGHT / 2
            for sprites in all_group:
                sprites.pos.y -= y_offset

        player.move(dt, keys)
        player.get_direction()
        player.draw(screen)

        pg.display.flip()


if __name__ == '__main__':
    main()
