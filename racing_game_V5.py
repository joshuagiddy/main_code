""""Racing_game_v5
 ,this version adds collision detection so the user has to dodge the enemy or the user loses.
It also adds a game over screen if the user crashes. Adds a score counter but resets after every crash"""

import pygame
import random
pygame.init()

WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing")
clock = pygame.time.Clock()

def load_image(filename, size=None):
    image = pygame.image.load(filename).convert_alpha()
    if size:
        image = pygame.transform.scale(image, size)
    return image

background_image = load_image("background.jpg", (WIDTH, HEIGHT))
car_size = (50, 100)
player_image = load_image("car_1.png", car_size)
enemy_image = load_image("car_2.png", car_size)

player_x = WIDTH // 2 - car_size[0] // 2
player_y = HEIGHT - 140
player_speed = 5

enemy_x = random.randint(50, WIDTH - 100)
enemy_y = -100
enemy_speed = 5

score = 0
font = pygame.font.SysFont("Arial", 36)
small_font = pygame.font.SysFont("Arial", 28)
game_over = False
running = True

while running:
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(enemy_image, (enemy_x, enemy_y))

    # Display the score at the top of the screen
    score_text = small_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x + car_size[0] < WIDTH:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y + car_size[1] < HEIGHT:
            player_y += player_speed

        enemy_y += enemy_speed

        if enemy_y > HEIGHT:
            enemy_y = -100
            enemy_x = random.randint(50, WIDTH - 100)
            score += 1


        player_rect = pygame.Rect(player_x, player_y, *car_size)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, *car_size)


        if player_rect.colliderect(enemy_rect):
            game_over = True

    else:
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(game_over_text, (150, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
