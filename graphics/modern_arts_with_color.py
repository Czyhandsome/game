import random

import pygame

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill([255, 255, 255])

    for i in range(100):
        width = random.randint(0, 250)
        height = random.randint(0, 100)
        top = random.randint(0, 400)
        left = random.randint(0, 500)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        pygame.draw.rect(screen, [r, g, b], [left, top, width, height], 1)

    pygame.display.flip()

    # Keep the screen alive ...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
