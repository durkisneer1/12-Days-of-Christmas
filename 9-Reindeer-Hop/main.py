import pygame as pg
import random as r
from constants import *
from player import Player
from reindeer import Reindeer

pg.init()

screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pg.SCALED)
pg.display.set_caption("Reindeer Hop")
clock = pg.time.Clock()
font = pg.font.SysFont("ComicSans", 16)

SPAWN_EVENT = pg.event.custom_type()
pg.time.set_timer(SPAWN_EVENT, 1500)

ground_rect = pg.Rect(0, WIN_HEIGHT * 3/4, WIN_WIDTH, WIN_HEIGHT / 4)
player = Player(ground_rect)

deer_list = []
deer_frame_list = [pg.transform.scale(
    pg.image.load(f"res/deer_anim/{i}.png"),
    (42, 42)).convert_alpha() for i in range(6)]

star_img = pg.transform.scale(
    pg.image.load("res/star.png"),
    (40, 60)
).convert_alpha()


def main():
    star_x = WIN_WIDTH - star_img.get_width()
    text_surf = font.render(f"Lives Left: {player.lives}", False, "white")
    run = True
    while run:
        dt = clock.tick() / 100
        keys = pg.key.get_pressed()
        for ev in pg.event.get():
            if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE):
                run = False
            elif ev.type == SPAWN_EVENT:
                spawn_type = r.choice(["ground", "air"])
                deer_list.append(Reindeer(deer_frame_list, spawn_type, ground_rect))

        screen.fill((20, 0, 75))
        pg.draw.rect(screen, (255, 250, 250), ground_rect)

        player.animate(dt)
        player.move(keys, dt)
        player.draw(screen)

        for deer in deer_list:
            deer.animate(dt)
            deer.move(dt)
            deer.draw(screen)

            if pg.sprite.collide_mask(deer, player):
                deer_list.remove(deer)
                player.lives -= 1
                text_surf = font.render(f"Lives Left: {player.lives}", False, "white")
                if player.lives < 0:
                    run = False

        star_x -= dt * 2  # 10 for testing
        if star_x < -star_img.get_width():
            run = False
        screen.blit(star_img, (star_x, 0))
        screen.blit(text_surf, (0, 0))

        pg.display.flip()


if __name__ == '__main__':
    main()
