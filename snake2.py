import pygame
import random
import time

pygame.init()

# Screen and grid settings
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
SNAKE_SPEED = 5

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake setup
snake = [(100, 100), (80, 100), (60, 100)]
direction = (GRID_SIZE, 0)

# Function to generate food with random value and timer
def generate_food():
    while True:
        x = random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE
        y = random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
        if (x, y) not in snake:
            value = random.choice([1, 2, 3])         # Random food weight
            timeout = time.time() + random.randint(5, 10)  # Food disappears after 5–10 seconds
            return {"pos": (x, y), "value": value, "timeout": timeout}

# Initialize food, score, level, and speed
food = generate_food()
score = 0
level = 1
speed = SNAKE_SPEED

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Prevent reversing direction
            if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                direction = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                direction = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                direction = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                direction = (GRID_SIZE, 0)

    # Move snake head
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Collision with wall or self
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake
    ):
        running = False

    snake.insert(0, new_head)

    # Check food collision
    if new_head == food["pos"]:
        score += food["value"]  # Add food value to score
        if score % 3 == 0:
            level += 1
            speed += 1
        food = generate_food()  # Generate new food after eating
    else:
        snake.pop()

    # Check if food expired
    if time.time() > food["timeout"]:
        food = generate_food()  # Replace expired food

    # Draw food
    pygame.draw.rect(screen, RED, (food["pos"][0], food["pos"][1], GRID_SIZE, GRID_SIZE))
    # Draw food value as text
    font = pygame.font.Font(None, 24)
    val_text = font.render(str(food["value"]), True, BLACK)
    screen.blit(val_text, (food["pos"][0] + 4, food["pos"][1] + 2))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # Draw score and level
    status_font = pygame.font.Font(None, 30)
    score_text = status_font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
