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

if __name__ == "__main__":
    main()
