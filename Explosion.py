import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self):
        super(Explosion, self).__init__()

        self.surf = pygame.image.load("Assets/explosion.png").convert()
        self.surf.set_colorkey((255, 255, 255))
        self.surf = pygame.transform.scale(self.surf, (40, 40))
