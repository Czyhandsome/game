import pygame

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill([255, 255, 255])
    pygame.draw.circle(screen, [255, 0, 0], [320, 240], 30, 0)
    pygame.display.flip()

    # Keep the screen alive ...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
