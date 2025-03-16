import pygame
import var_glob

class Botoncito_de_menu(pygame.sprite.Sprite):
    def __init__(self, grupo, ubicacion, imagen_icono):
        super().__init__(grupo)

        self.ubicacion_x_y = ubicacion
        self.sprite_icono = imagen_icono

    def update(self):
        var_glob.complete_screen.blit(self.sprite_icono, self.ubicacion_x_y)
    
    def obtener_recta(self):
        return self.sprite_icono.get_rect(topleft = self.ubicacion_x_y)
