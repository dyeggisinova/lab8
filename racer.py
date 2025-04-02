import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GOLD = (255, 215, 0)

# Player Car
player = pygame.Rect(WIDTH//2 - 25, HEIGHT - 100, 50, 80)
player_speed = 5

# Obstacles
obstacles = []
obstacle_speed = 5

# Coins
coins = []
coin_speed = 5
coin_count = 0

font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += player_speed
    
    # Generate obstacles
    if random.randint(1, 50) == 1:
        obstacles.append(pygame.Rect(random.randint(0, WIDTH - 50), -50, 50, 80))
    
    # Move obstacles
    for obstacle in obstacles[:]:
        obstacle.y += obstacle_speed
        if obstacle.y > HEIGHT:
            obstacles.remove(obstacle)
        pygame.draw.rect(screen, RED, obstacle)
    
    # Generate coins
    if random.randint(1, 80) == 1:
        coins.append(pygame.Rect(random.randint(0, WIDTH - 30), -30, 30, 30))
    
    # Move coins
    for coin in coins[:]:
        coin.y += coin_speed
        if coin.y > HEIGHT:
            coins.remove(coin)
        pygame.draw.circle(screen, GOLD, (coin.x + 15, coin.y + 15), 15)
    
    # Collision detection
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            running = False
    
    for coin in coins[:]:
        if player.colliderect(coin):
            coin_count += 1
            coins.remove(coin)
    
    # Draw player
    pygame.draw.rect(screen, BLACK, player)
    
    # Display coin count
    coin_text = font.render(f"Coins: {coin_count}", True, BLACK)
    screen.blit(coin_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
