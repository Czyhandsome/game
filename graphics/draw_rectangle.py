import pygame
from pygame.color import THECOLORS

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill([255, 255, 255])
    pygame.draw.rect(screen, THECOLORS["blue"], [250, 150, 300, 200], 2)
    pygame.display.flip()

    # Keep the screen alive ...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
