""""Racing_game_v5
 ,this version adds collision detection so the user has to dodge the enemy or the user loses.
It also adds a game over screen if the user crashes."""

import pygame
import random  # Import random to choose random positions and speeds
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

# Set the initial position of the player car
player_x = WIDTH // 2 - car_size[0] // 2
player_y = HEIGHT - 140
# Set the speed of the car movement
player_speed = 5

# Set the initial position of the enemy car (random x, above screen)
enemy_x = random.randint(50, WIDTH - 100)
enemy_y = -100  # Start above the screen
# Set the speed of the enemy car
enemy_speed = 5

# Set up font for text
font = pygame.font.SysFont("Arial", 36)
# Track whether the game is over
game_over = False

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

    # If the game is not over, allow movement and update
    if not game_over:
        # Get which keys are being pressed
        keys = pygame.key.get_pressed()
        # Move left if LEFT key is pressed and car is not off screen
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        # Move right if RIGHT key is pressed and car is not off screen
        if keys[pygame.K_RIGHT] and player_x + car_size[0] < WIDTH:
            player_x += player_speed
        # Move up if UP key is pressed and car is not off screen
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        # Move down if DOWN key is pressed and car is not off screen
        if keys[pygame.K_DOWN] and player_y + car_size[1] < HEIGHT:
            player_y += player_speed

        # Move the enemy car downward
        enemy_y += enemy_speed

        # If the enemy moves off the screen, reset it to the top at a new random x position
        if enemy_y > HEIGHT:
            enemy_y = -100
            enemy_x = random.randint(50, WIDTH - 100)

        # Createing rectangles for collision detection
        player_rect = pygame.Rect(player_x, player_y, car_size[0], car_size[1])
        enemy_rect = pygame.Rect(enemy_x, enemy_y, car_size[0], car_size[1])

        # Checking if player collides with enemy
        if player_rect.colliderect(enemy_rect):
            game_over = True  # Set game over flag to True

    else:
        # Show "Game Over" message when a crash happens
        game_over_text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
        screen.blit(game_over_text, (40, HEIGHT // 2))

        # Restarts game by pressing R
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Resetting the game
            game_over = False
            player_x = WIDTH // 2 - car_size[0] // 2
            player_y = HEIGHT - 140
            enemy_x = random.randint(50, WIDTH - 100)
            enemy_y = -100

    # Update the game screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
