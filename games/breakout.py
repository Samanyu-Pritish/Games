import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions and constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BALL_SIZE = 20
BRICK_WIDTH = 75
BRICK_HEIGHT = 30
BRICK_ROWS = 5
BRICK_COLUMNS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")

# Clock to control frame rate
clock = pygame.time.Clock()

def draw_paddle(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, PADDLE_WIDTH, PADDLE_HEIGHT))

def draw_ball(x, y):
    pygame.draw.ellipse(screen, GREEN, (x, y, BALL_SIZE, BALL_SIZE))

def draw_bricks(bricks):
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

def check_collision(rect1, rect2):
    return pygame.Rect(rect1).colliderect(rect2)

def main():
    paddle_x = (SCREEN_WIDTH - PADDLE_WIDTH) // 2
    paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT - 10
    ball_x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
    ball_y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
    ball_dx = random.choice([-4, 4])
    ball_dy = -4

    bricks = []
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLUMNS):
            brick_x = col * (BRICK_WIDTH + 5) + 30
            brick_y = row * (BRICK_HEIGHT + 5) + 30
            bricks.append(pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= 5
        if keys[pygame.K_RIGHT] and paddle_x < SCREEN_WIDTH - PADDLE_WIDTH:
            paddle_x += 5

        # Move the ball
        ball_x += ball_dx
        ball_y += ball_dy

        # Ball collision with walls
        if ball_x <= 0 or ball_x >= SCREEN_WIDTH - BALL_SIZE:
            ball_dx *= -1
        if ball_y <= 0:
            ball_dy *= -1

        # Ball collision with paddle
        if check_collision((ball_x, ball_y, BALL_SIZE, BALL_SIZE), (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)):
            ball_dy *= -1

        # Ball collision with bricks
        for brick in bricks[:]:
            if check_collision((ball_x, ball_y, BALL_SIZE, BALL_SIZE), brick):
                ball_dy *= -1
                bricks.remove(brick)

        # Ball falling below the paddle
        if ball_y > SCREEN_HEIGHT:
            print("Game Over!")
            pygame.quit()
            return

        # Clear screen
        screen.fill(BLACK)

        # Draw everything
        draw_paddle(paddle_x, paddle_y)
        draw_ball(ball_x, ball_y)
        draw_bricks(bricks)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
