import pygame
import colours
import map
import main


class Player(pygame.sprite.Sprite):

    def __init__(self, ppos, surface,level):
        pygame.sprite.Sprite.__init__(self)
        self.level = level
        self.sprites = pygame.sprite.Group()
        self.surface = surface
        self.state = "idle"
        self.stage = 1
        self.x = ppos[0]
        self.y = ppos[1]
        self.image = pygame.image.load("Graphics/cyborg {}/{}{}.png".format(self.state, self.state, self.stage))
        self.image.set_colorkey(colours.white)
        self.rect = self.image.get_rect(topleft=ppos)
        self.sprites.add(self)

    def animate(self):
        cycle = [1, 2, 3, 4]
        for num in cycle:
            self.stage = num

    def gravity(self, strength):
        super().__init__()
        self.strength = strength
        self.y += self.strength

    def collision(self):
        touch = pygame.sprite.spritecollideany(self, self.level)
        if touch:
            print("ok")

    def load(self):
        self.collision()
        self.surface.blit(self.image, (self.x, self.y))









