import pygame
import math
import datetime

pygame.init()
screen = pygame.display.set_mode((1000, 700))
done = False

clock = pygame.time.Clock()

radius = 200
angle = 0
surface = pygame.Surface((400, 300))
center = (screen.get_width() / 2, screen.get_height() / 2)

font = pygame.font.SysFont("comicsansms", 16)

white = (255, 255, 255)
black = (0, 0, 0)


def degrees(dots, r):
    y = math.cos(math.pi * (dots + 1) / 6) * r
    x = math.sin(math.pi * (dots + 1) / 6) * r
    return x + screen.get_width() / 2, -(y - screen.get_height() / 2)


# junk = 0

while not done:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    date1 = datetime.datetime.now()
    time_now = date1.strftime("%H:%M:%S")
    exact_time = time_now.split(":")
    # if exact_time != junk:
    #     print(exact_time)
    # junk = exact_time

    screen.fill(black)
    pygame.draw.circle(screen, white, center=center, radius=radius, width=10)
    for dot in range(12):
        dot_center = (round(degrees(dot, radius - 30)[0] - 8), round(degrees(dot, radius - 30)[1] - 8))
        # print(dot_center)
        text = font.render(f"{dot + 1}", True, white)
        screen.blit(text, (dot_center[0], dot_center[1]))

    # minutes
    pygame.draw.line(screen, white, start_pos=center, end_pos=degrees(float(exact_time[1]) / 5 - 1, radius - 40),
                     width=6)

    # seconds
    pygame.draw.line(screen, white, start_pos=center, end_pos=degrees(float(exact_time[2]) / 5 - 1, radius - 60),
                     width=6)

    # hours
    pygame.draw.line(screen, white, start_pos=center, end_pos=degrees(int(exact_time[0]) % 12 - 1, radius - 80), width=6)

    pygame.display.flip()
