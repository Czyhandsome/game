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

    # Keep the window alive...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
