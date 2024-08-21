# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    # Initialize pygame
    pygame.init()
    
    # Set up the screen (window)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Set up the clock for controlling FPS
    clock = pygame.time.Clock()
    dt = 0  # Delta time in seconds, initialized to 0

    # Create groups for updatables and drawables
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Create player at the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Add the player to both groups
    updatable.add(player)
    drawable.add(player)

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop if the window is closed

        # Update all objects in the updatable group
        for obj in updatable:
            obj.update(dt)

        # Fill the screen with black color (RGB: 0, 0, 0)
        screen.fill((0, 0, 0))

        # Draw all objects in the drawable group
        for obj in drawable:
            obj.draw(screen)
        
        # Refresh the screen
        pygame.display.flip()

        # Cap the frame rate to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000  # Returns time in milliseconds, convert to seconds

if __name__ == "__main__":
    main()