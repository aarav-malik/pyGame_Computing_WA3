import pygame
import colours


class Portal(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, screen):
        super().__init__()
        self.activated = False
        self.screen = screen
        self.sprites = []
        self.sprites.append(pygame.image.load('Graphics/portal/frame_1.png'))
        self.sprites.append(pygame.image.load('Graphics/portal/frame_2.png'))
        self.sprites.append(pygame.image.load('Graphics/portal/frame_3.png'))
        self.sprites.append(pygame.image.load('Graphics/portal/frame_4.png'))
        self.sprites.append(pygame.image.load('Graphics/portal/frame_5.png'))
        self.sprites.append(pygame.image.load('Graphics/portal/frame_6.png'))
        self.sprites.append(pygame.image.load('Graphics/portal/frame_7.png'))
        self.sprites.append(pygame.image.load('Graphics/portal/frame_8.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.x = pos_x
        self.y = pos_y

    def run(self):
        self.activated = True

    def update(self, speed):

        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.x -= 10
        self.rect.topleft = [self.x, self.y]

        if self.activated:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.activated = False

        self.image = self.sprites[int(self.current_sprite)]
        pygame.draw.rect(self.screen, colours.white, self.rect, 2)

