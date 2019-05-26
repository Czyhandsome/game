import math

import pygame

if __name__ == '__main__':
    # Init pygame window
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill([255, 255, 255])

    # Actual drawing is here...
    for x in range(0, 640):
        y = int(math.sin(x / 640.0 * 4 * math.pi) * 200 + 240)
        screen.set_at([x, y], [0, 0, 0])

    # Flip and show
    pygame.display.flip()

    # Keep the screen alive ...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
