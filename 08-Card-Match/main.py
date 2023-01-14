import pygame as pg
import numpy as np
from card import Card

pg.init()

WIN_WIDTH, WIN_HEIGHT = 600, 400
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pg.SCALED)
pg.display.set_caption("Christmas Card Match")
clock = pg.time.Clock()
font = pg.font.SysFont("ComicSans", 36)

# Getting card face images
card_list = [pg.image.load(f"res/cards/{i}.png").convert_alpha() for i in range(4)]

# Random card set
scale = 140
card_array = np.tile(np.arange(4), 2)
np.random.shuffle(card_array)
card_array = card_array.reshape((4, 2))

flipped_cards = pg.sprite.Group()
card_group = pg.sprite.Group()
for pos, value in np.ndenumerate(card_array):
    x_offset = 50
    y_offset = WIN_HEIGHT / 6
    scaled_pos = pos[0] * scale + x_offset, pos[1] * scale + y_offset
    Card(card_group, card_list[value], value, scaled_pos)

# Flip cards when wrong match
FLIP_EVENT = pg.event.custom_type()

text_surf = font.render("You Matched All The Cards!", True, "white")
text_rect = text_surf.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))


def main():
    flippable = True
    run = True
    while run:
        events = pg.event.get()
        for ev in events:
            if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE):
                run = False
            elif ev.type == FLIP_EVENT:
                for card in card_group:
                    card.flipped = False
                # Allow cards to be wrong again
                flippable = True

        screen.fill((100, 0, 100))
        for card in card_group:
            card.user_input(events)
            # Will not duplicate
            flipped_cards.add(card) if card.flipped else flipped_cards.remove(card)
            card.draw(screen)

        # Check once group at 2 limit
        if len(flipped_cards) == 2:
            lst = flipped_cards.sprites()
            # Clear cards from groups in same
            if lst[0].type == lst[1].type:
                for matched in flipped_cards:
                    matched.kill()
            else:
                # Change all cards to back-up after half a second
                if flippable:
                    pg.time.set_timer(FLIP_EVENT, 500, 1)
                    flippable = False
            # After either, empty group
            flipped_cards.empty()

        # Done matching all cards
        if len(card_group) == 0:
            screen.blit(text_surf, text_rect)

        pg.display.flip()


if __name__ == '__main__':
    main()
