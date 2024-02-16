import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Ball")
done = False
clock = pygame.time.Clock()

red = (255, 0, 0)
white = (255, 255, 255)
x, y = screen.get_width() / 2, screen.get_height() / 2
radius = 25

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y -= 20
            if y < radius:
                y = radius

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y += 20
            if y > screen.get_height()-radius:
                y = screen.get_height()-radius

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= 20
            if x < radius:
                x = radius

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += 20
            if x > screen.get_width()-radius:
                x = screen.get_width()-radius

    screen.fill(white)
    pygame.draw.circle(screen, red, (x, y), radius)
    pygame.display.flip()
