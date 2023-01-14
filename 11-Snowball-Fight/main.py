import pygame as pg
from constants import *
from player import Player
from ball import SnowBall

pg.init()

screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pg.SCALED)
pg.display.set_caption("Snowball Fight")
clock = pg.time.Clock()
font = pg.font.SysFont("ComicSans", 16)

player_list = [Player(1), Player(2)]

ball_list = []
ptype_dict = {pg.K_f: 1, pg.K_RETURN: 2}


def keep_active(events):
    for ev in events:
        if ev.type == pg.QUIT:
            return False
        elif ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE:
            return False
    return True


def throw_ball(event_key):
    for p in player_list:
        num = ptype_dict.get(event_key)
        if num is not None and p.type == num:
            ball_list.append(SnowBall(p.rect.center, num))


def check_snowball_hit(ball, player, direction, player_type):
    if ball.direction == direction and player.type == player_type:
        if ball.rect.colliderect(player.rect):
            ball_list.remove(ball)
            player.health -= 1


def main():
    healths_list = [font.render(f"Lives Left: {player_list[i].health}", True, "black") for i in range(2)]
    run = True
    while run:
        keys = pg.key.get_pressed()
        dt = clock.tick() / 100
        events = pg.event.get()
        for ev in events:
            if ev.type == pg.KEYDOWN:
                throw_ball(ev.key)
        run = keep_active(events)

        screen.fill((255, 250, 250))
        pg.draw.line(screen, "black", (WIN_WIDTH / 2, 0), (WIN_WIDTH / 2, WIN_HEIGHT), 2)

        for ball in ball_list:
            ball.move(dt)
            ball.draw(screen)
            if ball.pos.x < 0 or ball.pos.x > WIN_WIDTH:
                ball_list.remove(ball)

        for p in player_list:
            p.move(keys, dt)
            p.draw(screen)
            for ball in ball_list:
                check_snowball_hit(ball, p, 1, 2)
                check_snowball_hit(ball, p, 2, 1)
            if p.health < 0:
                if p.type == 1:
                    print("Player 2 Wins!")
                elif p.type == 2:
                    print("Player 1 Wins!")
                run = False
            else:
                healths_list = [font.render(f"Lives Left: {player_list[i].health}", True, "black") for i in range(2)]

        screen.blit(healths_list[0], (0, 0))
        screen.blit(healths_list[1], (WIN_WIDTH - healths_list[1].get_width(), 0))

        pg.display.flip()


if __name__ == '__main__':
    main()
