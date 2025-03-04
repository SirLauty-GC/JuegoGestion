import pygame
import var_glob
from objets.interfaz.boton_construccion import Boton_construccion
from objets.interfaz.boton_demolicion import Boton_demolicion

x_del_panel_interfaz = (var_glob.ancho_pantalla - 610) // 2 #Centrar panel. ACORDARSE DE CAMBIAR ESE 610
y_del_panel_interfaz = var_glob.alto_pantalla - 104
botones_ubicacion = {
    1 : (x_del_panel_interfaz + 10, y_del_panel_interfaz +16, var_glob.sprites_interfaz_principal[0]),
    2 : (x_del_panel_interfaz + 84, y_del_panel_interfaz +16, var_glob.sprites_interfaz_principal[1]),
    3 : (x_del_panel_interfaz + 158, y_del_panel_interfaz +16, var_glob.sprites_interfaz_principal[2]),
    4 : (x_del_panel_interfaz + 232, y_del_panel_interfaz +16, var_glob.sprites_interfaz_principal[3]),
    5 : (x_del_panel_interfaz + 306, y_del_panel_interfaz +16, var_glob.sprites_interfaz_principal[4]),
    6 : (x_del_panel_interfaz + 380, y_del_panel_interfaz +16, var_glob.sprites_interfaz_principal[5]),
    7 : (x_del_panel_interfaz + 454, y_del_panel_interfaz +16, var_glob.sprites_interfaz_principal[6]),
    8 : (x_del_panel_interfaz + 528, y_del_panel_interfaz +16, var_glob.sprites_interfaz_principal[7])
}
class Interfaz():
    def __init__(self):
        self.crear_panel()
        self.crear_botones()

    def crear_panel(self):
        panel_interfaz = pygame.image.load("./sprites/ui/panel.png")
        var_glob.screen.blit(panel_interfaz, (x_del_panel_interfaz, y_del_panel_interfaz))

    def crear_botones(self):
        self.boton_uno(var_glob.modo_construccion, var_glob.modo_demolicion)
        self.boton_dos(var_glob.modo_demolicion, var_glob.modo_construccion)
    
    def boton_uno(self, variable_del_boton, variable_condicion):
        if variable_del_boton == True:
            Boton_construccion(var_glob.screen, *botones_ubicacion[1], activacion = "_true")
        elif variable_del_boton == False & variable_condicion == False:
            Boton_construccion(var_glob.screen, *botones_ubicacion[1], activacion = "_false")
    
    def boton_dos(self, variable_del_boton, variable_condicion):
        if variable_del_boton == True:
            Boton_demolicion(var_glob.screen, *botones_ubicacion[2], activacion = "_true")
        elif variable_del_boton == False & variable_condicion == False:
            Boton_demolicion(var_glob.screen, *botones_ubicacion[2], activacion = "_false")