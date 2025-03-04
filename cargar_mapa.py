import pygame
import csv
import var_glob
import numpy as np
from objets.terreno.mar import Mar
from objets.terreno.montana import Montana
from objets.terreno.colina import Colina
from objets.terreno.arena import Arena
from objets.terreno.pasto import Pasto
from objets.construcciones.parra_de_vid import Parra_de_vid

def leer_mapa(ruta):
    with open(ruta, newline='') as archivo:
        reader = csv.reader(archivo)
        return [list(row) for row in reader]

class Mapa():
    def __init__(self):
        var_glob.mapa_cargardo = leer_mapa("./objets/mapa-cuyo.csv")
        self.crear_mapa()

    def crear_mapa(self):
        tipos_terreno= {
            "a": Mar,
            "m": Montana,
            "c": Colina,
            "s": Arena,
            "l": Pasto
        }
        for row_index_r, row in enumerate(var_glob.mapa_cargardo):
            for col_index_r, col in enumerate(row):
                if col in tipos_terreno:
                    x = col_index_r * 24
                    y = row_index_r * 24
                    tipos_terreno[col]((x, y), [var_glob.sprites_de_fondo])
        var_glob.ancho_mundo = (col_index_r + 1) * 24
        var_glob.alto_mundo = (row_index_r + 1) * 24