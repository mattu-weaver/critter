"""
The main appliation file.
"""
# disable E1101 warning
# pylint: disable=E1101
# pylint: disable=E0401

import random
import toml
import pygame
from creature import Creature

cfg = toml.load("config.toml")
cfg_c = cfg["CREATURE"]
cfg_e = cfg["ENV"]

pygame.init()
screen = pygame.display.set_mode((cfg["ENV"]["scr_width"], cfg["ENV"]["scr_height"]))
pygame.display.set_caption("Living the dream")


def initialise_simulation():
    """
    Create a list of creatures to simulate. 
    """
    critter_list = []
    for i in range(cfg["ENV"]["creature_count"]):
        energy = random.uniform(cfg_c["energy_min"], cfg_c["energy_max"])
        health = random.uniform(cfg_c["health_min"], cfg_c["health_min"])
        mass = random.uniform(cfg_c["mass_min"], cfg_c["mass_min"])

        critter = Creature(cfg=cfg, screen=screen, cid=i, age=5,
                           energy=energy, health=health, mass=mass, x=10.0, y=15.0)
        critter.draw(cfg_c["colour"])
        critter_list.append(critter)
    return critter_list

creature_list = initialise_simulation()

# Simulation loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for creature in creature_list[:]:
        if creature.is_alive():
            creature.update()
        else:
            creature.draw(cfg_e["background"])
            creature_list.remove(creature)

    pygame.time.wait(cfg_e["loop_delay"])
    pygame.display.update()
