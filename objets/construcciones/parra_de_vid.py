import pygame

class Parra_de_vid(pygame.sprite.Sprite):
    def __init__(self, pos, groups, etapa, rec):
        super().__init__(groups)

        if rec:
            if etapa > 25:
                self.image = pygame.image.load("./assets/sprites/construcciones/parra_de_vid/parra_de_vid_uvas_violetas.png")
        else:
            if etapa < 4:
                self.image = pygame.image.load("./assets/sprites/construcciones/parra_de_vid/parra_de_vid_primera_etapa.png")
            elif etapa < 8:
                self.image = pygame.image.load("./assets/sprites/construcciones/parra_de_vid/parra_de_vid_segunda_etapa.png")
            elif etapa < 15:
                self.image = pygame.image.load("./assets/sprites/construcciones/parra_de_vid/parra_de_vid_tercera_etapa.png")
            elif etapa < 21:
                self.image = pygame.image.load("./assets/sprites/construcciones/parra_de_vid/parra_de_vid_cuarta_etapa.png")
            else:
                self.image = pygame.image.load("./assets/sprites/construcciones/parra_de_vid/parra_de_vid_quinta_etapa.png")
        self.rect = self.image.get_rect(topleft=pos)
