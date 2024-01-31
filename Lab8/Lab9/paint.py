import pygame
import sys

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((1000, 800))
# screen2 = pygame.display.set_mode((1000, 100))
pygame.surface.Surface((1000, 100))
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()

# fonts
font = pygame.font.SysFont("Verdana", 36)
font_small = pygame.font.SysFont("Verdana", 24)

# shapes
shapes = ['rectangle', 'circle', 'square', 'triangle', 'romb', 'right-triangle']
shape_x = 30
shape_y = screen.get_height() / 35

# colors
colors = [['red', screen.get_height() / 35],
          ['green', screen.get_height() / 35 * 3],
          ['blue', screen.get_height() / 35 * 5],
          ['yellow', screen.get_height() / 35 * 7]]
color_x = screen.get_width() - 30

# defaults
current_mode = shapes[0]
i = 0
current_color = 'red'
screen.fill((255, 255, 255))
sizes_for_rectangle = [0, 10]
radius = 10
black = (0, 0, 0)
eraser = False
prev_mode = shapes[0]

# junk
image = pygame.image.load("/Users/uakks/Desktop/Star.png")


def in_radius(x, y, color_of_x, color_of_y, r):
    return (((x - color_of_x) ** 2 + (y - color_of_y) ** 2 <= r ** 2 and
             color_of_x - r <= x <= color_of_x + r and
             color_of_y - r <= y <= color_of_y + r))


def print_word():
    current_shape = font_small.render('Mode: ' + str(current_mode), True, black)
    shape_surface = current_shape.get_rect(midleft=(30, screen.get_height() - 30))
    another_surface = shape_surface
    if another_surface == shape_surface:
        screen.blit(current_shape, shape_surface)
        print("Yay")
    else:
        print("wow")


while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                if current_mode != 'eraser':
                    i += 1
                    if i == len(shapes):
                        i = 0
                current_mode = shapes[i]
            if event.key == pygame.K_e:
                eraser = not eraser

        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] or event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if (in_radius(mouse_pos[0], mouse_pos[1], shape_x, shape_y * 9, 5) or
                    in_radius(mouse_pos[0], mouse_pos[1], shape_x, shape_y * 3, 5) or
                    in_radius(mouse_pos[0], mouse_pos[1], shape_x, shape_y * 1, 5) or
                    in_radius(mouse_pos[0], mouse_pos[1], shape_x, shape_y * 5, 5) or
                    in_radius(mouse_pos[0], mouse_pos[1], shape_x, shape_y * 11, 5) or
                    in_radius(mouse_pos[0], mouse_pos[1], shape_x, shape_y * 7, 5) or
                    in_radius(mouse_pos[0], mouse_pos[1], color_x, colors[0][1], 10) or
                    in_radius(mouse_pos[0], mouse_pos[1], color_x, colors[1][1], 10) or
                    in_radius(mouse_pos[0], mouse_pos[1], color_x, colors[2][1], 10) or
                    in_radius(mouse_pos[0], mouse_pos[1], color_x, colors[3][1], 10)):
                pass
            else:
                for color in colors:
                    if not in_radius(mouse_pos[0], mouse_pos[1], color_x, color[1], radius):
                        if current_mode == 'eraser':
                            pygame.draw.circle(screen, (255, 255, 255), [mouse_pos[0], mouse_pos[1]], radius)
                        else:
                            for shape in shapes:
                                if current_mode == 'square':
                                    pygame.draw.rect(screen, current_color,
                                                     (mouse_pos[0] - radius, mouse_pos[1] - radius, radius * 2,
                                                      radius * 2))
                                elif current_mode == 'triangle':
                                    pygame.draw.polygon(screen, current_color, ((mouse_pos[0], mouse_pos[1] - radius),
                                                                                (mouse_pos[0] - radius,
                                                                                 mouse_pos[1] + radius),
                                                                                (mouse_pos[0] + radius,
                                                                                 mouse_pos[1] + radius)))
                                elif current_mode == 'right-triangle':
                                    pygame.draw.polygon(screen, current_color,
                                                        ((mouse_pos[0] - radius, mouse_pos[1] + radius),
                                                         (mouse_pos[0] - radius, mouse_pos[1] - radius),
                                                         (mouse_pos[0] + radius, mouse_pos[1] + radius)))
                                elif current_mode == 'rectangle':
                                    pygame.draw.rect(screen, current_color,
                                                     (mouse_pos[0] - radius, mouse_pos[1] - radius,
                                                      radius * 2 + sizes_for_rectangle[0],
                                                      radius * 2 + sizes_for_rectangle[1]))
                                elif current_mode == 'romb':
                                    pygame.draw.polygon(screen, current_color, ((mouse_pos[0] - radius, mouse_pos[1]),
                                                                                (mouse_pos[0],
                                                                                 mouse_pos[1] - radius * 2),
                                                                                (mouse_pos[0] + radius, mouse_pos[1]),
                                                                                (mouse_pos[0],
                                                                                 mouse_pos[1] + radius * 2)))
                                else:
                                    pygame.draw.circle(screen, current_color, (mouse_pos[0], mouse_pos[1]), radius)

    if eraser:
        current_mode = 'eraser'
    else:
        current_mode = shapes[i]
    # radius of circle
    if pygame.key.get_pressed()[pygame.K_r] and pygame.key.get_pressed()[pygame.K_EQUALS] and pygame.key.get_pressed()[
        pygame.K_x]:
        sizes_for_rectangle[0] += 1
    elif pygame.key.get_pressed()[pygame.K_r] and pygame.key.get_pressed()[pygame.K_MINUS] and pygame.key.get_pressed()[
        pygame.K_x]:
        sizes_for_rectangle[0] -= 1
    elif pygame.key.get_pressed()[pygame.K_r] and pygame.key.get_pressed()[pygame.K_MINUS] and pygame.key.get_pressed()[
        pygame.K_y]:
        sizes_for_rectangle[1] -= 1
    elif pygame.key.get_pressed()[pygame.K_r] and pygame.key.get_pressed()[pygame.K_EQUALS] and \
            pygame.key.get_pressed()[pygame.K_y]:
        sizes_for_rectangle[1] += 1
    elif pygame.key.get_pressed()[pygame.K_EQUALS]:
        radius += 1
        if radius > 100:
            radius = 100
    elif pygame.key.get_pressed()[pygame.K_MINUS]:
        radius -= 1
        if radius < 1:
            radius = 1

    # color selection
    for color in colors:
        pygame.draw.circle(screen, color[0], (color_x, color[1]), 10)
        if in_radius(mouse_pos[0], mouse_pos[1], color_x, color[1], 10) and pygame.mouse.get_pressed()[0]:
            current_color = color[0]
            print("changed color to", current_color)

    for shape in shapes:
        if shape == 'square':
            pygame.draw.rect(screen, black,
                             (shape_x - 5, shape_y * 3 - 5, 10, 10))
            if in_radius(mouse_pos[0], mouse_pos[1], shape_x, shape_y * 3, 5) and pygame.mouse.get_pressed()[0]:
                current_mode = shape
                i = 2
        elif shape == 'triangle':
            pygame.draw.polygon(screen, black, ((shape_x, shape_y * 5 - 5),
                                                (shape_x - 5, shape_y * 5 + 5),
                                                (shape_x + 5, shape_y * 5 + 5)))
            if in_radius(mouse_pos[0], mouse_pos[1], shape_x, shape_y * 5, 5) and pygame.mouse.get_pressed()[0]:
                current_mode = shape
                i = 3
        elif shape == 'right-triangle':
            pygame.draw.polygon(screen, black,
                                ((shape_x - 5, shape_y + 5),
                                 (shape_x - 5, shape_y - 5),
                                 (shape_x + 5, shape_y + 5)))
            if in_radius(mouse_pos[0], mouse_pos[1], shape_x, shape_y, 5) and pygame.mouse.get_pressed()[0]:
                current_mode = shape
                i = 5
        elif shape == 'rectangle':
            pygame.draw.rect(screen, black, (shape_x - 5, shape_y * 7 - 5, 8, 12))
            if in_radius(mouse_pos[0], mouse_pos[1], shape_x, shape_y * 7, 5) and pygame.mouse.get_pressed()[0]:
                current_mode = shape
                i = 0
        elif shape == 'romb':
            pygame.draw.polygon(screen, black, ((shape_x - 5, shape_y * 9),
                                                (shape_x, shape_y * 9 - 10),
                                                (shape_x + 5, shape_y * 9),
                                                (shape_x, shape_y * 9 + 10)))
            if in_radius(mouse_pos[0], mouse_pos[1], shape_x, shape_y * 9, 5) and pygame.mouse.get_pressed()[0]:
                current_mode = shape
                i = 4
        else:
            pygame.draw.circle(screen, black, (shape_x, shape_y * 11), 5)
            if in_radius(mouse_pos[0], mouse_pos[1], shape_x, shape_y * 11, 5) and pygame.mouse.get_pressed()[0]:
                current_mode = shape
                i = 1

    print_word()
    pygame.display.update()
    clock.tick(60)
