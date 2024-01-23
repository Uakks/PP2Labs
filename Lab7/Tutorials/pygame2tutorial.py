import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

surface = pygame.Surface((100, 100))
image = pygame.image.load('/Users/uakks/Downloads/6.png')

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    screen.fill((255, 255, 255))
    screen.blit(image, (20, 20))

    pygame.display.flip()
