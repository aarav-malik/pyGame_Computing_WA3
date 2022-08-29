import pygame


class Flask(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__()
        self.x = x
        self.y = y
        self.activated = False
        self.screen = screen
        self.sprites = []
        self.sprites.append(pygame.image.load('Graphics/flask/frame_01.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_02.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_03.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_04.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_05.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_06.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_07.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_09.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_10.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_11.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_12.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_13.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_14.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_15.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_16.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_17.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_18.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_19.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_20.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_21.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_22.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_23.png'))
        self.sprites.append(pygame.image.load('Graphics/flask/frame_24.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect(bottomleft=(self.x, self.y))

    def update(self, speed):
        self.activated = True

        if self.activated:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.activated = False

        self.image = self.sprites[int(self.current_sprite)]








