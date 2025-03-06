import pygame
import var_glob

class Boton_de_interfaz(pygame.sprite.Sprite):
    def __init__(self, grupo, verificacion, ubicacion, imagen_icono, texto, color_texto, text_ubic):
        super().__init__(grupo)
        
        self.fuente_de_botones = pygame.font.Font("assets/fonts/pixeled_font.ttf", 10)

        self.sprite_verific = verificacion
        self.ubicacion_x_y = ubicacion
        self.sprite_icono = imagen_icono
        self.font = self.fuente_de_botones
        self.texto = texto
        self.color_texto = color_texto
        self.text_ubic = text_ubic
        
        self.sprite_texto = self.fuente_de_botones.render(texto, True, color_texto)
        self.text_rect = self.sprite_texto.get_rect(topleft=text_ubic)

    def update(self):
        var_glob.screen.blit(self.sprite_verific, self.ubicacion_x_y)
        var_glob.screen.blit(self.sprite_icono, self.ubicacion_x_y)
        var_glob.screen.blit(self.sprite_texto, self.text_rect)
