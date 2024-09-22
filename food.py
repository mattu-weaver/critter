"""
This file contains the Food class.
"""
import random
import pygame
import utils as ut


class Food:
    """
    Represents an item of food in the simulation.
    f_id: int - the unique identifier for the food item
    cfg: dict - the configuration dictionary
    screen: pygame.Surface - the screen object
    """
    def __init__(self, f_id, cfg, screen):
        self.f_id = f_id
        self.screen = screen
        self.cfg = cfg["FOOD"]
        self.env = cfg["ENV"]
        self.x = random.uniform(0, self.env["scr_width"])
        self.y = random.uniform(0, self.env["scr_height"])
        self.size = ut.get_rnd_norm(self.cfg["size"][0], self.cfg["size"][1])
        self.colour = self.cfg["colour"]

    def draw(self, colour):
        """
        Draw the food item on the screen.
        colour: tuple - the RGB colour of the food item
        """
        pygame.draw.circle(self.screen, colour, (int(self.x), int(self.y)), self.size)

    def set(self):
        """
        Draw food on the screen.
        """
        self.draw(self.colour)


    def clear(self):
        """
        Clear food from the screen.
        """
        self.draw(self.env["background"]) 