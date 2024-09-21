"""
The main appliation file.
"""
# disable E1101 warning
# pylint: disable=E1101
# pylint: disable=E0401

import toml
import pygame
from creature import Creature

cfg = toml.load("config.toml")
pygame.init()
screen = pygame.display.set_mode((cfg["ENV"]["scr_width"], cfg["ENV"]["scr_height"]))
pygame.display.set_caption("Living the dream")
creature_list = []

for i in range(cfg["ENV"]["creature_count"]):
    c = Creature(cfg = cfg, screen = screen, cid=i, age=5,
                 energy=100.0, health=80.0, mass=70.0, x=10.0, y=15.0)
    creature_list.append(c)
    c.draw(cfg["CREATURE"]["colour"])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for c in creature_list[:]:
        c.draw(cfg["ENV"]["background"])
        if c.is_alive():
            c.move()
            c.draw(cfg["CREATURE"]["colour"])
        else:
            creature_list.remove(c)


    pygame.time.wait(cfg["ENV"]["loop_delay"])

    pygame.display.update()
