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

background_image = load_image("background.jpg", (WIDTH, HEIGHT))
car_size = (50, 100)
player_image = load_image("car_1.png", car_size)
enemy_image = load_image("car_2.png", car_size)

# Define lane x-positions (you can adjust spacing if needed)
lanes = [75, 175, 275, 375]  # These are example fixed positions (4 lanes)

# Player car initial position
player_x = WIDTH // 2 - car_size[0] // 2
player_y = HEIGHT - 140
player_speed = 5

# Enemy car initial position (random lane at the top)
enemy_x = random.choice(lanes)
enemy_y = -100
enemy_speed = 5

running = True

while running:
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, (player_x, player_y))
    screen.blit(enemy_image, (enemy_x, enemy_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
        enemy_x = random.choice(lanes)  # Spawn in a set lane

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
