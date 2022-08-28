import pygame
import colours
import time
import random


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
        self.rect.inflate_ip(-30, 5)
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
        # pygame.draw.rect(self.screen, colours.white, self.rect, 2)


class Ship(pygame.sprite.Sprite):
    def __init__(self, ppos, surface, level, portals):
        pygame.sprite.Sprite.__init__(self)
        self.ppos = ppos
        self.inair = False
        self.collideright = False
        self.level = level
        self.portal = portals
        self.sprites = pygame.sprite.Group()
        self.surface = surface
        self.stage = 1
        self.animate()
        self.x = ppos[0]
        self.y = ppos[1]
        self.sprites.add(self)

    def stage(self, stage):
        self.stage = stage

    def animate(self):
        self.image = pygame.image.load("Graphics/ship/{}.png".format(self.stage))
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect(topleft=self.ppos)
        self.image.set_colorkey(colours.green)

    def gravity(self, strength):
        self.strength = strength
        self.y += self.strength

    def collision(self):
        touch = pygame.sprite.spritecollide(self, self.level, False)
        return touch

    def portalcollision(self):
        enter = pygame.sprite.spritecollideany(self, self.portal)
        if enter:
            print(1)
        return enter

    def jump(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.y -= 50
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            time.sleep(0.001)
            self.stage = random.randint(1, 6)

    def update(self):
        self.jump()
        self.animate()
        self.surface.blit(self.image, (self.x, self.y))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        # pygame.draw.rect(self.surface, colours.white, self.rect, 2)
