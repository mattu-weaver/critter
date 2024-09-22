"""
The main appliation file.
"""
# disable E1101 warning
# pylint: disable=E1101
# pylint: disable=E0401

import toml
import pygame
from creature import Creature
from food import Food

# Read configuration details from config.toml
cfg = toml.load("config.toml")
cfg_e = cfg["ENV"]

pygame.init()
screen = pygame.display.set_mode((cfg_e["scr_width"], cfg_e["scr_height"]))
pygame.display.set_caption("Living the dream")


def check_creature_over_food(critter, food_items):
    """
    Check if the creature is over any food item in the food list.
    """
    for f in food_items:
        if critter.is_over_food(f):
            return f
    return None


def initialise_food():
    """
    Create a list of food items to simulate. 
    Size is randomly assigned within a specified range defined in config.toml.
    """
    food_items = []
    for f in range(cfg_e["food_count"]):
        food_item = Food(f_id = f, cfg=cfg, screen=screen)
        food_item.set()
        food_items.append(food_item)
    return food_items


def initialise_simulation():
    """
    Create a list of creatures to simulate. 
    Energy, health and mass are randomly assigned within a specified range defined in config.toml.
    """
    food_items = initialise_food()

    critter_list = []
    for i in range(cfg["ENV"]["creature_count"]):
        critter = Creature(c_id = i, cfg=cfg, screen=screen)
        critter.set()
        critter_list.append(critter)
    return food_items, critter_list


food_list, creature_list = initialise_simulation()


# The main simulation loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    for food in food_list:
        food.set()

    for creature in creature_list[:]:
        if creature.is_alive():
            creature.update()
            if found_food := check_creature_over_food(creature, food_list):
                creature.eat(found_food)
                found_food.clear()
                
                if found_food in food_list:
                    food_list.remove(found_food)
        else:
            creature.clear()
            creature_list.remove(creature)

    pygame.time.wait(cfg_e["loop_delay"])
    pygame.display.update()
