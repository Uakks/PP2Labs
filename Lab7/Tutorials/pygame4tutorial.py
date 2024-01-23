import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(10, 10, 100, 100), 1)
    pygame.draw.circle(screen, (100, 100, 100), (120, 120), 100, 1)
    pygame.draw.polygon(screen, (100, 100, 100), ((120, 120), (140, 140), (140, 160), (120, 180)), 1)
    pygame.display.flip()