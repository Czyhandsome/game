import random

import pygame
from pygame.color import THECOLORS

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill([255, 255, 255])

    for i in range(100):
        width = random.randint(0, 250)
        height = random.randint(0, 100)
        top = random.randint(0, 400)
        left = random.randint(0, 500)
        pygame.draw.rect(screen, THECOLORS["black"], [left, top, width, height], 1)

    pygame.display.flip()

    # Keep the screen alive ...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
