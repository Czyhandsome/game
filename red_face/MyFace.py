import pygame


class MyFace(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

        self._x = 1
        self._y = 0

    def move(self):
        self.rect = self.rect.move(self._x * 100, self._y * 100)
        self._next_x_y()

    def _next_x_y(self):
        if (self._x, self._y) == (1, 0):
            self._x, self._y = 0, 1
        elif (self._x, self._y) == (0, 1):
            self._x, self._y = -1, 0
        elif (self._x, self._y) == (-1, 0):
            self._x, self._y = 0, -1
        else:
            self._x, self._y = 1, 0


if __name__ == '__main__':
    pygame.init()
    width = 640
    height = 480
    screen = pygame.display.set_mode([width, height])
    screen.fill([255, 255, 255])

    red_face = MyFace("red_face.jpg", [20, 20])
    screen.blit(red_face.image, red_face.rect)
    pygame.display.flip()

    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        pygame.time.delay(100)
        screen.fill([255, 255, 255])
        red_face.move()
        screen.blit(red_face.image, red_face.rect)
        pygame.display.flip()
    pygame.quit()
