import pygame

if __name__ == '__main__':
    # Create a pygame window
    pygame.init()
    width = 640
    height = 400
    screen = pygame.display.set_mode([width, height])
    screen.fill([255, 255, 255])

    #########################
    # Actual drawing here...
    #########################
    pygame.draw.rect(screen, [0, 0, 255], [200, 100, 250, 250], 1)
    pygame.display.flip()

    # Keep the window alive...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
