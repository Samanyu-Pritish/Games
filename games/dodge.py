import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Shapes")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Game settings
PLAYER_SIZE = 50
PLAYER_COLOR = BLUE
SHAPE_SIZE = 50
SHAPE_COLOR = RED
SHAPE_FALL_SPEED = 5
SHAPE_INTERVAL = 30
SHAPE_SPEED = 5

# Player class
class Player:
    def __init__(self):
        self.x = WIDTH // 2 - PLAYER_SIZE // 2
        self.y = HEIGHT - PLAYER_SIZE - 10
        self.size = PLAYER_SIZE
        self.vel = 10

    def draw(self):
        pygame.draw.rect(SCREEN, PLAYER_COLOR, (self.x, self.y, self.size, self.size))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x - self.vel > 0:
            self.x -= self.vel
        if keys[pygame.K_RIGHT] and self.x + self.vel < WIDTH - self.size:
            self.x += self.vel

# Shape class
class Shape:
    def __init__(self):
        self.x = random.randint(0, WIDTH - SHAPE_SIZE)
        self.y = -SHAPE_SIZE
        self.size = SHAPE_SIZE

    def draw(self):
        pygame.draw.rect(SCREEN, SHAPE_COLOR, (self.x, self.y, self.size, self.size))

    def move(self):
        self.y += SHAPE_FALL_SPEED

def draw_game_over_screen(score):
    SCREEN.fill(WHITE)
    font = pygame.font.Font(None, 74)
    text = font.render(f"Game Over", True, BLACK)
    SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 100))
    
    font = pygame.font.Font(None, 50)
    score_text = font.render(f"Score: {score}", True, BLACK)
    SCREEN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    
    pygame.display.flip()

def main():
    clock = pygame.time.Clock()
    player = Player()
    shapes = []
    shape_timer = 0
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return  # Exit the game when the mouse is clicked on the game over screen

        keys = pygame.key.get_pressed()
        player.move(keys)

        # Add new shapes
        shape_timer += 1
        if shape_timer >= SHAPE_INTERVAL:
            shapes.append(Shape())
            shape_timer = 0

        # Move and draw shapes
        SCREEN.fill(WHITE)
        player.draw()

        for shape in shapes:
            shape.move()
            shape.draw()
            if shape.y > HEIGHT:
                shapes.remove(shape)
                score += 1
            # Check for collision
            if (player.x < shape.x + shape.size and
                player.x + player.size > shape.x and
                player.y < shape.y + shape.size and
                player.y + player.size > shape.y):
                draw_game_over_screen(score)
                pygame.time.wait(2000)  # Wait for 2 seconds before quitting
                pygame.quit()
                return

        # Display score
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, BLACK)
        SCREEN.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
