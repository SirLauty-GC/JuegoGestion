import pygame
import var_glob

class Panel_de_la_interfaz(pygame.sprite.Sprite):
    def __init__(self, grupo, x, y, ancho, alto, color):
        super().__init__(grupo)
        self.sprite_icono = pygame.Rect(x,y,ancho,alto)
        self.color = color
        pygame.draw.rect(var_glob.complete_screen, self.color, self.sprite_icono)
    
    def obtener_recta(self):
        return self.sprite_icono