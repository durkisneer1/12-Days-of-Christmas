import pygame as pg
from constants import *
from present import Present
from player import Player

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Steal the Presents!")
clock = pg.time.Clock()

bg_img = pg.image.load("res/background.jpg").convert()
bg_img = pg.transform.scale(bg_img, (WIN_WIDTH, WIN_HEIGHT))

present = Present()
player = Player()
final_score = 0


def main():
    global final_score
    run = True
    while run:
        dt = clock.tick() / 1000
        events = pg.event.get()
        for ev in events:
            if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE):
                run = False
        if player.bound():
            run = False

        player.move(dt, events)
        if present.rect.colliderect(player.rect):
            present.reposition()
            player.speed += 1
            final_score += 1

        screen.blit(bg_img, (0, 0))
        present.draw(screen)
        player.draw(screen)

        pg.display.flip()


if __name__ == '__main__':
    main()
    print(final_score)
