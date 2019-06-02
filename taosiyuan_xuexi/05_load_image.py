import pygame

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([640, 480])
    screen.fill([255, 255, 255])

    #########################
    # Actual drawing here...
    #########################
    red_face = pygame.image.load("red_face.jpg")
    screen.blit(red_face, [320 - 95 // 2, 240 - 76 // 2])

    pygame.display.flip()

    # Keep the window alive...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
