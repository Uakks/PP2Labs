import numpy
import pygame
import sys
import random
from pygame.math import Vector2

pygame.display.set_caption("Snake game")


class Snake:
    def __init__(self):
        self.body = [Vector2(7, 6), Vector2(6, 6), Vector2(5, 6)]
        self.direction = Vector2(0, 0)
        self.new_block = False
        self.score = 0

        self.head_up = pygame.transform.scale(
            pygame.image.load("/Users/uakks/Desktop/snake_graphics/head_top.png").convert_alpha(),
            (cell_size, cell_size))
        self.head_down = pygame.transform.scale(
            pygame.image.load("/Users/uakks/Desktop/snake_graphics/head_bottom.png").convert_alpha(),
            (cell_size, cell_size))
        self.head_left = pygame.transform.scale(
            pygame.image.load("/Users/uakks/Desktop/snake_graphics/head_left.png").convert_alpha(),
            (cell_size, cell_size))
        self.head_right = pygame.transform.scale(
            pygame.image.load("/Users/uakks/Desktop/snake_graphics/head_right.png").convert_alpha(),
            (cell_size, cell_size))

        self.tail_up = pygame.transform.scale(
            pygame.image.load("/Users/uakks/Desktop/snake_graphics/tail_top.png").convert_alpha(),
            (cell_size, cell_size))
        self.tail_down = pygame.transform.scale(
            pygame.image.load("/Users/uakks/Desktop/snake_graphics/tail_bottom.png").convert_alpha(),
            (cell_size, cell_size))
        self.tail_left = pygame.transform.scale(
            pygame.image.load("/Users/uakks/Desktop/snake_graphics/tail_left.png").convert_alpha(),
            (cell_size, cell_size))
        self.tail_right = pygame.transform.scale(
            pygame.image.load("/Users/uakks/Desktop/snake_graphics/tail_right.png").convert_alpha(),
            (cell_size, cell_size))

        self.body_vertical = pygame.transform.scale(
            pygame.image.load("/Users/uakks/Desktop/snake_graphics/vertical.png").convert_alpha(),
            (cell_size, cell_size))
        self.body_horizontal = pygame.transform.scale(
            pygame.image.load("/Users/uakks/Desktop/snake_graphics/horizontal.png").convert_alpha(),
            (cell_size, cell_size))

        self.body_tr = pygame.transform.scale(
            pygame.image.load("/Users/uakks/Desktop/snake_graphics/top_right_turn.png").convert_alpha(),
            (cell_size, cell_size))
        self.body_tl = pygame.transform.scale(
            pygame.image.load("/Users/uakks/Desktop/snake_graphics/top_left_turn.png").convert_alpha(),
            (cell_size, cell_size))
        self.body_br = pygame.transform.scale(
            pygame.image.load("/Users/uakks/Desktop/snake_graphics/bottom_right_turn.png").convert_alpha(),
            (cell_size, cell_size))
        self.body_bl = pygame.transform.scale(
            pygame.image.load("/Users/uakks/Desktop/snake_graphics/bottom_left_turn.png").convert_alpha(),
            (cell_size, cell_size))
        self.crunch_sound = pygame.mixer.Sound(sounds[sound_index])

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index - 1] - block
                next_block = self.body[index + 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.y == -1 and next_block.x == 1 or previous_block.x == 1 and next_block.y == -1:
                        screen.blit(self.body_br, block_rect)
                    elif previous_block.y == 1 and next_block.x == 1 or previous_block.x == 1 and next_block.y == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.y == 1 and next_block.x == -1 or previous_block.x == -1 and next_block.y == 1:
                        screen.blit(self.body_tl, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_down
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_left

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()
        sound_index = random.randint(0, len(sounds)-1)
        self.crunch_sound = pygame.mixer.Sound(sounds[sound_index])

    def reset(self):
        self.body = [Vector2(7, 6), Vector2(6, 6), Vector2(5, 6)]
        self.direction = Vector2(0, 0)
        self.score = 0


class Fruit:
    def __init__(self):
        self.images = [
            "/Users/uakks/Desktop/snake_graphics/Apple.png",
            "/Users/uakks/Desktop/snake_graphics/Cherry.png",
            "/Users/uakks/Desktop/snake_graphics/Strawberry.png"
        ]
        self.next_chance = 0
        self.randomize()
        self.image_for_score = pygame.transform.scale(pygame.image.load(self.images[0]).convert_alpha(), (cell_size, cell_size))

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        loaded = pygame.image.load(self.images[self.chance]).convert_alpha()
        self.used_image = pygame.transform.scale(loaded, (cell_size, cell_size))
        screen.blit(self.used_image, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        self.chance = numpy.random.choice(numpy.arange(0, 3), p=[0.2, 0.3, 0.5])
        if self.chance == 2:
            pygame.time.set_timer(pygame.USEREVENT + 1, 5000, 1)
        else:
            pygame.time.set_timer(TIMER_EVENT, 0, 1)


class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.difficulty = 0
        self.reset = True

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            if self.fruit.chance == 0:
                self.snake.score += 1
            elif self.fruit.chance == 1:
                self.snake.score += 2
            elif self.fruit.chance == 2:
                self.snake.score += 5
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
            if self.difficulty > 25:
                self.difficulty = 25
            else:
                self.difficulty += 1

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x <= cell_number - 1 or not 0 <= self.snake.body[0].y <= cell_number - 1:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()
        self.difficulty = 0

    def draw_grass(self):
        grass_color = (167, 209, 61)

        for col in range(cell_number):
            for row in range(cell_number):
                if (col + row) % 2 == 0:
                    grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)
            # for row in range(cell_number):

    def draw_score(self):
        # timer = 5000
        # while timer > 0:
            # disappearing_message = font_small.render()

        difficulty_text = str(self.difficulty // 5)
        if self.difficulty / 5 >= 5:
            difficulty_surface = font_small.render("Dif: " + difficulty_text, True, (255, 0, 0))
        else:
            difficulty_surface = font_small.render("Dif: " + difficulty_text, True, (255, 255, 255))

        score_text = str(self.snake.score)
        score_surface = font_small.render(score_text, True, (255, 255, 255))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 60)

        difficulty_rect = difficulty_surface.get_rect(center=(screen.get_width() - score_x, score_y))
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = self.fruit.image_for_score.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left - 5, apple_rect.top - 5, apple_rect.width + score_rect.width + 10,
                              apple_rect.height + 10)

        pygame.draw.rect(screen, (167, 209, 57), bg_rect)
        screen.blit(difficulty_surface, difficulty_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(self.fruit.image_for_score, apple_rect)
        pygame.draw.rect(screen, (50, 51, 52), bg_rect, 2)


pygame.init()
cell_number = 30
cell_size = 25
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

sounds = [
    "/Users/uakks/Desktop/Crunch Sound.mp3",
    "/Users/uakks/Desktop/carrotnom-92106.mp3"
]
sound_index = random.randint(0, len(sounds)-1)

font = pygame.font.SysFont("Verdana", 48)
font_small = pygame.font.SysFont("Verdana", 24)
# # #

main_game = Main()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

TIMER_EVENT = pygame.USEREVENT + 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == TIMER_EVENT:
            main_game.fruit.randomize()

        if event.type == SCREEN_UPDATE:
            main_game.update()
            SCREEN_UPDATE = pygame.USEREVENT
            pygame.time.set_timer(SCREEN_UPDATE, 150 - main_game.difficulty // 5 * 15)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    screen.fill((170, 230, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
