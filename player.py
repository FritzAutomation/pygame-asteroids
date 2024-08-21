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

    def rotate(self, dt, direction):
        # Rotate the player by PLAYER_TURN_SPEED * dt * direction
        self.rotation += PLAYER_TURN_SPEED * dt * direction

    def move(self, dt, direction):
        # Move the player in the direction they are facing
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction

    def update(self, dt):
        # Get key presses
        keys = pygame.key.get_pressed()

        # Rotate left (a key) or right (d key)
        if keys[pygame.K_a]:
            self.rotate(dt, -1)  # Invert dt for left rotation
        if keys[pygame.K_d]:
            self.rotate(dt, 1)   # Positive dt for right rotation

        # Move forward (w key) or backward (s key)
        if keys[pygame.K_w]:
            self.move(dt, 1)    # Move forward
        if keys[pygame.K_s]:
            self.move(dt, -1)   # Move backward

    def draw(self, screen):
        # Draw the player as a triangle on the screen
        pygame.draw.polygon(screen, "white", self.triangle(), 2)