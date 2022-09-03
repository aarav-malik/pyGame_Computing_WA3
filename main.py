import pygame
from map import *
import sprite
import colours
from sprite import *
from pygame.locals import *
from pygame import mixer
from part2 import *

# from pyvidplayer import Video

scroll = 0
collected = 0

screen = pygame.display.set_mode((1300, 646))

pygame.display.set_caption("Industrial")
logo = pygame.image.load("Graphics/logo.png")
pygame.display.set_icon(logo)

portals = pygame.sprite.Group()
portal = Portal(300, 300, screen)
portals.add(portal)

# intro = Video("intro.mp4")

level1 = Level(tile_data, screen)
player = Player((70, 300), screen, level1.tiles, portals, level1.flasks)

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
            speed += 1


mixer.init()
mixer.music.load("backgroundmusic.wav")
pygame.mixer.music.set_volume(0.2)
mixer.music.play(-1)

pygame.font.init()
fontObj = pygame.font.Font('Graphics/FutureMillennium.ttf', 20)
render = fontObj.render('Flasks Collected: ' + str(collected), True, (0, 0, 0), )
rect = render.get_rect()
rect.center = (150, 30)

running = True
screen_state = "Play"
current_sprite = 0

while running:
    if screen_state == "Play":
        index = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_bg()
        level1.run(player.collision())

        if scroll > 360:
            portals.draw(screen)
            portals.update(0.25)
            portal.run()
            if player.portalcollision():
                player = Ship((300, 300), screen, level1.tiles, portals, level1.flasks)
                player.gravity(3)

        if player.flaskcollection():
            collected += 1
        render = fontObj.render('Flasks Collected: ' + str(collected), True, (0, 0, 0), )
        rect = render.get_rect()
        rect.center = (150, 30)
        screen.blit(render, rect)

        if player.collision():
            # print("colliding")
            player.gravity(0)
        else:
            # print("not colliding")
            player.gravity(10)
        player.update()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and scroll > 0:
            scroll -= 1
        if key[pygame.K_RIGHT] and scroll < 3000 and player.collision() != "side":
            scroll += 1
            index += 1

        if player.end():
            screen_state = "End"

    if screen_state == "Intro":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # intro.draw(screen, (0, 0))

    if screen_state == "End":
        screen.fill(colours.black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        frames = []

        for frame in range(37):
            frames.append(pygame.image.load('Graphics/Game Over/frame_{}.png'.format(frame)))

        current_sprite += 1
        if int(current_sprite) >= len(frames):
            current_sprite = 0
        image = frames[int(current_sprite)]
        image = pygame.transform.scale(image, (1148, 646))

        screen.blit(image, (100, 0))

        #if pygame.key.get_pressed()[pygame.K_r]:
            #player = Player((70, 300), screen, level1.tiles, portals, level1.flasks)
            #portal = Portal(300, 300, screen)
            #level1 = Level(tile_data, screen)

            #screen_state = "Play"

    pygame.display.update()
