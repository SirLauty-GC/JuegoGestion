import pygame
class Arena(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("./assets/sprites/tileset/arena.png")
        self.rect = self.image.get_rect(topleft = pos)