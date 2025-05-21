import pygame
import random

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)

# Load and scale images
def load_image(filename, size=None):
    image = pygame.image.load(filename).convert_alpha()
    if size:
        image = pygame.transform.scale(image, size)
    return image

# Load background and car images
background_image = load_image("background.jpg", (WIDTH, HEIGHT))
car_size = (50, 100)  # Smaller car size
player_image = load_image("car_1.png", car_size)
enemy_images = [load_image(f"car_2.png", car_size) for i in range(1, 5)]

# High score functions
def load_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except:
        return 0

def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

# Car class
class Car:
    def __init__(self, image, x, y, speed):
        self.image = image
        self.rect = image.get_rect(topleft=(x, y))
        self.speed = speed

    def move(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-200, -100)
            self.rect.x = random.randint(50, WIDTH - 100)
            return True
        return False

    def draw(self):
        screen.blit(self.image, self.rect)

# Create player car
player = Car(player_image, WIDTH // 2 - car_size[0] // 2, HEIGHT - 140, 0)

# Create enemy cars
enemies = []
for img in enemy_images:
    x = random.randint(50, WIDTH - 100)
    y = random.randint(-300, -100)
    speed = random.randint(3, 6)
    enemies.append(Car(img, x, y, speed))

# Game variables
score = 0
high_score = load_high_score()
game_over = False

# Game loop
running = True
while running:
    screen.blit(background_image, (0, 0))  # Draw background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.rect.left > 0:
            player.rect.x -= 5
        if keys[pygame.K_RIGHT] and player.rect.right < WIDTH:
            player.rect.x += 5
        if keys[pygame.K_UP] and player.rect.top > 0:
            player.rect.y -= 5
        if keys[pygame.K_DOWN] and player.rect.bottom < HEIGHT:
            player.rect.y += 5

        for enemy in enemies:
            passed = enemy.move()
            if passed:
                score += 1
            enemy.draw()

            if player.rect.colliderect(enemy.rect):
                game_over = True
                if score > high_score:
                    high_score = score
                    save_high_score(high_score)

        player.draw()

        screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
        screen.blit(font.render(f"High Score: {high_score}", True, (255, 255, 0)), (10, 40))

    else:
        screen.blit(font.render("Game Over! Press R to Restart", True, (255, 0, 0)), (60, HEIGHT // 2))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            score = 0
            game_over = False
            player.rect.x = WIDTH // 2 - car_size[0] // 2
            for enemy in enemies:
                enemy.rect.y = random.randint(-300, -100)
                enemy.rect.x = random.randint(50, WIDTH - 100)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
