import pygame
class Montana(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load("./assets/sprites/tileset/montana.png")
        self.rect = self.image.get_rect(topleft = pos)