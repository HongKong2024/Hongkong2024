# Import the pygame module

import pygame
import random
from threading import Timer

# Import pygame.locals for easier access to key coordinates

# Updated to conform to flake8 and black standards

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Timer

# Define constants for the screen width and height

SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600


# how fast do you want everything to move?
speed = 1


kills = 0


# Keep track of Red Chinese Communist eliminated
def kill_counter():
    global kills
    kills = kills + 1


# Define Hong Kong's hero class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.surf = pygame.image.load("Lee.png").convert()

        self.surf.set_colorkey((255, 255, 255))

        self.surf = pygame.transform.scale(self.surf, (100, 100))

        self.rect = self.surf.get_rect()

        # Move the sprite based on user keypresses. Collide with and kill red chinese communist.

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -speed)
            if pygame.sprite.spritecollideany(self, enemies):
                sprite = pygame.sprite.spritecollideany(self, enemies)
                self.rect.move_ip(0, speed)
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("Goblin Death.wav"))
                kill_counter()
                explosion = Explosion()
                explosion.rect = sprite.rect
                sprite.kill()
                all_sprites.add(explosion)
                kill_timer = Timer(2, explosion.kill)
                kill_timer.start()

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, speed)
            if pygame.sprite.spritecollideany(self, enemies):
                sprite = pygame.sprite.spritecollideany(self, enemies)
                self.rect.move_ip(0, -speed)
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("Goblin Death.wav"))
                kill_counter()
                explosion = Explosion()
                explosion.rect = sprite.rect
                sprite.kill()
                all_sprites.add(explosion)
                kill_timer = Timer(2, explosion.kill)
                kill_timer.start()

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-speed, 0)
            if pygame.sprite.spritecollideany(self, enemies):
                sprite = pygame.sprite.spritecollideany(self, enemies)
                self.rect.move_ip(speed, 0)
                pygame.mixer.Channel(2).play(pygame.mixer.Sound("Goblin Death.wav"))
                kill_counter()
                explosion = Explosion()
                explosion.rect = sprite.rect
                sprite.kill()
                all_sprites.add(explosion)
                kill_timer = Timer(2, explosion.kill)
                kill_timer.start()

        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(speed, 0)
            if pygame.sprite.spritecollideany(self, enemies):
                sprite = pygame.sprite.spritecollideany(self, enemies)
                self.rect.move_ip(-speed, 0)
                pygame.mixer.Channel(3).play(pygame.mixer.Sound("Goblin Death.wav"))
                kill_counter()
                explosion = Explosion()
                explosion.rect = sprite.rect
                sprite.kill()
                all_sprites.add(explosion)
                kill_timer = Timer(2, explosion.kill)
                kill_timer.start()

        # Keep player on the screen

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# Define Red Chinese Communist class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()

        self.surf = pygame.image.load("rcc.png").convert()

        self.surf = pygame.transform.scale(self.surf, (30, 30))

        self.surf.set_colorkey((0, 0, 0))

        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(1, 5)

    # Move the sprite based on speed

    # Remove the sprite when it passes the left edge of the screen

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if pygame.sprite.spritecollideany(self, players):
            self.rect.move_ip(self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self):
        super(Explosion, self).__init__()

        self.surf = pygame.image.load("explosion.png").convert()

        self.surf.set_colorkey((255, 255, 255))

        self.surf = pygame.transform.scale(self.surf, (40, 40))


# Initialize pygame

pygame.init()

# Set game title in window
pygame.display.set_caption("Hongkong 2024")

# Create the screen object

# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set game icon
img = pygame.image.load("latest-3890457162.png")
pygame.display.set_icon(img)

# Play Chinese Music FOREVER

pygame.mixer.init()
pygame.mixer.music.load(
    "HONGKONG1997 - I Love Beijing Tiananmen (High Quality) (Full song - not loop) not a clickbait.mp3"
)
pygame.mixer.music.play(-1)

# Create a custom event for adding a new enemy

ADDENEMY = pygame.USEREVENT + 1

pygame.time.set_timer(ADDENEMY, 250)

# Instantiate player.

player = Player()

# background
background = pygame.image.load("ccp.jpg").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# - enemies and players are used for collision detection and position updates

# - all_sprites is used for rendering

enemies = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

all_sprites.add(player)

players = pygame.sprite.Group()
players.add(player)

# Set font
pygame.font.init()

my_font = pygame.font.Font("CuteFont-Regular.ttf", 50)

# Variable to keep the main loop running

running = True

# Setup the clock for a decent framerate

clock = pygame.time.Clock()
# Main loop

while running:
    # for loop through the event queue

    for event in pygame.event.get():
        # Check for KEYDOWN event

        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop

            if event.key == K_ESCAPE:
                running = False

        # Check for QUIT event. If QUIT, then set running to false.

        elif event.type == QUIT:
            running = False

        # Add a new enemy?

        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups

            new_enemy = Enemy()

            enemies.add(new_enemy)

            all_sprites.add(new_enemy)

    # Get the set of keys pressed and check for user input

    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses

    player.update(pressed_keys)

    # Update enemy position

    enemies.update()

    # Render Background
    screen.blit(background, (0, 0))
    bottom_text = "placeholder"

    # Bottom Text Counter
    if kills >= 1200000000:
        bottom_text = "1.2 BILLION RED COMMUNIST SLAIN"
    else:
        bottom_text = "Red Chinese Communist Eliminated:" + str(kills)
    text_surface = my_font.render((bottom_text), False, (255, 255, 255))
    screen.blit(text_surface, (SCREEN_WIDTH / 8, SCREEN_HEIGHT * 0.05))

    # Draw the player and enemies on the screen

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Update the display

    pygame.display.flip()

    # Ensure program maintains a rate of 150 frames per second

    clock.tick(150)
