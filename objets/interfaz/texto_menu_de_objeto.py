import pygame
import var_glob

class Texto_de_menu(pygame.sprite.Sprite): 
    def __init__(self, grupo, texto, text):
        super().__init__(grupo)

        self.sprite_texto = texto
        self.text_rect = text

    def update(self):
        var_glob.complete_screen.blit(self.sprite_texto, self.text_rect)
