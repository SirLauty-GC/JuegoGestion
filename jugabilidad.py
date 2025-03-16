import pygame
import var_glob
from cargar_mapa import Mapa
from gestor_partidas import Guardado
from objets.construcciones.parra_de_vid import Parra_de_vid
from objets.construcciones.lagar_de_cuero import Lagar_de_cuero

class Jugabilidad():
    def __init__(self):
        self.mamapa = Mapa
        self.guardado = Guardado
        self.guardado()

    def movimiento_camara(self):
        var_glob.sprites_de_fondo.update()
        for sprite in var_glob.sprites_de_fondo:
            var_glob.complete_screen.blit(sprite.image, (sprite.rect.x + var_glob.offset_x, sprite.rect.y + var_glob.offset_y))
        for sprite in var_glob.sprites_de_construcciones:
            var_glob.complete_screen.blit(sprite.image, (sprite.rect.x + var_glob.offset_x, sprite.rect.y + var_glob.offset_y))
        
        # Interfaz 
        
        for sprites in var_glob.menu_de_objeto_rectangulos:
            if sprites:
                for sprite in sprites:
                    if sprite:
                        pygame.draw.rect(var_glob.complete_screen, sprite.color, sprite.sprite_icono)
        for sprites in var_glob.menu_de_objeto_botones_o_datos:
            if sprites:
                for sprite in sprites:
                    if sprite:
                        var_glob.complete_screen.blit(sprite.sprite_icono, sprite.ubicacion_x_y)
        for sprites in var_glob.menu_de_objeto_texto:
            if sprites:
                for sprite in sprites:
                    if sprite:
                        var_glob.complete_screen.blit(sprite.sprite_texto, sprite.text_rect)

        for sprites in var_glob.rectangulos_interfaz_principal:
            for sprite in sprites:
                pygame.draw.rect(var_glob.complete_screen, var_glob.color_azul_oscuro, sprite.sprite_icono)

        for sprites in var_glob.sprites_interfaz_principal:
            for sprite in sprites:
                var_glob.complete_screen.blit(sprite.sprite_verific, sprite.ubicacion_x_y)
                var_glob.complete_screen.blit(sprite.sprite_texto, sprite.text_ubic)
                var_glob.complete_screen.blit(sprite.sprite_icono, sprite.ubicacion_x_y)
                
    def detectar_tile(self, mouse_x, mouse_y, offset_x, offset_y):
        global_x = mouse_x - offset_x
        global_y = mouse_y - offset_y

        tile_x = global_x // 24
        tile_y = global_y // 24

        if 0 <= tile_y < len(var_glob.mapa_cargardo) and 0 <= tile_x < len(var_glob.mapa_cargardo[0]):
            return var_glob.mapa_cargardo[tile_y][tile_x], tile_x, tile_y
        else:
            return None

    def construir(self, tile):
        if tile[0] == 'a':
            return
        else:
            fila, columna = tile[1], tile[2]
            tile_x, tile_y = fila * 24, columna * 24
            if var_glob.modo_const_parra_de_vid == True: # Parra de vid
                verificacion = self.guardado.detectar_casillas_disponibles(fila, columna, 1, 1) #fila, columna, ancho, alto
                if verificacion:
                    guardado_confirmación = self.guardado.guardar_construccion('Parra', fila, columna, 1, 1)
                    if guardado_confirmación:
                        tile = Parra_de_vid((tile_x, tile_y-8), [var_glob.sprites_de_construcciones], 0, False)
                    else:
                        pass

            elif var_glob.modo_const_lagar_de_cuero == True: # Lagares
                verificacion = self.guardado.detectar_casillas_disponibles(fila, columna, 2, 1) #fila, columna, ancho, alto
                if verificacion:
                    guardado_confirmación = self.guardado.guardar_construccion('Lagar', fila, columna, 2, 1)
                    if guardado_confirmación:
                        tile = Lagar_de_cuero((tile_x, tile_y), [var_glob.sprites_de_construcciones])
                    else:
                        pass
                
    def eliminar_construccion(self, tile):
        fila, columna = tile[1], tile[2]
        valores_construccion = self.guardado.eliminar_construccion(fila, columna)
        lista_de_construcciones = [Parra_de_vid, Lagar_de_cuero]
        if valores_construccion:
            tile_x, tile_y = valores_construccion[1] * 24, valores_construccion[2] * 24
            for sprite in var_glob.sprites_de_construcciones:
                for construccion in lista_de_construcciones:
                    if valores_construccion[0] == 'Parra':
                        if isinstance(sprite, construccion) and sprite.rect.topleft == (tile_x, tile_y - 8):
                            sprite.kill()
                    else:
                        if isinstance(sprite, construccion) and sprite.rect.topleft == (tile_x, tile_y):
                            sprite.kill()
    
    def recolectar_produccion(self, tile):
        fila, columna = tile[1], tile[2]
        self.guardado.recoleccion_de_produccion(fila, columna)