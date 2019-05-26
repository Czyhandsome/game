import pygame
from pygame.color import THECOLORS

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill([255, 255, 255])
    pygame.draw.circle(screen, THECOLORS["red"], [100, 100], 30, 0)
    pygame.display.flip()

    # Keep the screen alive ...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
