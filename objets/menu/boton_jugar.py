import pygame

class Boton_menu_principal_jugar(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, group, activacion):
        super().__init__(group)
        self.icono = pygame.image.load(f"./sprites/menu/icono_menu_principal_jugar{activacion}.png")
        self.rect = self.icono.get_rect(topleft = (x,y))
        screen.blit(self.icono,(x, y))