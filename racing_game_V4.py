""""Racing_game_v4
this version adds enemy cars that move downward and spawn in random points at the top of the screen.
Still doesn't work since the enemy cars cannot crash into the users car."""

import pygame
import random
pygame.init()
WIDTH, HEIGHT = 500, 600
# Create the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Setting the title
pygame.display.set_caption("Car Racing")
clock = pygame.time.Clock()

# Function to load and scale the image
def load_image(filename, size=None):
    # Loading image
    image = pygame.image.load(filename).convert_alpha()
    if size:
        # Resizing the image if a size is given
        image = pygame.transform.scale(image, size)
    return image

# Loading the background image to fill the screen
background_image = load_image("background.jpg", (WIDTH, HEIGHT))
# size of car
car_size = (50, 100)
# Loading the player car image
player_image = load_image("car_1.png", car_size)
# Loading the enemy car image
enemy_image = load_image("car_2.png", car_size)

# Setting the position of the player car
player_x = WIDTH // 2 - car_size[0] // 2
player_y = HEIGHT - 140
# Setting the speed of the car movement
player_speed = 5

# Setting theposition of the enemy car, which is any x point on top of the screen
enemy_x = random.randint(50, WIDTH - 100)
enemy_y = -100  # Start above the screen
# Set the speed of the enemy car
enemy_speed = 5

# Game loop control variable
running = True

# Main loop
while running:
    # Start the background image onto the screen
    screen.blit(background_image, (0, 0))
    # Start the player car image at its position
    screen.blit(player_image, (player_x, player_y))
    # Start the enemy car image at its position
    screen.blit(enemy_image, (enemy_x, enemy_y))

    # If user closes program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get which keys are being pressed
    keys = pygame.key.get_pressed()
    # Move left if left key is pressed
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    # Move right if right key is pressed
    if keys[pygame.K_RIGHT] and player_x + car_size[0] < WIDTH:
        player_x += player_speed
    # Move up if up key is pressed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    # Move down if down key is pressed
    if keys[pygame.K_DOWN] and player_y + car_size[1] < HEIGHT:
        player_y += player_speed

    # moving the enemy car downward
    enemy_y += enemy_speed
    # If the enemy moves off the screen, reset it to the top of the screen at a new random x position
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, WIDTH - 100)

    # Update the game screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
