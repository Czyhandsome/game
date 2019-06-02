import pygame

if __name__ == '__main__':
    # Init the window
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    screen.fill([255, 255, 255])

    # Actual draw here ...
    read_face = pygame.image.load("red_face.jpg")
    screen.blit(read_face, [50, 50])

    # Flip and show
    pygame.display.flip()

    # Other drawing here...
    pygame.time.delay(500)
    screen.blit(read_face, [150, 50])
    pygame.draw.rect(screen, [255, 255, 255], [50, 50, 100, 90], 0)

    # Flip and show
    pygame.display.flip()

    # Keep the screen alive ...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
