import pygame
import var_glob
from objets.menu.boton_jugar import Boton_menu_principal_jugar

class Menu():
    def __init__(self):
        self.x_del_menu_principal = (var_glob.ancho_pantalla - 128) // 2 #Centrar panel. ACORDARSE DE CAMBIAR ESE 610
        self.y_del_menu_principal = (var_glob.alto_pantalla - 64) //2
        self.botones_ubicacion_menu_principal = {
            1 : (self.x_del_menu_principal, self.y_del_menu_principal, var_glob.sprites_menu_principal)
        }

    def boton_jugar(self):
        if var_glob.modo_menu_inicio == True:
            Boton_menu_principal_jugar(var_glob.screen, *self.botones_ubicacion_menu_principal[1], activacion = "_true")
        elif var_glob.modo_menu_inicio == False & var_glob.modo_demolicion == False:
            Boton_menu_principal_jugar(var_glob.screen, *self.botones_ubicacion_menu_principal[1], activacion = "_false") 
