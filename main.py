import pygame
from map import *
import sprite
import colours
from sprite import *


scroll = 0

screen = pygame.display.set_mode((900, 323))

pygame.display.set_caption("Industrial")
logo = pygame.image.load("Graphics/logo.png")
pygame.display.set_icon(logo)

level1 = Level(tile_data, screen)
player = Player((50, 170), screen)

bg_images = []
for i in range(1, 6):
    bg_image = pygame.image.load(f"Graphics/{i}.png")
    bg_images.append(bg_image)
    bg_width = bg_images[0].get_width()


def draw_bg():
    for x in range(5):
        speed = 0.3
        for bg in bg_images:
            screen.blit(bg, ((x * bg_width) - scroll * speed, 0))
            speed += 0.3


running = True
while running:
    index = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_bg()
    level1.run()
    player.load()
    player.gravity(1)
    player.update()

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and scroll > 0:
        scroll -= 1
    if key[pygame.K_RIGHT] and scroll < 3000:
        scroll += 1
        index += 1

    pygame.display.update()
