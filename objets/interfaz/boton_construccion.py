import pygame

class Boton_construccion(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, group, activacion):
        super().__init__(group)
        self.icono = pygame.image.load(f"./sprites/ui/icono_construccion{activacion}.png")
        self.rect = self.icono.get_rect(topleft = (x,y))
        screen.blit(self.icono,(x, y))