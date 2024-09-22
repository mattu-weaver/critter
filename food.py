import random
import utils as ut
import pygame

class Food:
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
        pygame.draw.circle(self.screen, colour, (int(self.x), int(self.y)), self.size)

    def set(self):
        """
        Draw a creature on the screen.
        """
        self.draw(self.colour)


    def clear(self):
        """
        Clear the creature from the screen.
        """
        self.draw(self.env["background"]) 