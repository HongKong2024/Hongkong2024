# Define Hong Kong's hero class
from Explosion import Explosion
from KillCount import kill_count
from config import SCREEN_HEIGHT, SCREEN_WIDTH, all_sprites, enemies, speed


import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP
from threading import Timer


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.surf = pygame.image.load("Assets/Lee.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.rect = self.surf.get_rect()

    # Move the sprite based on user keypresses. Collide with and kill red chinese communist.
    def update(self, pressed_keys):
        movements = {
            K_UP: (0, -speed),
            K_DOWN: (0, speed),
            K_LEFT: (-speed, 0),
            K_RIGHT: (speed, 0),
        }

        for key, (dx, dy) in movements.items():
            if pressed_keys[key]:
                self.rect.move_ip(dx, dy)
                if pygame.sprite.spritecollideany(self, enemies):
                    sprite = pygame.sprite.spritecollideany(self, enemies)
                    self.rect.move_ip(-dx, -dy)
                    unused_channel = pygame.mixer.find_channel()
                    if unused_channel:
                        unused_channel.play(
                            pygame.mixer.Sound("Assets/Goblin Death.opus")
                        )
                    kill_count.increment()
                    explosion = Explosion()
                    explosion.rect = sprite.rect
                    sprite.kill()
                    all_sprites.add(explosion)
                    kill_timer = Timer(2, explosion.kill)
                    kill_timer.start()

        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
