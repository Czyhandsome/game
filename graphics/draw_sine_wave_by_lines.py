import math

import pygame
from pygame.color import THECOLORS

if __name__ == '__main__':
    # Init pygame window
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill([255, 255, 255])

    # Compute the points...
    plotPoints = []
    for x in range(0, 640):
        y = int(math.sin(x / 640.0 * 4 * math.pi) * 200 + 240)
        plotPoints.append([x, y])

    # Actual drawing is here...
    pygame.draw.lines(screen, THECOLORS["black"], False, plotPoints, 2)

    # Flip and show
    pygame.display.flip()

    # Keep the screen alive ...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
