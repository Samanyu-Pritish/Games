import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 40
MAZE_WIDTH = SCREEN_WIDTH // TILE_SIZE
MAZE_HEIGHT = SCREEN_HEIGHT // TILE_SIZE

# Colors
WALL_COLOR = (0, 0, 0)  # Black
PATH_COLOR = (255, 255, 255)  # White
PLAYER_COLOR = (0, 0, 255)  # Blue
WIN_COLOR = (0, 255, 0)  # Green

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

# Clock to control frame rate
clock = pygame.time.Clock()

def generate_maze(width, height):
    maze = [[1] * width for _ in range(height)]
    stack = [(0, 0)]
    maze[0][0] = 0

    while stack:
        x, y = stack[-1]
        neighbors = []

        if x > 1 and maze[y][x - 2] == 1:
            neighbors.append((x - 2, y))
        if x < width - 2 and maze[y][x + 2] == 1:
            neighbors.append((x + 2, y))
        if y > 1 and maze[y - 2][x] == 1:
            neighbors.append((x, y - 2))
        if y < height - 2 and maze[y + 2][x] == 1:
            neighbors.append((x, y + 2))

        if neighbors:
            nx, ny = random.choice(neighbors)
            maze[ny][nx] = 0
            maze[(ny + y) // 2][(nx + x) // 2] = 0
            stack.append((nx, ny))
        else:
            stack.pop()

    return maze

def draw_maze(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = PATH_COLOR if cell == 0 else WALL_COLOR
            pygame.draw.rect(screen, color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def draw_player(x, y):
    pygame.draw.rect(screen, PLAYER_COLOR, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def draw_win_message():
    font = pygame.font.SysFont(None, 74)
    text = font.render('You Win!', True, WIN_COLOR)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)

def main():
    maze = generate_maze(MAZE_WIDTH, MAZE_HEIGHT)
    player_x, player_y = 0, 0
    goal_x, goal_y = MAZE_WIDTH - 1, MAZE_HEIGHT - 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0 and maze[player_y][player_x - 1] == 0:
            player_x -= 1
        if keys[pygame.K_RIGHT] and player_x < MAZE_WIDTH - 1 and maze[player_y][player_x + 1] == 0:
            player_x += 1
        if keys[pygame.K_UP] and player_y > 0 and maze[player_y - 1][player_x] == 0:
            player_y -= 1
        if keys[pygame.K_DOWN] and player_y < MAZE_HEIGHT - 1 and maze[player_y + 1][player_x] == 0:
            player_y += 1

        if (player_x, player_y) == (goal_x, goal_y):
            screen.fill(PATH_COLOR)
            draw_maze(maze)
            draw_player(player_x, player_y)
            draw_win_message()
            pygame.display.flip()
            pygame.time.wait(2000)  # Wait for 2 seconds
            running = False
            continue

        screen.fill(PATH_COLOR)
        draw_maze(maze)
        draw_player(player_x, player_y)
        pygame.display.flip()

        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
