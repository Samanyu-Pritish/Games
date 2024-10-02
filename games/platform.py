import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game with Moving Platforms")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 0)

# Game settings
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_SPEED = 5
JUMP_STRENGTH = 15
GRAVITY = 1
STATIC_PLATFORM_WIDTH, STATIC_PLATFORM_HEIGHT = 100, 20
MOVING_PLATFORM_WIDTH, MOVING_PLATFORM_HEIGHT = 100, 20
MOVING_PLATFORM_SPEED = 2
MOVING_PLATFORM_RANGE = 200  # Range of movement for moving platforms

# Player class
class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - PLAYER_HEIGHT - STATIC_PLATFORM_HEIGHT
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.speed = PLAYER_SPEED
        self.velocity_y = 0
        self.jumping = False
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self):
        SCREEN.blit(self.image, self.rect.topleft)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        self.velocity_y += GRAVITY
        self.y += self.velocity_y

        self.rect.topleft = (self.x, self.y)
        self.rect.clamp_ip(SCREEN.get_rect())

    def jump(self):
        if not self.jumping:
            self.velocity_y = -JUMP_STRENGTH
            self.jumping = True

    def land(self):
        self.velocity_y = 0
        self.jumping = False

# Static Platform class
class StaticPlatform:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, STATIC_PLATFORM_WIDTH, STATIC_PLATFORM_HEIGHT)

    def draw(self):
        pygame.draw.rect(SCREEN, GREEN, self.rect)

# Moving Platform class
class MovingPlatform:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, MOVING_PLATFORM_WIDTH, MOVING_PLATFORM_HEIGHT)
        self.start_x = x
        self.direction = 1
        self.range = MOVING_PLATFORM_RANGE

    def move(self):
        self.rect.x += MOVING_PLATFORM_SPEED * self.direction
        if self.rect.left < self.start_x - self.range or self.rect.right > self.start_x + self.range:
            self.direction *= -1

    def draw(self):
        pygame.draw.rect(SCREEN, GREEN, self.rect)

def main():
    player = Player()
    static_platforms = [
        StaticPlatform(50, HEIGHT - 50),
        StaticPlatform(200, HEIGHT - 150),
        StaticPlatform(400, HEIGHT - 250),
        StaticPlatform(600, HEIGHT - 350)
    ]
    moving_platforms = [
        MovingPlatform(100, HEIGHT - 450),
        MovingPlatform(300, HEIGHT - 550),
        MovingPlatform(500, HEIGHT - 650),
        MovingPlatform(700, HEIGHT - 750)
    ]
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.move(keys)

        # Update moving platforms
        for platform in moving_platforms:
            platform.move()

        # Collision detection with static platforms
        player_on_platform = False
        for platform in static_platforms:
            if player.rect.colliderect(platform.rect) and player.velocity_y > 0:
                player.y = platform.rect.top - player.height
                player.land()
                player_on_platform = True

        # Collision detection with moving platforms
        for platform in moving_platforms:
            if player.rect.colliderect(platform.rect) and player.velocity_y > 0:
                player.y = platform.rect.top - player.height
                player.land()
                player.x += platform.rect.x - platform.rect.x
                player_on_platform = True

        if not player_on_platform:
            if player.y + player.height > HEIGHT:
                player.y = HEIGHT - player.height
                player.land()

        # Handle jumping
        if keys[pygame.K_SPACE] and not player.jumping:
            player.jump()

        SCREEN.fill(BLUE)
        player.draw()
        for platform in static_platforms:
            platform.draw()
        for platform in moving_platforms:
            platform.draw()

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
 # type: ignore