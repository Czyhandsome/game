import pygame


class MyFaceClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def move(self):
        self.rect = self.rect.move(100, 100)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([640, 480])
    screen.fill([255, 255, 255])

    my_face = MyFaceClass("red_face.jpg", [20, 20])
    screen.blit(my_face.image, my_face.rect)
    pygame.display.flip()

    # Keep the window alive...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.time.delay(1000)
        my_face.move()
        screen.fill([255, 255, 255])
        screen.blit(my_face.image, my_face.rect)
        pygame.display.flip()
    pygame.quit()
