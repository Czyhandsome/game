import pygame

from collapse.RedFace import RedFace
from collapse.Sony import Sony


if __name__ == '__main__':
    # Init main frame
    width, height = 640, 480
    pygame.init()
    screen = pygame.display.set_mode([width, height])
    screen.fill([255, 255, 255])

    # Get a clock
    clock = pygame.time.Clock()

    # Print red face
    red_face = RedFace([20, 20], width, height)
    screen.blit(red_face.image, red_face.rect)
    pygame.display.flip()

    # Print sony
    sony = Sony([220, 20], width, height)
    screen.blit(sony.image, sony.rect)
    pygame.display.flip()

    # Keep the window alive...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(120)
        print(clock.get_fps())
        screen.fill([255, 255, 255])
        # Move red_face
        red_face.move()
        screen.blit(red_face.image, red_face.rect)
        pygame.display.flip()
        # Move sony
        sony.move()
        screen.blit(sony.image, sony.rect)
        pygame.display.flip()
        # Collapse test
        group = pygame.sprite.Group()
        group.add(sony)
        if pygame.sprite.spritecollide(red_face, group, False):
            sony.revert()
    pygame.quit()
