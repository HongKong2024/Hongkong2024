# Define Red Chinese Communist class
from config import SCREEN_HEIGHT, SCREEN_WIDTH, players
import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()

        self.surf = pygame.image.load("Assets/rcc.png").convert()
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        self.surf.set_colorkey((0, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(1, 5)

    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if pygame.sprite.spritecollideany(self, players):
            self.rect.move_ip(self.speed, 0)
        if self.rect.right < 0:
            self.kill()
