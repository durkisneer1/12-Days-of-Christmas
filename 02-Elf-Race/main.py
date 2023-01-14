import pygame as pg
from random import randint
from constants import *
from opponent import OpponentElf
from player import PlayerElf

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Elf Race")
clock = pg.time.Clock()
font = pg.font.SysFont("Comicsans", 96)

opp_group = pg.sprite.Group()
for i in range(WIN_HEIGHT // 100):
    i *= 100
    if i == WIN_HEIGHT / 2:
        player = PlayerElf((0, i))
    else:
        OpponentElf(opp_group, (0, i), randint(200, 300))


def main():
    text = None
    finish = False
    run = True
    while run:
        dt = clock.tick() / 1000
        events = pg.event.get()
        for ev in events:
            if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE):
                run = False

        screen.fill("lightgray")
        if not finish:
            player.run(events, dt)
            player.animate(dt)
            player.draw(screen)

            for opp in opp_group:  # End Game
                opp.run(dt)
                opp.animate(dt)
                opp.draw(screen)
                if opp.pos.x > WIN_WIDTH:
                    finish = True
                    text = font.render("You Lose.", True, "black")

            if player.pos.x > WIN_WIDTH:  # Level Reset
                finish = True
                text = font.render("You Win!", True, "black")
        else:
            screen.blit(text, (WIN_WIDTH / 2 - text.get_width() / 2,
                               WIN_HEIGHT / 2 - text.get_height() / 2))

        pg.display.flip()


if __name__ == '__main__':
    main()
