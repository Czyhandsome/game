import pygame
from pygame.color import THECOLORS

if __name__ == '__main__':
    # Init pygame window
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill([255, 255, 255])

    # Compute the points...
    dots = [[221, 432], [225, 331], [133, 342], [141, 310],
            [51, 230], [74, 217], [58, 153], [114, 164],
            [123, 135], [176, 190], [159, 77], [193, 93],
            [230, 28], [267, 93], [310, 77], [284, 190],
            [327, 135], [336, 164], [402, 153], [386, 217],
            [409, 230], [319, 310], [327, 342], [233, 331],
            [237, 432]]

    # Actual drawing is here...
    pygame.draw.lines(screen, THECOLORS["black"], True, dots, 2)

    # Flip and show
    pygame.display.flip()

    # Keep the screen alive ...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
