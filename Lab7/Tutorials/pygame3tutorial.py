import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
play = True

pygame.mixer.music.load('/Users/uakks/Desktop/Music_em/Emin.mp3')
pygame.mixer.music.play(0)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            play = not play

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.mixer.music.stop()

        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    if play:
        pygame.mixer.music.unpause()
    else:
        pygame.mixer.music.pause()
