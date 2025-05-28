"""racing_game_V1.py
This is just same basic code to start the frame work of the game as well as give the game a title"""

import pygame
pygame.init()
WIDTH, HEIGHT = 500, 600
# Create the game screen/window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set the window title
pygame.display.set_caption("Car Racing")
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))
    # Handle events (e.g., user clicks the close button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Stop the loop if the user closes the window
            running = False
    # Update the display to reflect any changes
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame when the loop ends
pygame.quit()
