import pygame


class Face(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    # def move(self):
    #     if self.rect.left <= screen.get_rect().left or \
    #             self.rect.right >= screen.get_rect().right:
    #         self.speed[0] = - self.speed[0]
    #     newpos = self.rect.move(self.speed)
    #     self.rect = newpos

    def move_up(self):
        self.rect.top -= 50
        if self.rect.top <= 0:
            self.rect.top = 0

    def move_down(self):
        self.rect.bottom += 50
        if self.rect.bottom >= 480:
            self.rect.bottom = 480

    def move_left(self):
        self.rect.left -= 50
        if self.rect.left <= 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.right += 50
        if self.rect.right >= 640:
            self.rect.right = 640


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([640, 480])
    background = pygame.Surface(screen.get_size())
    background.fill([255, 255, 255])
    clock = pygame.time.Clock()

    my_face = Face('red_face.jpg', [10, 0], [20, 20])
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    my_face.move_up()
                elif event.key == pygame.K_DOWN:
                    my_face.move_down()
                elif event.key == pygame.K_LEFT:
                    my_face.move_right()
                elif event.key == pygame.K_RIGHT:
                    my_face.move_left()
        clock.tick(60)
        screen.blit(background, (0, 0))
        # my_face.move()
        screen.blit(my_face.image, my_face.rect)
        pygame.display.flip()
    pygame.quit()
