import pygame
from constants import *

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, radius):
        super().__init__()  # Initialize the sprite
        self.radius = radius

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(radius)
        
        # Initialize position and velocity
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        # Move the asteroid by its velocity scaled by dt
        self.position += self.velocity * dt

    def draw(self, screen):
        # Draw the asteroid as a circle with a width of 2
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)
