import random
import sys

import pygame
from map import *
import sprite
import colours
from sprite import *
from pygame import mixer
from part2 import *
from button import Button

pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()

scroll = 0
scroll2 = 0
collected = 0

screen = pygame.display.set_mode((1300, 646))

pygame.display.set_caption("Industrial")
logo = pygame.image.load("Graphics/logo.png")
pygame.display.set_icon(logo)

portals = pygame.sprite.Group()
portal = Portal(300, 300, screen)
portals.add(portal)

level1 = Level(tile_data, screen)
player = Player((70, 300), screen, level1.tiles, portals, level1.flasks)
burn_sound = pygame.mixer.Sound('burn.mp3')
burn_sound.set_volume(0.2)

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


def draw_bg2():
    for x in range(5):
        speed = 0.3
        for bg in bg_images:
            screen.blit(bg, ((x * bg_width) - scroll2 * speed, 0))
            speed += 1


mixer.music.load("backgroundmusic.wav")
pygame.mixer.music.set_volume(0)
mixer.music.play(-1)

pygame.font.init()
fontObj = pygame.font.Font('Graphics/FutureMillennium.ttf', 20)
render = fontObj.render('Flasks Collected: ' + str(collected), True, (0, 0, 0), )
rect = render.get_rect()
rect.center = (150, 30)

font_b = pygame.font.Font('Graphics/FutureMillennium.ttf', 30)

running = True
screen_state = "Intro"
current_sprite = 0

while running:

    if screen_state == "Intro":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(colours.white)
        burn_sound.play()

        iframes = []

        for iframe in range(38):
            iframes.append(pygame.image.load('Intro/frame-{}.jpg'.format(iframe + 1)))

        current_sprite += 0.25
        if current_sprite >= len(iframes):
            current_sprite = 0
            screen_state = "Menu"
        iimage = iframes[int(current_sprite)]
        iimage = pygame.transform.scale(iimage, (646, 646))

        screen.blit(iimage, (327, 0))

    if screen_state == "Loading":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(colours.black)
        lframes = []

        for lframe in range(38):
            lframes.append(pygame.image.load('Loading/frame-{}.jpg'.format(lframe + 1)))

        current_sprite += 1
        if current_sprite >= len(lframes):
            current_sprite = 0
            screen_state = "Play"
        limage = lframes[int(current_sprite)]
        limage = pygame.transform.scale(limage, (1148, 646))

        screen.blit(limage, (100, 0))

    if screen_state == "Menu":
        screen.fill(colours.black)
        pygame.mixer.music.set_volume(0.2)
        draw_bg2()
        scroll2 += 1
        if scroll2 > 1100:
            scroll2 = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        c_pos = pygame.mouse.get_pos()
        play_b = Button(image=pygame.image.load("Graphics/button.png"), pos=(640, 250),
                        text_input="PLAY", font=font_b, base_color="#3246a8", hovering_color="White")
        options_b = Button(image=pygame.image.load("Graphics/button.png"), pos=(640, 400),
                           text_input="OPTIONS", font=font_b, base_color="#3246a8", hovering_color="White")
        quit_b = Button(image=pygame.image.load("Graphics/button.png"), pos=(640, 550),
                        text_input="QUIT", font=font_b, base_color="#3246a8", hovering_color="White")
        for button in [play_b, options_b, quit_b]:
            button.changeColor(c_pos)
            button.update(screen)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_b.checkForInput(c_pos):
                screen_state = "Loading"
            if quit_b.checkForInput(c_pos):
                pygame.quit()
                sys.exit()

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
        respawn = fontObj.render("Press R to Respawn", False, (255, 255, 255))
        select = random.randint(1, 2)
        if select == 1:
            screen.blit(respawn, (570, 600))

        if pygame.key.get_pressed()[pygame.K_r]:
            screen_state = "Loading"

    pygame.display.update()
