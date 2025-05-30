""""Racing_game_v9
This version introduces multiple enemy cars to make the game more challenging.
Three enemy cars appear and must be dodged simultaneously. Each enemy moves independently."""

import pygame
import random
pygame.init()
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing")
clock = pygame.time.Clock()

# Function to load and scale the image
def load_image(filename, size=None):
    image = pygame.image.load(filename).convert_alpha()
    if size:
        image = pygame.transform.scale(image, size)
    return image

# Load background and car images
background_image = load_image("background.jpg", (WIDTH, HEIGHT))
car_size = (50, 100)
player_image = load_image("car_1.png", car_size)
enemy_image1 = load_image("car_2.png", car_size)
enemy_image2 = load_image("car_3.png", car_size)
enemy_image3 = load_image("car_2.png", car_size)  # reuse car_2.png for a third

# Initial player position
player_x = WIDTH // 2 - car_size[0] // 2
player_y = HEIGHT - 140
player_speed = 5

# Initial enemy positions and speed
enemy1_x = random.randint(50, WIDTH - 100)
enemy1_y = -100
enemy2_x = random.randint(50, WIDTH - 100)
enemy2_y = -300
enemy3_x = random.randint(50, WIDTH - 100)
enemy3_y = -500
enemy_speed = 5

font = pygame.font.SysFont("Arial", 36)
small_font = pygame.font.SysFont("Arial", 28)

game_over = False
score = 0
high_score = 0
running = True

while running:
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(enemy_image1, (enemy1_x, enemy1_y))
    screen.blit(enemy_image2, (enemy2_x, enemy2_y))
    screen.blit(enemy_image3, (enemy3_x, enemy3_y))

    # Display score and high score
    screen.blit(small_font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    screen.blit(small_font.render(f"High Score: {high_score}", True, (255, 255, 0)), (10, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x + car_size[0] < WIDTH:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y + car_size[1] < HEIGHT:
            player_y += player_speed

        # Move enemies
        enemy1_y += enemy_speed
        enemy2_y += enemy_speed
        enemy3_y += enemy_speed

        # Reset and score
        for enemy_index, (x, y) in enumerate([(enemy1_x, enemy1_y), (enemy2_x, enemy2_y), (enemy3_x, enemy3_y)]):
            if y > HEIGHT:
                if enemy_index == 0:
                    enemy1_y = -100
                    enemy1_x = random.randint(50, WIDTH - 100)
                elif enemy_index == 1:
                    enemy2_y = -random.randint(150, 300)
                    enemy2_x = random.randint(50, WIDTH - 100)
                elif enemy_index == 2:
                    enemy3_y = -random.randint(200, 400)
                    enemy3_x = random.randint(50, WIDTH - 100)
                score += 1
                if score % 5 == 0:
                    enemy_speed += 1

        # Collision detection
        player_rect = pygame.Rect(player_x, player_y, *car_size)
        enemy_rects = [
            pygame.Rect(enemy1_x, enemy1_y, *car_size),
            pygame.Rect(enemy2_x, enemy2_y, *car_size),
            pygame.Rect(enemy3_x, enemy3_y, *car_size)
        ]

        if any(player_rect.colliderect(enemy_rect) for enemy_rect in enemy_rects):
            game_over = True
            if score > high_score:
                high_score = score

    else:
        game_over_text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
        screen.blit(game_over_text, (40, HEIGHT // 2))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Reset game state
            game_over = False
            score = 0
            enemy_speed = 5
            player_x = WIDTH // 2 - car_size[0] // 2
            player_y = HEIGHT - 140
            enemy1_x = random.randint(50, WIDTH - 100)
            enemy1_y = -100
            enemy2_x = random.randint(50, WIDTH - 100)
            enemy2_y = -300
            enemy3_x = random.randint(50, WIDTH - 100)
            enemy3_y = -500

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
