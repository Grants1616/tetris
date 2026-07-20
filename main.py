import pygame
from constants import *


def main():
    print("Hello from tetris!")
    print(f"starting tetris with pygame version: {pygame.version.ver}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.draw.polygon(screen, "white", [(40, 30), (70, 30), (70, 100)], 1)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
