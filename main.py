import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display dimensions
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing")
clock = pygame.time.Clock()

# Load and optionally resize an image
def load_image(filename, size=None):
    # Load image with transparency
    image = pygame.image.load(filename).convert_alpha()
    if size:
        image = pygame.transform.scale(image, size)
    return image

# EnemyCar class to manage individual enemy cars
class EnemyCar:
    def __init__(self, image, y_offset_range):
        # Store image and random starting position
        self.image = image
        self.x = random.randint(50, WIDTH - 100)
        self.y = -random.randint(*y_offset_range)
        self.y_offset_range = y_offset_range

    def move(self, speed):
        # Move the enemy car downward
        self.y += speed
        # If it goes off screen, reset its position and return True to increase score
        if self.y > HEIGHT:
            self.reset()
            return True
        return False

    def reset(self):
        # Reset enemy to a new random position above the screen
        self.x = random.randint(50, WIDTH - 100)
        self.y = -random.randint(*self.y_offset_range)

    def draw(self, surface):
        # Draw the enemy car on the screen
        surface.blit(self.image, (self.x, self.y))

    def get_rect(self):
        # Return the rect for collision detection
        return pygame.Rect(self.x, self.y, *car_size)

# Load background and car images
background_image = load_image("background.jpg", (WIDTH, HEIGHT))
car_size = (50, 100)  # Standard size for all cars
player_image = load_image("car_1.png", car_size)
enemy_images = [
    load_image("car_2.png", car_size),
    load_image("car_3.png", car_size),
    load_image("car_2.png", car_size)  # Reuse car_2.png for the third enemy
]

# Player's starting position and speed
player_x = WIDTH // 2 - car_size[0] // 2
player_y = HEIGHT - 140
player_speed = 5

# Fonts for displaying text
font = pygame.font.SysFont("Arial", 36)
small_font = pygame.font.SysFont("Arial", 28)

# Create list of enemy car objects
enemies = [
    EnemyCar(enemy_images[0], (100, 100)),
    EnemyCar(enemy_images[1], (150, 300)),
    EnemyCar(enemy_images[2], (200, 400)),
]

# Game state variables
enemy_speed = 5
score = 0
high_score = 0
game_over = False
running = True

# Game loop
while running:
    # Draw background and player car
    screen.blit(background_image, (0, 0))
    screen.blit(player_image, (player_x, player_y))

    # Draw enemy cars
    for enemy in enemies:
        enemy.draw(screen)

    # Display score and high score
    screen.blit(small_font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    screen.blit(small_font.render(f"High Score: {high_score}", True, (255, 255, 0)), (10, 40))

    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
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

        # Move each enemy car and check if it went off screen
        for enemy in enemies:
            if enemy.move(enemy_speed):
                # Increase score when an enemy is reset
                score += 1
                # Every 5 points, increase enemy speed
                if score % 5 == 0:
                    enemy_speed += 1

        # Create rectangles for collision detection
        player_rect = pygame.Rect(player_x, player_y, *car_size)
        # Check collision between player and any enemy car
        if any(player_rect.colliderect(enemy.get_rect()) for enemy in enemies):
            game_over = True
            # Update high score if current score is higher
            if score > high_score:
                high_score = score

    else:
        # Display game over message
        game_over_text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
        screen.blit(game_over_text, (40, HEIGHT // 2))

        # If R key is pressed, restart the game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_over = False
            score = 0
            enemy_speed = 5
            # Reset player position
            player_x = WIDTH // 2 - car_size[0] // 2
            player_y = HEIGHT - 140
            # Reset all enemy cars
            for enemy in enemies:
                enemy.reset()

    # Update the screen and set the frame rate
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
