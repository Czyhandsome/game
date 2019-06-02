import random

import pygame

if __name__ == '__main__':
    # Create a pygame window
    pygame.init()
    width = 640
    height = 480
    screen = pygame.display.set_mode([width, height])
    screen.fill([255, 255, 255])

    #########################
    # Actual drawing here...
    #########################
    for i in range(100):
        x = random.randint(0, width)
        y = random.randint(0, height)
        radius = random.randint(0, min(x, y))
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        pygame.draw.circle(screen, [r, g, b], [x, y], radius, min(1, radius))

    pygame.display.flip()

    # Keep the window alive...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
