# Imports
import random
import time

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

# Other Variables for use in the program
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SPEED = 5
SCORE = 0
COINS = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# background image
back = pygame.image.load("/Users/uakks/Desktop/screenshots/Road_back.png")
background = pygame.transform.scale(back, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Race")


# Classes
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("/Users/uakks/Desktop/Black_car.png")
        self.image = pygame.transform.scale(image, (80, 177))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load("/Users/uakks/Desktop/Red_car.png")
        self.image = pygame.transform.scale(image, (80, 177))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 90)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[K_UP]:
        # self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        # self.rect.move_ip(0,5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-SPEED - 3, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(SPEED + 3, 0)


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        image = pygame.image.load("/Users/uakks/Desktop/coin.png")
        self.image = pygame.transform.scale(image, (75, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > SCREEN_HEIGHT:
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

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Just background music
pygame.mixer.music.load("/Users/uakks/Desktop/Better Day.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

# Game Loop
while True:

    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.2
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Show score and coins
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    coins = font_small.render(str(COINS), True, YELLOW)
    DISPLAYSURF.blit(coins, (SCREEN_WIDTH-30, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Colliding with coins
    if pygame.sprite.spritecollideany(P1, game_coins):
        pygame.mixer.Sound('/Users/uakks/Desktop/Coin Touch.wav').play()
        COINS += 1
        C1.rect.top = 0
        C1.rect.center = (random.randint(50, SCREEN_WIDTH - 50), 0)
        # random_timing = random.randint(0, 10000)

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound('/Users/uakks/Desktop/Accident Sound.wav').play()
        time.sleep(0.5)

        collected_coins = font_small.render(f"Collected coins: {COINS}", True, BLACK)
        final_score = font_small.render(f"Score: {SCORE}", True, BLACK)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (SCREEN_WIDTH / 2 - 130, SCREEN_HEIGHT / 2 - 30))
        DISPLAYSURF.blit(final_score, (SCREEN_WIDTH / 2 - 130, SCREEN_HEIGHT / 2 + 30))
        DISPLAYSURF.blit(collected_coins, (SCREEN_WIDTH / 2 - 130, SCREEN_HEIGHT / 2 + 50))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Update screen
    pygame.display.update()
    FramePerSec.tick(FPS)
