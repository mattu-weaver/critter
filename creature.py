from dataclasses import dataclass
import random
import pygame

@dataclass
class Creature:
    screen: pygame.Surface
    cfg: dict
    cid: int
    mass: float
    x: float
    y: float
    width: int = 1200
    height: int = 900
    speed: float = 0.0
    age: float = 30
    energy: float = 100
    health: float = 100

    def __post_init__(self):
        """Automatically called after initialisation to calculate speed."""
        self.calculate_speed()
        self.width, self.height = self.screen.get_size()
        self.x = self.width // 2
        self.y = self.height // 2

    def draw(self, colour):
        """Draw the creature on the screen."""
        pygame.draw.rect(self.screen, colour, (self.x, self.y, 10, 10))


    def calculate_speed(self):
        """Calculate the creature's speed based on energy and mass."""
        if self.mass > 0:
            self.speed = (self.energy / self.mass) * self.cfg["CREATURE"]["speed_factor"]
        else:
            self.speed = 0.0

    def move(self):
        """Move the creature in search of food while staying within screen boundaries."""
        if self.energy > 0:
            # Random movement logic: moves by `speed` units in a random direction
            dx = random.uniform(-1, 1) * self.speed
            dy = random.uniform(-1, 1) * self.speed
            # Update position
            new_x = self.x + dx
            new_y = self.y + dy

            # Ensure the creature doesn't move out of bounds
            self.x = max(0, min(new_x, self.width))   # Clamp x between 0 and SCREEN_WIDTH
            self.y = max(0, min(new_y, self.height))  # Clamp y between 0 and SCREEN_HEIGHT

            # Reduce energy with each move
            if not self.cfg["CREATURE"]["infinite_energy"]:
                self.energy -= 1

            # Recalculate speed after energy decreases
            self.calculate_speed()

    def is_alive(self) -> bool:
        """Check if the creature is alive."""
        return self.health > 0

    def __repr__(self):
        return (f"Creature(cid={self.cid}, age={self.age}, energy={self.energy}, health={self.health}, "
                f"mass={self.mass}, x={self.x}, y={self.y}, speed={self.speed})")

