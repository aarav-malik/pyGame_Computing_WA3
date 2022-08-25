import pygame
import colours
import time
import random


class Player(pygame.sprite.Sprite):

    def __init__(self, ppos, surface, level):
        pygame.sprite.Sprite.__init__(self)
        self.ppos = ppos
        self.inair = False
        self.level = level
        self.sprites = pygame.sprite.Group()
        self.surface = surface
        self.state = "move"
        self.stage = 1
        self.animate()
        self.x = ppos[0]
        self.y = ppos[1]
        self.sprites.add(self)

    def animate(self):
        self.image = pygame.image.load("Graphics/robot {}/{}{}.png".format(self.state, self.state, self.stage))
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(topleft=self.ppos)
        self.image.set_colorkey(colours.green)

    def gravity(self, strength):
        self.strength = strength
        self.y += self.strength

    def collision(self):
        touch = pygame.sprite.spritecollide(self, self.level,False)
        if touch:
            self.inair = False
        else:
            self.inair = True
        return touch

    def jump(self):
        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.inair:
            self.y -= 100
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            time.sleep(0.001)
            self.stage = random.randint(1, 8)

    def update(self):
        self.jump()
        self.animate()
        self.surface.blit(self.image, (self.x, self.y))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        pygame.draw.rect(self.surface, colours.white, self.rect, 2)
