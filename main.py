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
pygame.font.init()

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

earths = pygame.sprite.Group()
earth = Earth(300, 300, screen)
earths.add(earth)

level1 = Level(tile_data, screen)
player = Player((70, 300), screen, level1.tiles, portals, level1.flasks, earths)

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


def font_sizer(size):
    return pygame.font.Font('Graphics/FutureMillennium.ttf', size)


running = True
screen_state = "Intro"
current_sprite = 0
icurrent_sprite = 0
lgcurrent_sprite = 0
lcurrent_sprite = 0

while running:

    if screen_state == "Intro":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(colours.white)

        iframes = []

        for iframe in range(38):
            iframes.append(pygame.image.load('Intro/frame-{}.jpg'.format(iframe + 1)))

        icurrent_sprite += 0.25
        if icurrent_sprite >= len(iframes):
            icurrent_sprite = 0
            screen_state = "Menu"
        iimage = iframes[int(icurrent_sprite)]
        iimage = pygame.transform.scale(iimage, (646, 646))

        screen.blit(iimage, (327, 0))

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
        play_b = Button(image=pygame.image.load("Graphics/button.png"), pos=(640, 400),
                        text_input="PLAY", font=font_sizer(30), base_color="#3246a8", hovering_color="White")
        quit_b = Button(image=pygame.image.load("Graphics/button.png"), pos=(640, 550),
                        text_input="QUIT", font=font_sizer(30), base_color="#3246a8", hovering_color="White")
        for button in [play_b, quit_b]:
            button.changeColor(c_pos)
            button.update(screen)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_b.checkForInput(c_pos):
                screen_state = "Loading"
            if quit_b.checkForInput(c_pos):
                pygame.quit()
                sys.exit()

        lgframes = []

        for lgframe in range(150):
            lgframes.append(pygame.image.load('Logo/unscreen-{}.png'.format(lgframe + 1)))

        lgcurrent_sprite += 1
        if int(lgcurrent_sprite) >= len(lgframes):
            lgcurrent_sprite = 0
        lgimage = lgframes[int(lgcurrent_sprite)]
        lgimage = lgimage.convert_alpha()
        lgimage.set_colorkey((253, 255, 252))
        lgimage = pygame.transform.scale(lgimage, (586, 356))

        screen.blit(lgimage, (350, 0))

    if screen_state == "Loading":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(colours.black)
        lframes = []

        for lframe in range(38):
            lframes.append(pygame.image.load('Loading/frame-{}.jpg'.format(lframe + 1)))

        lcurrent_sprite += 1
        if lcurrent_sprite >= len(lframes):
            lcurrent_sprite = 0
            screen_state = "Play"
        limage = lframes[int(lcurrent_sprite)]
        limage = pygame.transform.scale(limage, (1148, 646))

        screen.blit(limage, (100, 0))

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
                player = Ship((300, 300), screen, level1.tiles, portals, level1.flasks, earths)
                player.gravity(3)
        print(scroll)
        if scroll > 750:
            earths.draw(screen)
            earths.update(0.25)
            earth.run()

        if player.flaskcollection():
            collected += 1
        render = font_sizer(20).render('Flasks Collected: ' + str(collected), True, (0, 0, 0), )
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

        # if player.finish():
        #     screen_state = "Finish"
        #     screen.fill(colours.black)
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             running = False

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and scroll > 0:
            scroll -= 0.5
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
        respawn = font_sizer(20).render("Press R to Respawn", False, (255, 255, 255))
        select = random.randint(1, 2)
        if select == 1:
            screen.blit(respawn, (570, 600))

        if pygame.key.get_pressed()[pygame.K_r]:
            screen_state = "Loading"

    pygame.display.update()
