import pygame
import random

# Initialize Pygame
pygame.init()
# Game screen size and tittle
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)

# Loading and scaling images to the right size
def load_image(filename, size=None):
    image = pygame.image.load(filename).convert_alpha()
    if size:
        image = pygame.transform.scale(image, size)
    return image

# Load background and car images
background_image = load_image("background.jpg", (WIDTH, HEIGHT))
#car size
car_size = (50, 100)
# Main Car
player_image = load_image("car_1.png", car_size)
#Enemy car
enemy_image_filenames = ["car_2.png"] + ["car_3.png"]
enemy_images = [load_image(filename, car_size) for filename in enemy_image_filenames]

# High score loading function
def load_high_score():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except:
        return 0
# Saving users highscore

def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

# Car class
class Car:
    # Initialize a new Car object with the given image, position, and speed
    def __init__(self, image, x, y, speed):
        # Store the image of the car
        self.image = image
        # Create a rectangle for the car's position
        self.rect = image.get_rect(topleft=(x, y))
        # Store the speed of the car
        self.speed = speed

    # Move the car by updating its position
    def move(self):
        # Move the car down by its speed
        self.rect.y += self.speed

        # Check if the car has moved off the bottom of the screen
        if self.rect.top > HEIGHT:
            # Resetting the car's position to a random location above the screen
            self.rect.y = random.randint(-200, -100)
            self.rect.x = random.randint(50, WIDTH - 100)
            # Return True to tell that the car has moved off the screen
            return True
        # Return False to tell that the car is still on the screen
        return False

    def draw(self):
        screen.blit(self.image, self.rect)

# Create player car
player = Car(player_image, WIDTH // 2 - car_size[0] // 2, HEIGHT - 140, 0)

# Create a list to store enemy car objects
enemies = []

# Initialize a variable to store the previous enemy car's x-position
previous_x = None

# Iterate over the list of enemy car images
for image in enemy_images:
    # Generate a random x-position for the enemy car
    x = random.randint(50, WIDTH - 100)

    # If this is not the first enemy car, ensure a gap of at least car_size[0] between it and the previous car
    if previous_x is not None:
        while abs(x - previous_x) < car_size[0]:  # Check if the gap is too small
            # If the gap is too small, generate a new random x-position
            x = random.randint(50, WIDTH - 100)
    # Store the current x-position for the next time
    previous_x = x
    # Generate a random y-position for the enemy car at the top of the screenn
    y = random.randint(-300, -100)
    # Generating speed for the car
    speed = random.randint(3, 6)
    # Create a new Car object
    enemies.append(Car(image, x, y, speed))

# Game variables
score = 0  # Initialize score to 0
high_score = load_high_score()  # Load the high score from storage
game_over = False  # Initialize game over flag to False

# Game loop
running = True
while running:
    # Draw the background image on the screen
    screen.blit(background_image, (0, 0))

    # Handle events (e.g. closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the user closes the window, stop the game loop
            running = False

    # If the game is not over, updating the game stats
    if not game_over:
        # Get the state of the keyboard keys
        keys = pygame.key.get_pressed()

        # Moving the main car depending on the pressed keys
        if keys[pygame.K_LEFT] and player.rect.left > 0:
            player.rect.x -= 5
        if keys[pygame.K_RIGHT] and player.rect.right < WIDTH:
            player.rect.x += 5
        if keys[pygame.K_UP] and player.rect.top > 0:
            player.rect.y -= 5
        if keys[pygame.K_DOWN] and player.rect.bottom < HEIGHT:
            player.rect.y += 5

        # Updating enemy positions
        for enemy in enemies:
            # Move the enemy and check if it has passed the player
            passed = enemy.move()
            if passed:
                # If the enemy has passed the player, increment the score
                score += 1
            # Draw the enemy on the screen
            enemy.draw()

            # Check if the player has collided with the enemy
            if player.rect.colliderect(enemy.rect):
                # If a collision occurs, set the game over flag to True
                game_over = True
                # Check if the current score is higher than the high score
                if score > high_score:
                    # If the current score is higher, update the high score and save it
                    high_score = score
                    save_high_score(high_score)

        # Draw the player on the screen
        player.draw()

        # Draw the score and high score on the screen
        screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
        screen.blit(font.render(f"High Score: {high_score}", True, (255, 255, 0)), (10, 40))

    else:
        # Draw the game over message on the screen
        screen.blit(font.render("Game Over! Press R to Restart", True, (255, 0, 0)), (60, HEIGHT // 2))
        # Checks if key are pressed of the keyboard
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # If the R key is pressed, reset the game
            score = 0
            game_over = False
            player.rect.x = WIDTH // 2 - car_size[0] // 2
            for enemy in enemies:
                enemy.rect.y = random.randint(-300, -100)
                enemy.rect.x = random.randint(50, WIDTH - 100)
# Update the display
    pygame.display.flip()
    #timer
    clock.tick(60)

# Quit the Pygame
pygame.quit()
