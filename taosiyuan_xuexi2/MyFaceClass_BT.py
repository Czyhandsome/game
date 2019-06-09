import random

import pygame


class MyFaceClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.sx = 10
        self.sy = 10

    def move(self):
        self.rect = self.rect.move((self.sx, self.sy))
        self._change_speed()

    def _change_speed(self):
        self.sx, self.sy = self._raise(self.sx), self._raise(self.sy)

        if self.rect.left < 0 or self.rect.right > width:
            self.sx = -self.sx

        if self.rect.top < 0 or self.rect.bottom > height:
            self.sy = -self.sy

    @staticmethod
    def _raise(x):
        ratio = random.random() * 2 - 1
        x = int(x * ratio)
        return x


if __name__ == '__main__':
    width = 480
    height = 640
    size = (width, height)
    screen = pygame.display.set_mode(size)
    screen.fill([255, 255, 255])
    img_file = "red_face.jpg"
    faces = []
    num = 3
    for row in range(0, num):
        for column in range(0, num):
            location = [column * 180 + 10, row * 180 + 10]
            face = MyFaceClass(img_file, location)
            faces.append(face)
    for face in faces:
        screen.blit(face.image, face.rect)
    pygame.display.flip()

    # Keep the window alive...
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.time.delay(20)
        screen.fill([255, 255, 255])
        for face in faces:
            face.move()
            screen.blit(face.image, face.rect)
        pygame.display.flip()

    pygame.quit()
