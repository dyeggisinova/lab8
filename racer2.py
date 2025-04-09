import pygame
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GOLD = (255, 215, 0)

# Player setup
player = pygame.Rect(WIDTH//2 - 25, HEIGHT - 100, 50, 80)
player_speed = 5

# Obstacles and coins
obstacles = []
obstacle_speed = 5

coins = []  # List of tuples: (coin_rect, coin_value)
coin_speed = 5
coin_count = 0

# Font
font = pygame.font.Font(None, 36)

# Coin collection to trigger speed increase
coin_threshold = 5  # Every N coins, speed increases
next_threshold = coin_threshold

running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += player_speed

    # Generate new obstacles randomly
    if random.randint(1, 50) == 1:
        obstacles.append(pygame.Rect(random.randint(0, WIDTH - 50), -50, 50, 80))

    # Move and draw obstacles
    for obstacle in obstacles[:]:
        obstacle.y += obstacle_speed
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)
        pygame.draw.rect(screen, RED, obstacle)

    # Randomly generate coins with different weights
    if random.randint(1, 80) == 1:
        value = random.choice([1, 2, 3])  # Random coin value
        coin_rect = pygame.Rect(random.randint(0, WIDTH - 30), -30, 30, 30)
        coins.append((coin_rect, value))

    # Move and draw coins
    for coin, value in coins[:]:
        coin.y += coin_speed
        if coin.y > HEIGHT:
            coins.remove((coin, value))
        pygame.draw.circle(screen, GOLD, (coin.x + 15, coin.y + 15), 15)
        # Optional: draw the value inside the coin
        value_text = font.render(str(value), True, BLACK)
        screen.blit(value_text, (coin.x + 7, coin.y + 3))

    # Collision with obstacles ends game
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            running = False

    # Collision with coins adds to score
    for coin, value in coins[:]:
        if player.colliderect(coin):
            coin_count += value
            coins.remove((coin, value))

            # Increase enemy speed when threshold reached
            if coin_count >= next_threshold:
                obstacle_speed += 1
                next_threshold += coin_threshold

    # Draw player
    pygame.draw.rect(screen, BLACK, player)

    # Draw coin score
    coin_text = font.render(f"Coins: {coin_count}", True, BLACK)
    screen.blit(coin_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
