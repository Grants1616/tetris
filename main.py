import pygame
from constants import *
from shape import *


def main():
    print("Hello from tetris!")
    print(f"starting tetris with pygame version: {pygame.version.ver}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    shape = Shape(SCREEN_WIDTH / 2, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        shape.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
