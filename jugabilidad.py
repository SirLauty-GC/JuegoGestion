import pygame
import var_glob
from cargar_mapa import Mapa
from gestor_partidas import Guardado
from objets.construcciones.parra_de_vid import Parra_de_vid

class Jugabilidad():
    def __init__(self):
        self.mamapa = Mapa
        self.guardado = Guardado
        self.guardado()
    def detectar_tile(self, mouse_x, mouse_y, offset_x, offset_y):
        global_x = mouse_x - offset_x
        global_y = mouse_y - offset_y

        tile_x = global_x // 24
        tile_y = global_y // 24

        if 0 <= tile_y < len(var_glob.mapa_cargardo) and 0 <= tile_x < len(var_glob.mapa_cargardo[0]):
            return var_glob.mapa_cargardo[tile_y][tile_x], tile_x, tile_y
        return None

    def construir(self, tile):
        if tile[0] == 'a':
            return
        else:
            #rot = var_glob.modo_const_rotada
            if var_glob.modo_const_parra_de_vid == True: # Parra de vid
                #if rot == 0 or rot == 2:
                fila, columna = tile[1], tile[2]
                tile_x, tile_y = fila * 24, columna * 24
                guardado_confirmación = self.guardado.guardar_construccion_de_parra('parra', fila, columna)
                if guardado_confirmación:
                    tile = Parra_de_vid((tile_x, tile_y-8), [var_glob.sprites_de_construcciones], 0, False)
                else:
                    pass

    def eliminar_parra(self, tile):
        fila, columna = tile[1], tile[2]
        tile_x, tile_y = fila * 24, columna * 24 - 8
        for sprite in var_glob.sprites_de_construcciones:
            if isinstance(sprite, Parra_de_vid) and sprite.rect.topleft == (tile_x, tile_y):
                sprite.kill()
        self.guardado.eliminar_construccion_de_parra(fila, columna)
        
    def recolectar_produccion(self, tile):
        fila, columna = tile[1], tile[2]
        self.guardado.recoleccion_de_produccion(fila, columna)