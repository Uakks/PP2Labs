# importing everything
import numpy
import pygame
import sys
import random
from pygame.math import Vector2


# defining class Snake(Player)
class Snake:
    def __init__(self):
        # creating body, 3 cells of a body, default direction, score and new block attributes
        self.body = [Vector2(7, 6), Vector2(6, 6), Vector2(5, 6)]
        self.direction = Vector2(0, 0)
        self.new_block = False
        self.score = 0

        # all below is just graphics of snake, head, tail to every direction, turning positions and straight body
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

        # current sound when eating food
        self.crunch_sound = pygame.mixer.Sound(sounds[sound_index])

    # drawing snake
    def draw_snake(self):
        # these 2 methods will update head and tail direction according to next and previous element in body
        self.update_head_graphics()
        self.update_tail_graphics()

        # getting rectangle position of each cell to define position for each cell
        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            # checking each cell of body index to draw specific part of this body, for example, when index == 0,
            # it means that it must be head, so we blit head part on screen
            if index == 0:
                screen.blit(self.head, block_rect)
            # last index is always tail
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                # here we compare each body cell from index 1 to previous of last with their previous and next cell
                previous_block = self.body[index - 1] - block
                next_block = self.body[index + 1] - block
                # when the x-axis or y-axis is same draw straight bodies
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    # checking for every possible turning point and blitting correct image
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.y == -1 and next_block.x == 1 or previous_block.x == 1 and next_block.y == -1:
                        screen.blit(self.body_br, block_rect)
                    elif previous_block.y == 1 and next_block.x == 1 or previous_block.x == 1 and next_block.y == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.y == 1 and next_block.x == -1 or previous_block.x == -1 and next_block.y == 1:
                        screen.blit(self.body_tl, block_rect)

    def update_head_graphics(self):
        # drawing head according to next element of the body
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
        # drawing tail according to previous element of the body
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_down
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_left

    # moving snake
    def move_snake(self):
        # moving snake with deque method
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    # when snake eats something
    def add_block(self):
        self.new_block = True

    # sound effects
    def play_crunch_sound(self):
        # playing random sound from library
        self.crunch_sound.play()
        sound_index = random.randint(0, len(sounds) - 1)
        self.crunch_sound = pygame.mixer.Sound(sounds[sound_index])

    # play again
    def reset(self):
        # resetting the game by assigning default values
        self.body = [Vector2(7, 6), Vector2(6, 6), Vector2(5, 6)]
        self.direction = Vector2(0, 0)
        self.score = 0


# Fruit class
class Fruit:
    # 3 images for different situations
    def __init__(self):
        # defining possible fruits, position and score image
        self.images = [
            "/Users/uakks/Desktop/snake_graphics/Apple.png",
            "/Users/uakks/Desktop/snake_graphics/Cherry.png",
            "/Users/uakks/Desktop/snake_graphics/Strawberry.png"
        ]
        self.randomize()
        self.image_for_score = pygame.transform.scale(pygame.image.load(self.images[0]).convert_alpha(),
                                                      (cell_size, cell_size))

    # drawing fruit on randomized coordinates
    def draw_fruit(self):
        # drawing chosen fruit on the screen
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        loaded = pygame.image.load(self.images[self.chance]).convert_alpha()
        self.used_image = pygame.transform.scale(loaded, (cell_size, cell_size))
        screen.blit(self.used_image, fruit_rect)

    # randomizing coordinates of fruit after collision
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        # chance of getting apple, cherry or strawberry
        self.chance = numpy.random.choice(numpy.arange(0, 3), p=[0.6, 0.3, 0.1])
        self.seconds = 5000
        # checking for strawberry, which will activate timer for collection
        if self.chance == 2:
            pygame.time.set_timer(pygame.USEREVENT + 1, 5000, 1)
        else:
            pygame.time.set_timer(pygame.USEREVENT + 1, 0, 1)


class Main:
    # main game, initialize player and fruit
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.difficulty = 0
        self.reset = True
        self.start_tick = pygame.time.get_ticks()

    # update the screen and check for any kind of collision
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    # drawing elements on the screen
    def draw_elements(self):
        self.draw_grass()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_score()

    # checking for collision
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # different types of fruits gives different amount of points
            if self.fruit.chance == 0:
                self.snake.score += 1
            elif self.fruit.chance == 1:
                self.snake.score += 2
            elif self.fruit.chance == 2:
                self.snake.score += 5
            # randomize and extend snake body after player collects the fruit
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
            # set up difficulty
            if self.difficulty > 25:
                self.difficulty = 25
            else:
                self.difficulty += 1

        # make sure to avoid spawning fruit on body
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    # check for fail
    def check_fail(self):
        # when snake hits the wall
        if not 0 <= self.snake.body[0].x <= cell_number - 1 or not 0 <= self.snake.body[0].y <= cell_number - 1:
            self.game_over()

        # when snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        # resetting the game and difficulty
        self.snake.reset()
        self.difficulty = 0

    # drawing grass on the field
    def draw_grass(self):
        grass_color = (167, 209, 61)

        for col in range(cell_number):
            for row in range(cell_number):
                if (col + row) % 2 == 0:
                    grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rect)

    # draw score on the screen
    def draw_score(self):

        # first create difficulty text and level
        difficulty_text = str(self.difficulty // 5)
        if self.difficulty / 5 >= 5:
            difficulty_surface = font_small.render("Dif: " + difficulty_text, True, (255, 0, 0))
        else:
            difficulty_surface = font_small.render("Dif: " + difficulty_text, True, (255, 255, 255))

        # create score text
        score_text = str(self.snake.score)
        score_surface = font_small.render(score_text, True, (255, 255, 255))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 60)

        # defining positions of the difficulty text and score text
        difficulty_rect = difficulty_surface.get_rect(center=(screen.get_width() - score_x, score_y))
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        # adding apple image to show that score text means collected points
        apple_rect = self.fruit.image_for_score.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left - 5, apple_rect.top - 5, apple_rect.width + score_rect.width + 10,
                              apple_rect.height + 10)

        # when strawberry on the screen, timer will start and be showed with text, also has position defined
        disappearing_message = font_small.render(f"Remaining time: {format(main_game.fruit.seconds / 1000, ".2f")}", True,
                                                 (255, 255, 255))
        message_surface = disappearing_message.get_rect(center=(cell_size * 6, cell_size * 2))

        pygame.draw.rect(screen, (167, 209, 57), bg_rect)

        # timer for strawberry, blitting it
        if self.fruit.chance == 2:
            main_game.fruit.seconds -= 5000/300
            screen.blit(disappearing_message, message_surface)

        # blitting every essential text and surfaces
        screen.blit(difficulty_surface, difficulty_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(self.fruit.image_for_score, apple_rect)
        pygame.draw.rect(screen, (50, 51, 52), bg_rect, 2)


# initializing the game with default values
pygame.init()
pygame.display.set_caption("Snake game")
cell_number = 30
cell_size = 25
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pygame.time.Clock()

# used sounds
sounds = [
    "/Users/uakks/Desktop/Crunch Sound.mp3",
    "/Users/uakks/Desktop/carrotnom-92106.mp3"
]
sound_index = random.randint(0, len(sounds) - 1)

# used fonts
font = pygame.font.SysFont("Verdana", 48)
font_small = pygame.font.SysFont("Verdana", 24)

# game events and starting class
main_game = Main()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

FOOD_TIMER = pygame.USEREVENT + 1

timer = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # randomizes fruit position if player does not eat it on time
        if event.type == FOOD_TIMER:
            main_game.fruit.randomize()

        # updating screen in respect with difficulty
        if event.type == SCREEN_UPDATE:
            main_game.update()
            SCREEN_UPDATE = pygame.USEREVENT
            pygame.time.set_timer(SCREEN_UPDATE, 150 - main_game.difficulty // 5 * 15)

        # another way to leave the game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        # changing direction according to arrow buttons
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

    # updating screen and drawing everything
    screen.fill((170, 230, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
