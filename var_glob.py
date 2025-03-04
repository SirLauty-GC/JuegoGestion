import pygame


offset_x = 0
offset_y = 0

ancho_pantalla = 1024
alto_pantalla = 640

ancho_mundo = 0
alto_mundo = 0

screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

partida_guardada_actual = "partida_guardada_uno"

# Mapa
mapa_cargardo = "."
partida_guardada = "."

# Inventario
contador_de_uvas = 0

# Tiempo
segundos_de_juego = 0
dia_de_juego = 0

# Modos
modo_menu_inicio = True

modo_construccion = False
modo_demolicion = False

# Construccion
modo_const_parra_de_vid = False

# Sprites grupos
sprites_de_fondo = pygame.sprite.Group()
sprites_de_construcciones = pygame.sprite.Group()

sprites_menu_principal = pygame.sprite.Group()

interfaz_principal_boton_1 = pygame.sprite.GroupSingle()
interfaz_principal_boton_2 = pygame.sprite.GroupSingle()
interfaz_principal_boton_3 = pygame.sprite.GroupSingle()
interfaz_principal_boton_4 = pygame.sprite.GroupSingle()
interfaz_principal_boton_5 = pygame.sprite.GroupSingle()
interfaz_principal_boton_6 = pygame.sprite.GroupSingle()
interfaz_principal_boton_7 = pygame.sprite.GroupSingle()
interfaz_principal_boton_8 = pygame.sprite.GroupSingle()
sprites_interfaz_principal = [interfaz_principal_boton_1,interfaz_principal_boton_2,interfaz_principal_boton_3,interfaz_principal_boton_4,interfaz_principal_boton_5,interfaz_principal_boton_6,interfaz_principal_boton_7,interfaz_principal_boton_8]