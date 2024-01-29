# Import the pygame module
import pygame
from Enemy import Enemy
from KillCount import kill_count
from Player import Player
from config import SCREEN_WIDTH, SCREEN_HEIGHT, all_sprites, enemies, players

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


pygame.init()

# Set game title in window
pygame.display.set_caption("Hongkong 2024")

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set game icon
img = pygame.image.load("Assets/latest-3890457162.png")
pygame.display.set_icon(img)

# Play Chinese Music FOREVER
pygame.mixer.init()
pygame.mixer.music.load(
    "Assets/HONGKONG1997 - I Love Beijing Tiananmen (High Quality) (Full song - not loop) not a clickbait.opus"
)
pygame.mixer.music.play(-1)

# Create a custom event for adding a new enemy

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Instantiate player.

player = Player()

# background
background = pygame.image.load("Assets/ccp.jpg").convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# - enemies and players are used for collision detection and position updates

# - all_sprites is used for rendering


all_sprites.add(player)
players.add(player)

# Set font
pygame.font.init()

my_font = pygame.font.Font("Assets/CuteFont-Regular.ttf", 50)

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
    if kill_count.get_kill_count() >= 1200000000:
        bottom_text = "1.2 BILLION RED COMMUNIST SLAIN"
    else:
        bottom_text = "Red Chinese Communist Eliminated:" + str(
            kill_count.get_kill_count()
        )
    text_surface = my_font.render((bottom_text), False, (255, 255, 255))
    screen.blit(text_surface, (SCREEN_WIDTH / 8, SCREEN_HEIGHT * 0.05))

    # Draw the player and enemies on the screen

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Update the display

    pygame.display.flip()

    # Ensure program maintains a rate of 150 frames per second

    clock.tick(150)
