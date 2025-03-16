import pygame
import var_glob

class Menu():
    def __init__(self):
        self.x_del_menu_principal = (var_glob.ancho_pantalla - 260) // 2 #Centrar panel. ACORDARSE DE CAMBIAR ESE 610
        self.y_del_menu_principal = (var_glob.alto_pantalla - 300) //2
        self.botones_ubicacion_menu_principal = {
            1 : (self.x_del_menu_principal + 20, self.y_del_menu_principal + 20, 220, 80),
            2 : (self.x_del_menu_principal + 20, self.y_del_menu_principal + 110, 220, 80),
            3 : (self.x_del_menu_principal + 20, self.y_del_menu_principal + 200, 220, 80)
        }
    
    def panel_menu_principal(self):
        self.rectangulo_panel_menu_principal = pygame.Rect(self.x_del_menu_principal, self.y_del_menu_principal, 260, 300)
        color = var_glob.color_negro

        pygame.draw.rect(var_glob.complete_screen, color, self.rectangulo_panel_menu_principal)
        self.boton_jugar()
        self.boton_opciones()
        self.boton_salir()

    def boton_jugar(self):
        self.rectangulo_boton_jugar = pygame.Rect(*self.botones_ubicacion_menu_principal[1])
        color = var_glob.color_borravino
        text = "Jugar"
        font = pygame.font.Font("assets/fonts/pixeled_font.ttf", 24)
        text_color = var_glob.color_blanco

        pygame.draw.rect(var_glob.complete_screen, color, self.rectangulo_boton_jugar)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=self.rectangulo_boton_jugar.center)
        var_glob.complete_screen.blit(text_surface, text_rect)

    def boton_opciones(self):
        self.rectangulo_boton_opciones = pygame.Rect(*self.botones_ubicacion_menu_principal[2])
        color = var_glob.color_borravino
        text = "Opciones"
        font = pygame.font.Font("assets/fonts/pixeled_font.ttf", 24)
        text_color = var_glob.color_blanco

        pygame.draw.rect(var_glob.complete_screen, color, self.rectangulo_boton_opciones)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=self.rectangulo_boton_opciones.center)
        var_glob.complete_screen.blit(text_surface, text_rect)

    def boton_salir(self):
        self.rectangulo_boton_salir = pygame.Rect(*self.botones_ubicacion_menu_principal[3])
        color = var_glob.color_borravino
        text = "Salir"
        font = pygame.font.Font("assets/fonts/pixeled_font.ttf", 24)
        text_color = var_glob.color_blanco

        pygame.draw.rect(var_glob.complete_screen, color, self.rectangulo_boton_salir)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(center=self.rectangulo_boton_salir.center)
        var_glob.complete_screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rectangulo_boton_jugar.collidepoint(event.pos):
                var_glob.boton_menu_principal = "jugar"
                return True
            elif self.rectangulo_boton_opciones.collidepoint(event.pos):
                var_glob.boton_menu_principal = "opciones"
                return True
            elif self.rectangulo_boton_salir.collidepoint(event.pos):
                var_glob.boton_menu_principal = "salir"
                return True
            else:
                return False