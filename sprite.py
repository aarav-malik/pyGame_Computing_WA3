import pygame
import colours
import time
import random


class Player(pygame.sprite.Sprite):

    def __init__(self, ppos, surface, level, portals, flasks, earths):
        pygame.sprite.Sprite.__init__(self)
        self.ppos = ppos
        self.inair = False
        self.collideright = False
        self.level = level
        self.flasks = flasks
        self.portal = portals
        self.earth = earths
        self.sprites = pygame.sprite.Group()
        self.surface = surface
        self.state = "move"
        self.stage = 1
        self.animate()
        self.x = ppos[0]
        self.y = ppos[1]
        self.sprites.add(self)

    def stage(self, stage):
        self.stage = stage

    def animate(self):
        super().__init__()
        self.image = pygame.image.load("Graphics/robot {}/{}{}.png".format(self.state, self.state, self.stage))
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_bounding_rect()
        self.image.set_colorkey(colours.green)

    def gravity(self, strength):
        self.strength = strength
        self.y += self.strength

    def collision(self):
        touch = pygame.sprite.spritecollide(self, self.level, False)
        if touch:
            self.inair = False
        else:
            self.inair = True

        if len(touch) >= 3:
            return "side"
        return touch

    def portalcollision(self):
        enter = pygame.sprite.spritecollideany(self, self.portal)
        return enter

    def flaskcollection(self):
        collected = pygame.sprite.spritecollide(self, self.flasks, True)
        return collected

    def jump(self):
        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.inair:
            self.y -= 100
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            time.sleep(0.001)
            self.stage = random.randint(1, 8)

    def end(self):
        return self.y < 0 or self.y > 646

    def finish(self):
        return pygame.sprite.spritecollide(self, self.earth, False)

    def reset(self):
        self.x = 70
        self.y = 300

    def update(self):
        self.jump()
        self.animate()
        self.surface.blit(self.image, (self.x, self.y))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        # pygame.draw.rect(self.surface, colours.white, self.rect, 2)
