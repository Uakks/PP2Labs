import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
play = True

pygame.mixer.music.load('/Users/uakks/Desktop/Emin.mp3')
pygame.mixer.music.queue('/Users/uakks/Music/Music/Media.localized/Apple Music/Eminem/The Eminem Show/10 Without Me.m4p')
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
