import pygame
import var_glob

class Panel_de_la_interfaz(pygame.sprite.Sprite):
    def __init__(self, grupo, x, y):
        super().__init__(grupo)
        self.sprite_icono = pygame.image.load("./assets/sprites/ui/panel.png")
        self.ubicacion_x_y, self.text_ubic = (x, y), (x, y)
        self.sprite_verific, self.sprite_texto = pygame.image.load("./assets/sprites/ui/panel.png"), pygame.image.load("./assets/sprites/ui/panel.png")
        var_glob.screen.blit(self.sprite_icono, self.ubicacion_x_y)