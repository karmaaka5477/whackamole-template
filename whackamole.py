import pygame
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 512
GRID_SIZE = 32

# colors
GRID_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (144, 238, 144)

def draw_grid(screen):
    """Draws a 20x16 grid on the screen."""
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))


def move_mole():
    """Returns a new random position for the mole aligned with the grid."""
    x = random.randrange(0, SCREEN_WIDTH, GRID_SIZE)
    y = random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)
    return x, y

def main():
    try:
        pygame.init()
        # drawing mole
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
