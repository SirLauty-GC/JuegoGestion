import pygame
import var_glob

class Iconos_interfaz(pygame.sprite.Sprite):
    def __init__(self, grupo, ubicacion, imagen_icono, valor, color_texto, text_ubic):
        super().__init__(grupo)
        self.fuente_de_botones = pygame.font.Font("assets/fonts/pixeled_font.ttf", 10)
        
        self.sprite_icono = imagen_icono
        self.sprite_verific = imagen_icono
        self.ubicacion_x_y = ubicacion
        self.font = self.fuente_de_botones
        self.texto = str(valor)
        self.color_texto = color_texto
        self.text_ubic = text_ubic
        self.sprite_texto = self.fuente_de_botones.render(self.texto, True, color_texto)
        self.text_rect = self.sprite_texto.get_rect(topleft=text_ubic)
    def update(self):
        var_glob.screen.blit(self.sprite_verific, self.ubicacion_x_y)
        var_glob.screen.blit(self.sprite_icono, self.ubicacion_x_y)
        var_glob.screen.blit(self.sprite_texto, self.text_rect)
