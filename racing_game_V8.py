""""Racing_game_v8
This version increases difficulty over time by making the enemy car move faster
as the player's score increases. The speed increases every 5 points earned."""

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

# Set the initial position of the player car
player_x = WIDTH // 2 - car_size[0] // 2
player_y = HEIGHT - 140
# Set the speed of the car movement
player_speed = 5

# Set the initial position of the enemy car
enemy_x = random.randint(50, WIDTH - 100)
enemy_y = -100  # Start above the screen
# Set the initial speed of the enemy car
enemy_speed = 5

# Set up font for text
font = pygame.font.SysFont("Arial", 36)
small_font = pygame.font.SysFont("Arial", 28)

# Track whether the game is over
game_over = False
# Track the player's score
score = 0
# Track the highest score
high_score = 0

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

    # Display the current score and high score at the top
    score_text = small_font.render(f"Score: {score}", True, (255, 255, 255))
    high_score_text = small_font.render(f"High Score: {high_score}", True, (255, 255, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (10, 40))

    # If user closes program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # If the game is not over, allow movement and update
    if not game_over:
        # Get which keys are being pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x + car_size[0] < WIDTH:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y + car_size[1] < HEIGHT:
            player_y += player_speed

        # Move the enemy car downward
        enemy_y += enemy_speed

        # If the enemy moves off screen, reset it and increase difficulty
        if enemy_y > HEIGHT:
            enemy_y = -100
            enemy_x = random.randint(50, WIDTH - 100)
            score += 1  # Add 1 to score

            # Increase difficulty every 5 points
            if score % 5 == 0:
                enemy_speed += 1

        # Create rectangles for collision detection
        player_rect = pygame.Rect(player_x, player_y, car_size[0], car_size[1])
        enemy_rect = pygame.Rect(enemy_x, enemy_y, car_size[0], car_size[1])

        # Collision detection
        if player_rect.colliderect(enemy_rect):
            game_over = True
            if score > high_score:
                high_score = score

    else:
        # Show "Game Over" message when a crash happens
        game_over_text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
        screen.blit(game_over_text, (40, HEIGHT // 2))

        # Restarts game by pressing R
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_over = False
            score = 0
            enemy_speed = 5  # Reset enemy speed
            player_x = WIDTH // 2 - car_size[0] // 2
            player_y = HEIGHT - 140
            enemy_x = random.randint(50, WIDTH - 100)
            enemy_y = -100

    # Update the game screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
