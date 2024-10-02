import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player settings
player_width, player_height = 100, 20
player = pygame.Rect(WIDTH // 2 - player_width // 2, HEIGHT - player_height - 10, player_width, player_height)
player_speed = 5

# Bullet settings
bullet_width, bullet_height = 5, 10
bullet_speed = 7
bullets = []

# Enemy settings
enemy_width, enemy_height = 50, 30
enemy_speed = 3
num_of_rows = 6
num_of_columns = 10
enemies = []

# Create a grid of enemies
for row in range(num_of_rows):
    for col in range(num_of_columns):
        x = col * (enemy_width + 10) + 50
        y = row * (enemy_height + 10) + 50
        enemies.append(pygame.Rect(x, y, enemy_width, enemy_height))

# Game loop
running = True
clock = pygame.time.Clock()
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player.centerx - bullet_width // 2, player.top - bullet_height, bullet_width, bullet_height)
                bullets.append(bullet)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    # Keep player within screen bounds
    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH

    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Move enemies
    for enemy in enemies:
        enemy.x += enemy_speed
        if enemy.right > WIDTH or enemy.left < 0:
            enemy_speed = -enemy_speed
            for e in enemies:
                e.y += enemy_height // 2
            break

    # Check for bullet collisions with enemies
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    # Check for enemies reaching the bottom of the screen
    for enemy in enemies:
        if enemy.bottom >= HEIGHT - player_height:
            game_over = True
            running = False
            break

    # Check for win condition
    if not enemies:
        print("You Win!")
        running = False

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, GREEN, enemy)

    pygame.display.flip()
    clock.tick(30)

if game_over:
    print("Game Over!")    

pygame.quit()
