import pygame
class Colina(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("./assets/sprites/tileset/colina.png")
        self.rect = self.image.get_rect(topleft = pos)