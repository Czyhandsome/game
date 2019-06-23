import pygame


class Sony(pygame.sprite.Sprite):
    def __init__(self, location, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            "/Users/caoziyu/PycharmProjects/github/game/collapse/resources/sony.png")
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.width = width
        self.height = height
        self.x = 10
        self.y = 10

    def move(self):
        self.rect = self.rect.move(self.x, self.y)
        if self.rect.left <= 0 or self.rect.right > self.width:
            self.x = -self.x
        if self.rect.top <= 0 or self.rect.bottom >= self.height:
            self.y = -self.y

    def revert(self):
        self.x = -self.x
        self.y = -self.y
