"""
File contains the creature class which is responsible for the creature's behaviour and attributes.
"""
# pylint: disable=R0902

import random
import pygame
import math
import utils as ut


class Creature:
    """
    Definition for a creatire in this simulation.
    """

    def __init__(self, c_id, cfg, screen):
        """
        Initialises a creature with the specified attributes.
        """
        self.cfg = cfg["CREATURE"]
        self.env = cfg["ENV"]
        self.cid = c_id
        self.screen = screen
        self.mass = ut.get_rnd_norm(self.cfg["mass"][0], self.cfg["mass"][1])
        self.width, self.height = self.screen.get_size()
        self.x = random.uniform(0, self.width)
        self.y = random.uniform(0, self.height)
        self.energy = ut.get_rnd_norm(self.cfg["energy"][0], self.cfg["energy"][1])
        self.health = ut.get_rnd_norm(self.cfg["health"][0], self.cfg["health"][1])
        self.age = 0.0
        self.age_factor = self.cfg["age_factor"]
        self.old_age = self.cfg["old_age"]
        self.speed = self.calculate_speed()


    def set(self):
        """
        Draw a creature on the screen.
        """
        self.draw(self.cfg["colour"])


    def clear(self):
        """
        Clear the creature from the screen.
        """
        self.draw(self.env["background"])


    def draw(self, colour):
        """
        Draw the creature on the screen.
        """
        pygame.draw.rect(self.screen, colour, (self.x, self.y, 10, 10))


    def get_older(self):
        """
        Increment the age of the creature.
        """
        self.age += self.age_factor


    def update(self):
        """
        Updates a creature, moving it and reducing its energy.
        """
        self.get_older()

        self.draw(self.env["background"])
        if self.is_alive():
            self.move()
            self.draw(self.cfg["colour"])

        if self.energy < self.cfg["low_energy_limit"]:
            self.health -= self.cfg["health_energy_reduction"]


    def set_birth_mass(self, mean=8, std_dev=1):
        """
        Generate a random value from a normal distribution within the specified range.
        """
        self.mass = random.gauss(mean, std_dev)
        # Ensure the value is within the specified range


    def calculate_speed(self):
        """
        Calculate the creature's speed based on energy and mass.
        """
        if self.mass > 0:
            return (self.energy / self.mass) * self.cfg["speed_factor"]
        else:
            return 0.0


    def move(self):
        """
        Move the creature in search of food while staying within screen boundaries.
        """
        if self.energy > 0:
            dx = random.uniform(-1, 1) * self.speed
            dy = random.uniform(-1, 1) * self.speed

            # Update position
            new_x = self.x + dx
            new_y = self.y + dy

            # Ensure the creature doesn't move out of bounds
            self.x = max(0, min(new_x, self.width))
            self.y = max(0, min(new_y, self.height))

            # Reduce energy with each move
            if not self.cfg["infinite_energy"]:
                self.energy -= 1

            if self.energy < 0:
                self.energy = 0

            # Recalculate speed after energy decreases
            self.calculate_speed()


    def is_alive(self) -> bool:
        """
        Check if the creature is alive.
        Being alive means the creature has health greater tha nzero.
        """
        return self.health > 0


    def eat(self, food):
        """
        The creature eats the food.
        """
        self.energy += food.size
        #self.health += food.health
        #self.mass += food.mass
        self.calculate_speed()
        #food.clear()


    def is_over_food(self, food):
        """
        Check if the creature is over the food.
        """
        distance = math.sqrt((self.x - food.x) ** 2 + (self.y - food.y) ** 2)
        return distance < 2 * food.size


    def __repr__(self):
        """
        Return a string representation of the creature.
        """
        return f"""Creature(cid={self.cid}, age={self.age:.1f},
                   energy={self.energy:.1f}, health={self.health:.1f}, 
                   mass={self.mass:.1f}, x={self.x:.0f}, y={self.y:.0f}, 
                   speed={self.speed:.1f})"""
 