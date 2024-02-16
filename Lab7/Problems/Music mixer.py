# Create music player with keyboard controller.
# You have to be able to press keyboard: play, stop, next and previous as some keys.
# Player has to react to the given command appropriately.

import pygame
import os

pygame.init()
screen = pygame.display.set_mode((1000, 700))
done = False
muted = False
play = True
font = pygame.font.SysFont("comicsansms", 28)
center = (screen.get_width() / 2, screen.get_height() / 2)
black = (0, 0, 0)
white = (255, 255, 255)

list_of_music = ["../Music_em/"
                 + f for f in os.listdir("../Music_em") if f[-3:] == "mp3"]
names_of_music = []
for i in list_of_music:
    names_of_music.append(i.split("/")[-1][0:-4])
print(names_of_music)

pygame.mixer.music.load(list_of_music[0])
pygame.mixer.music.play()

i = 0
volume = pygame.mixer.music.get_volume()
prev = 0

while not done:
    muted_volume = 0

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.mixer.music.stop()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pygame.mixer.music.play()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            play = not play

        if event.type == pygame.KEYDOWN and event.key == pygame.K_EQUALS:
            volume += 0.05
            if volume >= 1:
                volume = 1
            pygame.mixer.music.set_volume(volume)
            print(volume)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_MINUS:
            volume -= 0.05
            if volume <= 0:
                volume = 0
            pygame.mixer.music.set_volume(volume)
            print(volume)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if pygame.mixer.music.get_pos() < 5000:
                i -= 1
                if i == -1:
                    i = len(list_of_music)-1
                pygame.mixer.music.queue(list_of_music[i], loops=0)
                pygame.mixer.music.set_pos(1000000)
            else:
                pygame.mixer.music.rewind()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            i += 1
            if i == len(list_of_music):
                i = 0
            pygame.mixer.music.queue(list_of_music[i], loops=0)
            pygame.mixer.music.set_pos(1000000)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            pos = pygame.mixer.music.get_pos() + prev + 5000
            pygame.mixer.music.play(0, pos / 1000)
            prev = pos

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            pos = pygame.mixer.music.get_pos() + prev - 5000
            pygame.mixer.music.play(0, pos / 1000)
            prev = pos

        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            muted = not muted

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
            pygame.quit()

    screen.fill(black)
    name_of_music = font.render(f"{names_of_music[i]}", True, white)
    screen.blit(name_of_music, (screen.get_width()/4, screen.get_height() / 2 - 25))
    if muted:
        pygame.mixer.music.set_volume(muted_volume)
    else:
        pygame.mixer.music.set_volume(volume)

    if play:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()

    pygame.display.flip()
