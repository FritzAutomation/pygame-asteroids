import pygame
from constants import *

class CircleShape:
    def __init__(self, radius):
        self.radius = radius

class Player(CircleShape):
    def __init__(self, x, y):
        # Call the parent class's constructor
        super().__init__(PLAYER_RADIUS)
        
        # Initialize position and rotation
        self.position = pygame.Vector2(x, y)
        self.rotation = 0

    def triangle(self):
        # Define the points of the triangle
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # Draw the player as a triangle on the screen
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
