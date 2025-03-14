import pygame
import var_glob
from objets.interfaz.panel_de_la_interfaz import Panel_de_la_interfaz
from objets.interfaz.boton_de_interfaz import Boton_de_interfaz
from objets.interfaz.iconos_interfaz import Iconos_interfaz

x_del_panel_interfaz = 0 # (var_glob.ancho_pantalla - 610) // 2 #Centrar panel. ACORDARSE DE CAMBIAR ESE 610
y_del_panel_interfaz = var_glob.alto_pantalla - 48

botones_ubicacion = {
    1 : {
        "boton": (x_del_panel_interfaz + 16, y_del_panel_interfaz + 4),
        "grupos_sprite": [var_glob.sprites_interfaz_principal[1],var_glob.sprites_interfaz_principal[2],var_glob.sprites_interfaz_principal[3]],
        "texto": (x_del_panel_interfaz + 52, y_del_panel_interfaz + 8)},
    2 : {
        "boton": (x_del_panel_interfaz + 160, y_del_panel_interfaz + 4),
        "grupos_sprite": [var_glob.sprites_interfaz_principal[4],var_glob.sprites_interfaz_principal[5],var_glob.sprites_interfaz_principal[6]],
        "texto": (x_del_panel_interfaz + 196, y_del_panel_interfaz + 8)},
    3 : {
        "boton": (x_del_panel_interfaz + 304, y_del_panel_interfaz + 4),
        "grupos_sprite": [var_glob.sprites_interfaz_principal[7],var_glob.sprites_interfaz_principal[8],var_glob.sprites_interfaz_principal[9]],
        "texto": (x_del_panel_interfaz + 340, y_del_panel_interfaz + 8)},
    4 : {
        "boton": (x_del_panel_interfaz + 448, y_del_panel_interfaz + 4),
        "grupos_sprite": [var_glob.sprites_interfaz_principal[10],var_glob.sprites_interfaz_principal[11],var_glob.sprites_interfaz_principal[12]],
        "texto": (x_del_panel_interfaz + 484, y_del_panel_interfaz + 8)},
    5 : {
        "boton": (x_del_panel_interfaz + 592, y_del_panel_interfaz + 4),
        "grupos_sprite": [var_glob.sprites_interfaz_principal[13],var_glob.sprites_interfaz_principal[14],var_glob.sprites_interfaz_principal[15]],
        "texto": (x_del_panel_interfaz + 628, y_del_panel_interfaz + 8)}
    }

interfaz_valores_ubicacion = {
    1 : {
        "boton": (x_del_panel_interfaz + 736, y_del_panel_interfaz + 4),
        "grupos_sprite": [var_glob.sprites_interfaz_principal[16],var_glob.sprites_interfaz_principal[17],var_glob.sprites_interfaz_principal[18]],
        "texto": (x_del_panel_interfaz + 756, y_del_panel_interfaz + 8)},
    2 : {
        "boton": (x_del_panel_interfaz + 832, y_del_panel_interfaz + 4),
        "grupos_sprite": [var_glob.sprites_interfaz_principal[19],var_glob.sprites_interfaz_principal[20],var_glob.sprites_interfaz_principal[21]],
        "texto": (x_del_panel_interfaz + 852, y_del_panel_interfaz + 8)},
    3 : {
        "boton": (x_del_panel_interfaz + 928, y_del_panel_interfaz + 4),
        "grupos_sprite": [var_glob.sprites_interfaz_principal[22],var_glob.sprites_interfaz_principal[23],var_glob.sprites_interfaz_principal[24]],
        "texto": (x_del_panel_interfaz + 948, y_del_panel_interfaz + 8)}
    }

icono_construccion = pygame.image.load(f"./assets/sprites/ui/icono_construccion.png")
icono_demolicion = pygame.image.load(f"./assets/sprites/ui/icono_demolicion.png")
icono_uvas_violetas = pygame.image.load(f"./assets/sprites/ui/iconos/icono_de_uva_violeta.png")
icono_uvas_amarillas = pygame.image.load(f"./assets/sprites/ui/iconos/icono_de_uva_amarilla.png")

color_texto = var_glob.color_blanco

class Interfaz():
    def __init__(self):
        self.crear_botones()

    def crear_botones(self):
        Panel_de_la_interfaz(var_glob.sprites_interfaz_principal[0],x_del_panel_interfaz, y_del_panel_interfaz)
        self.boton_uno(icono_construccion, "CONSTRUIR", var_glob.modo_construccion, var_glob.modo_demolicion)
        self.boton_dos(icono_demolicion, "DEMOLER", var_glob.modo_demolicion, var_glob.modo_construccion)
        self.valores_interfaz()

    def boton_uno(self, icono, texto, variable_del_boton, variable_condicion):
        self.rectangulo_boton_uno = icono.get_rect(topleft = botones_ubicacion[1]["boton"])
        if variable_del_boton:
            verificacion = pygame.image.load(f"./assets/sprites/ui/icono_true.png")
        elif variable_del_boton == False & variable_condicion == False:
            verificacion = pygame.image.load(f"./assets/sprites/ui/icono_false.png")

        Boton_de_interfaz(botones_ubicacion[1]["grupos_sprite"],verificacion, botones_ubicacion[1]["boton"], icono, texto, color_texto, botones_ubicacion[1]["texto"])

    def boton_dos(self, icono, texto, variable_del_boton, variable_condicion):
        self.rectangulo_boton_dos = icono.get_rect(topleft = botones_ubicacion[2]["boton"])
        if variable_del_boton:
            verificacion = pygame.image.load(f"./assets/sprites/ui/icono_true.png")
        elif variable_del_boton == False & variable_condicion == False:
            verificacion = pygame.image.load(f"./assets/sprites/ui/icono_false.png")

        Boton_de_interfaz(botones_ubicacion[2]["grupos_sprite"],verificacion, botones_ubicacion[2]["boton"], icono, texto, color_texto, botones_ubicacion[2]["texto"])

    def valores_interfaz(self):
        Iconos_interfaz(interfaz_valores_ubicacion[2]["grupos_sprite"], interfaz_valores_ubicacion[2]["boton"], icono_uvas_violetas, var_glob.contador_de_uvas_violetas, color_texto, interfaz_valores_ubicacion[2]["texto"])
        Iconos_interfaz(interfaz_valores_ubicacion[3]["grupos_sprite"], interfaz_valores_ubicacion[3]["boton"], icono_uvas_amarillas, var_glob.contador_de_uvas_amarillas, color_texto, interfaz_valores_ubicacion[3]["texto"])
    
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rectangulo_boton_uno.collidepoint(event.pos):
                var_glob.boton_interfaz = "construccion"
                return True
            elif self.rectangulo_boton_dos.collidepoint(event.pos):
                var_glob.boton_interfaz = "demolicion"
                return True
            else:
                return False