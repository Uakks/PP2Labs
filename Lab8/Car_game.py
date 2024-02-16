# Imports
import random
import time

import numpy
import pygame
import sys
from pygame.locals import *

# Initializing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Other Variables for use in the program, defaults
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SPEED = 15
SCORE = 0
COINS = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# background image
back = pygame.image.load("assets/car_game_assets/images/Road_back.png")
background = pygame.transform.scale(back, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a white screen, name it
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("Race")


# Classes
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        # setting up the params for enemy cars
        super().__init__()
        image = pygame.image.load("assets/car_game_assets/images/Black_car.png")
        self.image = pygame.transform.scale(image, (80, 177))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.counter = 0
        self.speed = 5

    # moving enemy cars with defined speed and resetting after they hit bottom of the screen
    def move(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.top > 600:
            self.counter += 1
            if self.counter >= 75:
                self.counter = 75
            elif self.counter % 5 == 0:
                self.speed += 1
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    # defining player parameters
    def __init__(self):
        super().__init__()
        image = pygame.image.load("assets/car_game_assets/images/Red_car.png")
        self.image = pygame.transform.scale(image, (80, 177))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 90)

    # moving players car with constant speed
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-SPEED, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(SPEED, 0)


class Coins(pygame.sprite.Sprite):
    # defining coins, that will appear as extra element
    def __init__(self):
        super().__init__()
        self.chance = 0
        self.coins = [
            "assets/car_game_assets/images/Coin.png",
            "assets/car_game_assets/images/Star.png"
        ]
        self.image = pygame.transform.scale(pygame.image.load(self.coins[0]), (60, 60))
        self.rect = self.image.get_rect()
        self.randomize()

    def move(self):
        # moving coins down the screen until they hit ground
        self.rect.move_ip(0, 5)
        if self.rect.top > SCREEN_HEIGHT:
            self.change_coin()
            self.randomize()

    def change_coin(self):
        # creating chance of getting more valuable coin, updating image also
        self.chance = numpy.random.choice(numpy.arange(0, 2), p=[0.85, 0.15])
        print(self.chance)
        self.image = pygame.transform.scale(pygame.image.load(self.coins[self.chance]), (60, 60))

    def randomize(self):
        # randomizing next coin drops position
        self.rect.top = 0
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)


# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coins()

# Creating Sprites Groups
game_coins = pygame.sprite.Group()
game_coins.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(C1)
all_sprites.add(P1)
all_sprites.add(E1)

# Just background music
pygame.mixer.music.load("assets/car_game_assets/audios/Better Day.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

# Game Loop
while True:

    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Show score and coins
    screen.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))
    coins = font_small.render(str(COINS), True, YELLOW)
    screen.blit(coins, (SCREEN_WIDTH - 30, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # Checking for collision of enemy cars and coins to make sure that coins are collectable
    if pygame.sprite.spritecollideany(E1, game_coins):
        C1.randomize()

    # checking for collision between player and coins,
    # to count total score of coins and resetting coins to drop from above
    if pygame.sprite.spritecollideany(P1, game_coins):
        pygame.mixer.Sound('assets/car_game_assets/audios/Coin Touch.wav').play()
        if C1.chance == 0:
            COINS += 1
        else:
            COINS += 5
        C1.change_coin()
        C1.rect.top = 0
        C1.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)
        # random_timing = random.randint(0, 10000)

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound('assets/car_game_assets/audios/Accident Sound.wav').play()
        time.sleep(0.5)

        # showing texts on endgame screen
        collected_coins = font_small.render(f"Collected coins: {COINS}", True, BLACK)
        final_score = font_small.render(f"Score: {SCORE}", True, BLACK)
        screen.fill(RED)
        screen.blit(game_over, (SCREEN_WIDTH / 2 - 130, SCREEN_HEIGHT / 2 - 30))
        screen.blit(final_score, (SCREEN_WIDTH / 2 - 130, SCREEN_HEIGHT / 2 + 30))
        screen.blit(collected_coins, (SCREEN_WIDTH / 2 - 130, SCREEN_HEIGHT / 2 + 50))

        # deleting elements from all_sprites and quitting pygame
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Update screen
    pygame.display.update()
    FramePerSec.tick(FPS)
