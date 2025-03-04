import pygame, sys
import var_glob
from menu_principal import Menu
from cargar_mapa import Mapa
from interfaz import Interfaz
from jugabilidad import Jugabilidad
from gestor_partidas import Guardado

pygame.init()

# Configuración de pantalla
limite_pantalla = 48
velocidad_camara = 8

TIMER_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_EVENT, 1000) 

clock = pygame.time.Clock()
def movimiento_camara():
    var_glob.sprites_de_fondo.update()
    for sprite in var_glob.sprites_de_fondo:
        var_glob.screen.blit(sprite.image, (sprite.rect.x + var_glob.offset_x, sprite.rect.y + var_glob.offset_y))
    for sprite in var_glob.sprites_de_construcciones:
        var_glob.screen.blit(sprite.image, (sprite.rect.x + var_glob.offset_x, sprite.rect.y + var_glob.offset_y))
    for sprites in var_glob.sprites_interfaz_principal:
        for sprite in sprites:
            var_glob.screen.blit(sprite.icono, (sprite.rect.x, sprite.rect.y))

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
                if event.type == TIMER_EVENT:
                    if var_glob.modo_menu_inicio == False:
                        var_glob.segundos_de_juego = var_glob.segundos_de_juego + 1

                        if var_glob.segundos_de_juego == 1:
                            var_glob.segundos_de_juego = 0
                            self.guardado.actualizar_dias()
                            var_glob.dia_de_juego = var_glob.dia_de_juego + 1
                            print("dias de juego:", var_glob.dia_de_juego)
                            print("Uvas:", var_glob.contador_de_uvas)

                var_glob.screen.fill((155,155,155))

                if event.type == pygame.QUIT:
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        var_glob.modo_construccion = not var_glob.modo_construccion
                        var_glob.modo_const_parra_de_vid = not var_glob.modo_const_parra_de_vid
                        var_glob.modo_demolicion = False
                        self.interfaz.crear_botones()

                    if event.key == pygame.K_w:
                        var_glob.modo_demolicion = not var_glob.modo_demolicion
                        var_glob.modo_construccion = False
                        var_glob.modo_const_parra_de_vid = False
                        self.interfaz.crear_botones()
                    
                    
                    if event.key == pygame.K_SPACE:
                        if var_glob.modo_menu_inicio:
                            var_glob.modo_menu_inicio = False

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
                                        self.jugabilidad.eliminar_parra(tile)
                                
                                if var_glob.modo_construccion == False & var_glob.modo_demolicion == False:
                                    mouse_x, mouse_y = pygame.mouse.get_pos()
                                    tile = self.jugabilidad.detectar_tile(mouse_x, mouse_y, var_glob.offset_x, var_glob.offset_y)
                                    if tile:
                                        self.jugabilidad.recolectar_produccion(tile)
                            
            if var_glob.modo_menu_inicio:
                self.menu_principal.boton_jugar()
            else:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if mouse_x < limite_pantalla:  # Izquierda
                    if var_glob.offset_x < 0:
                        var_glob.offset_x += velocidad_camara
                if mouse_x > var_glob.ancho_pantalla - limite_pantalla:  # Derecha
                    if var_glob.offset_x > var_glob.ancho_pantalla - var_glob.ancho_mundo:
                        var_glob.offset_x -= velocidad_camara
                if mouse_y < limite_pantalla:  # Arriba
                    if var_glob.offset_y < 0:
                        var_glob.offset_y += velocidad_camara
                if mouse_y > var_glob.alto_pantalla - limite_pantalla:  # Abajo
                    if var_glob.offset_y > var_glob.alto_pantalla - var_glob.alto_mundo:
                        var_glob.offset_y -= velocidad_camara
                
                movimiento_camara()
                
            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
    juego = Juego()
    juego.corre_juego()