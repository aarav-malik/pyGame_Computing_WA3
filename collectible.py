import pygame


class Flask(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.activated = False
        self.screen = screen
        self.sprites = []
        for x in range(25):
            self.sprites.append(pygame.image.load('Graphics/flask/frame_{}.png'.format(x)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect(bottomleft=(self.x, self.y))

    def update(self, speed, x_shift):
        self.activated = True

        if self.activated:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.activated = False

        self.image = self.sprites[int(self.current_sprite)]
        self.rect.x += x_shift








