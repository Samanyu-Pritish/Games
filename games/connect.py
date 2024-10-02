import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect the Dots")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Dot settings
DOT_RADIUS = 5
DOT_COLOR = BLACK
LINE_COLOR = BLUE
LINE_WIDTH = 2

# Dot class
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(SCREEN, DOT_COLOR, (self.x, self.y), DOT_RADIUS)

def main():
    dots = [Dot(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)) for _ in range(10)]
    connections = []
    drawing = False
    last_dot = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_dot = None
                for dot in dots:
                    if (dot.x - mouse_x) ** 2 + (dot.y - mouse_y) ** 2 <= DOT_RADIUS ** 2:
                        clicked_dot = dot
                        break

                if clicked_dot:
                    if last_dot:
                        connections.append((last_dot, clicked_dot))
                    last_dot = clicked_dot

        SCREEN.fill(WHITE)

        # Draw lines
        for line in connections:
            pygame.draw.line(SCREEN, LINE_COLOR, (line[0].x, line[0].y), (line[1].x, line[1].y), LINE_WIDTH)

        # Draw dots
        for dot in dots:
            dot.draw()

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
