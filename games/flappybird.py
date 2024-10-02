# pip install pygame
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
GREEN = (255, 0, 0)

# Game settings
GRAVITY = 0.25
JUMP_STRENGTH = -7
PIPE_WIDTH = 70
PIPE_GAP = 200  # Increased gap between pipes
PIPE_SPEED = 3

# Bird settings
BIRD_COLOR = (161, 26, 219 )
BIRD_SIZE = 15  # Smaller bird size

class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.size = BIRD_SIZE
        self.vel = 0

    def draw(self):
        pygame.draw.circle(SCREEN, BIRD_COLOR, (self.x, int(self.y)), self.size)

    def move(self):
        self.vel += GRAVITY
        self.y += self.vel

    def jump(self):
        self.vel = JUMP_STRENGTH

class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(150, 400)
        self.width = PIPE_WIDTH
        self.gap = PIPE_GAP

    def draw(self):
        pygame.draw.rect(SCREEN, GREEN, (self.x, 0, self.width, self.height))
        pygame.draw.rect(SCREEN, GREEN, (self.x, self.height + self.gap, self.width, HEIGHT))

    def move(self):
        self.x -= PIPE_SPEED

def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        # Move and draw background
        SCREEN.fill(WHITE)

        # Move and draw bird
        bird.move()
        bird.draw()

        # Move and draw pipes
        for pipe in pipes:
            pipe.move()
            pipe.draw()
            if pipe.x + pipe.width < 0:
                pipes.remove(pipe)
                pipes.append(Pipe())
                score += 1

        # Collision detection
        if bird.y + bird.size > HEIGHT or bird.y - bird.size < 0:
            running = False
        for pipe in pipes:
            if pipe.x < bird.x + bird.size < pipe.x + pipe.width:
                if not (pipe.height < bird.y < pipe.height + pipe.gap):
                    running = False

        # Display score
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {score}", True, BLACK)
        SCREEN.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()