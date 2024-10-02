import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = (255, 255, 255)  # White

# Game settings
CATCHER_WIDTH = 100
CATCHER_HEIGHT = 20
OBJECT_RADIUS = 20
OBJECT_FALL_SPEED = 5
CATCHER_COLOR = (0, 0, 255)  # Blue
OBJECT_COLOR = (255, 0, 0)    # Red

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Clock to control frame rate
clock = pygame.time.Clock()

def draw_catcher(x, y):
    pygame.draw.rect(screen, CATCHER_COLOR, (x, y, CATCHER_WIDTH, CATCHER_HEIGHT))

def draw_object(x, y):
    pygame.draw.circle(screen, OBJECT_COLOR, (x, y), OBJECT_RADIUS)

def display_message(message, color, size, position):
    font = pygame.font.SysFont(None, size)
    text = font.render(message, True, color)
    screen.blit(text, position)

def main():
    catcher_x = (SCREEN_WIDTH - CATCHER_WIDTH) // 2
    catcher_y = SCREEN_HEIGHT - CATCHER_HEIGHT - 10

    object_x = random.randint(OBJECT_RADIUS, SCREEN_WIDTH - OBJECT_RADIUS)
    object_y = -OBJECT_RADIUS
    score = 0

    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                catcher_x -= 10
                if catcher_x < 0:
                    catcher_x = 0
            if keys[pygame.K_RIGHT]:
                catcher_x += 10
                if catcher_x > SCREEN_WIDTH - CATCHER_WIDTH:
                    catcher_x = SCREEN_WIDTH - CATCHER_WIDTH

            # Update object position
            object_y += OBJECT_FALL_SPEED

            # Check if the object falls below the screen
            if object_y > SCREEN_HEIGHT:
                # Game over condition
                game_over = True

            # Check for collision
            if (catcher_x < object_x < catcher_x + CATCHER_WIDTH or
                catcher_x < object_x + OBJECT_RADIUS * 2 < catcher_x + CATCHER_WIDTH) and \
               (catcher_y < object_y < catcher_y + CATCHER_HEIGHT):
                score += 1
                object_x = random.randint(OBJECT_RADIUS, SCREEN_WIDTH - OBJECT_RADIUS)
                object_y = -OBJECT_RADIUS

            # Clear the screen
            screen.fill(SCREEN_COLOR)

            # Draw catcher and falling object
            draw_catcher(catcher_x, catcher_y)
            draw_object(object_x, object_y)

            # Display the score
            display_message(f'Score: {score}', (0, 0, 0), 36, (10, 10))

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            clock.tick(30)
        else:
            # Display game over message
            screen.fill(SCREEN_COLOR)
            display_message('Game Over', (255, 0, 0), 72, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
            display_message(f'Score: {score}', (0, 0, 0), 36, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 20))
            pygame.display.flip()
            pygame.time.wait(3000)  # Wait for 3 seconds before quitting

            pygame.quit()
            return

if __name__ == "__main__":
    main()
