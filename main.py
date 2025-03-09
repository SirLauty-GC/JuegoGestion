import pygame, sys
import var_glob
from menu_principal import Menu
from cargar_mapa import Mapa
from interfaz import Interfaz
from jugabilidad import Jugabilidad
from gestor_partidas import Guardado

pygame.init()

TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 1000) 

clock = pygame.time.Clock()

iniciar = True
class Juego:
    def __init__(self):
        self.menu_principal = Menu()
        self.cargar_mapa = Mapa()
        self.interfaz = Interfaz()
        self.jugabilidad = Jugabilidad()
        self.guardado = Guardado()

    def corre_juego(self):
        while iniciar:
            for event in pygame.event.get():
                # Tiempo
                if event.type == TIMER_EVENT:
                    if var_glob.modo_menu_inicio == False:
                        var_glob.segundos_de_juego = var_glob.segundos_de_juego + 1

                        if var_glob.segundos_de_juego == 10:
                            var_glob.segundos_de_juego = 0
                            self.guardado.actualizar_dias()
                            var_glob.dia_de_juego = var_glob.dia_de_juego + 1
                            print("dias de juego:", var_glob.dia_de_juego)
                            print("Uvas:", var_glob.contador_de_uvas_violetas)

                var_glob.screen.fill((155,155,155))

                if event.type == pygame.QUIT:
                    sys.exit()
                
                # Teclado
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        var_glob.modo_construccion = not var_glob.modo_construccion
                        var_glob.modo_demolicion = False
                        self.interfaz.crear_botones()

                    if event.key == pygame.K_w:
                        var_glob.modo_demolicion = not var_glob.modo_demolicion
                        var_glob.modo_construccion = False
                        var_glob.modo_const_parra_de_vid = False
                        var_glob.modo_const_lagar_de_cuero = False
                        self.interfaz.crear_botones()

                    if event.key == pygame.K_1:
                        if var_glob.modo_construccion:
                            var_glob.modo_const_parra_de_vid = not var_glob.modo_const_parra_de_vid
                            var_glob.modo_demolicion = False

                    if event.key == pygame.K_2:
                        if var_glob.modo_construccion:
                            var_glob.modo_const_lagar_de_cuero = not var_glob.modo_const_lagar_de_cuero
                            var_glob.modo_demolicion = False
                    
                    if event.key == pygame.K_SPACE:
                        if var_glob.modo_menu_inicio:
                            var_glob.modo_menu_inicio = False

                # Mouse
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if var_glob.modo_menu_inicio == False:
                            if var_glob.modo_construccion == True:
                                mouse_x, mouse_y = pygame.mouse.get_pos()
                                tile = self.jugabilidad.detectar_tile(mouse_x, mouse_y, var_glob.offset_x, var_glob.offset_y)
                                if tile:
                                    self.jugabilidad.construir(tile)

                            if var_glob.modo_demolicion == True:
                                mouse_x, mouse_y = pygame.mouse.get_pos()
                                tile = self.jugabilidad.detectar_tile(mouse_x, mouse_y, var_glob.offset_x, var_glob.offset_y)
                                if tile:
                                    self.jugabilidad.eliminar_construccion(tile)
                            
                            if var_glob.modo_construccion == False & var_glob.modo_demolicion == False:
                                mouse_x, mouse_y = pygame.mouse.get_pos()
                                tile = self.jugabilidad.detectar_tile(mouse_x, mouse_y, var_glob.offset_x, var_glob.offset_y)
                                if tile:
                                    self.jugabilidad.recolectar_produccion(tile)
                
                if self.menu_principal.is_clicked(event):
                    if var_glob.modo_menu_inicio:
                        if var_glob.boton_menu_principal == "jugar":
                            if var_glob.modo_menu_inicio:
                                var_glob.modo_menu_inicio = False
                        if var_glob.boton_menu_principal == "opciones":
                            print("opciones")
                        if var_glob.boton_menu_principal == "salir":
                            sys.exit()
                
                if self.interfaz.is_clicked(event):
                    if var_glob.modo_menu_inicio == False:
                        if var_glob.boton_interfaz == "construccion":
                            var_glob.modo_construccion = not var_glob.modo_construccion
                            var_glob.modo_const_parra_de_vid = not var_glob.modo_const_parra_de_vid
                            var_glob.modo_demolicion = False

                        if var_glob.boton_interfaz == "demolicion":
                            var_glob.modo_demolicion = not var_glob.modo_demolicion
                            var_glob.modo_construccion = False
                            var_glob.modo_const_parra_de_vid = False
                        self.interfaz.valores_interfaz()
                        self.interfaz.crear_botones()
                            
            if var_glob.modo_menu_inicio:
                self.menu_principal.panel_menu_principal()
            else:

                # Movimiento de la cámara
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if mouse_x < var_glob.limite_pantalla:  # Izquierda
                    if var_glob.offset_x < 0:
                        var_glob.offset_x += var_glob.velocidad_camara
                if mouse_x > var_glob.ancho_pantalla - var_glob.limite_pantalla:  # Derecha
                    if var_glob.offset_x > var_glob.ancho_pantalla - var_glob.ancho_mundo:
                        var_glob.offset_x -= var_glob.velocidad_camara
                if mouse_y < var_glob.limite_pantalla:  # Arriba
                    if var_glob.offset_y < 0:
                        var_glob.offset_y += var_glob.velocidad_camara
                if mouse_y > var_glob.alto_pantalla - var_glob.limite_pantalla:  # Abajo
                    if var_glob.offset_y > var_glob.alto_pantalla - var_glob.alto_mundo:
                        var_glob.offset_y -= var_glob.velocidad_camara
                self.jugabilidad.movimiento_camara()
                self.interfaz.valores_interfaz()
            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
    juego = Juego()
    juego.corre_juego()