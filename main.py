# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    # Initialize pygame
    pygame.init()
    
    # Set up the screen (window)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Set up the clock for controlling FPS
    clock = pygame.time.Clock()
    dt = 0  # Delta time in seconds, initialized to 0

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop if the window is closed

        # Fill the screen with black color (RGB: 0, 0, 0)
        screen.fill((0, 0, 0))
        
        # Refresh the screen
        pygame.display.flip()

        # Cap the frame rate to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000  # Returns time in milliseconds, convert to seconds

if __name__ == "__main__":
    main()