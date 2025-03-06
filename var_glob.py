import pygame

# Pantalla y movimiento de la cámara
offset_x = 0
offset_y = 0

ancho_pantalla = 1024
alto_pantalla = 640

limite_pantalla = 48
velocidad_camara = 8

ancho_mundo = 0
alto_mundo = 0

screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

partida_guardada_actual = "partida_guardada_uno"

# Botones
boton_menu_principal = ""
boton_interfaz = ""

# Mapa
mapa_cargardo = "."
partida_guardada = "."

# Inventario
contador_de_uvas_violetas = 0
contador_de_uvas_amarillas = 0

# Tiempo
segundos_de_juego = 0
dia_de_juego = 0

# Modos
modo_menu_inicio = True

modo_construccion = False
modo_demolicion = False

# Construccion
modo_const_parra_de_vid = False

# Colores
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)
color_borravino = (128, 0, 64)

# Sprites grupos
sprites_de_fondo = pygame.sprite.Group()
sprites_de_construcciones = pygame.sprite.Group()

sprites_menu_principal = pygame.sprite.Group()

interfaz_principal_panel = pygame.sprite.GroupSingle()
interfaz_principal_boton_1_icono = pygame.sprite.GroupSingle()
interfaz_principal_boton_1_verif = pygame.sprite.GroupSingle()
interfaz_principal_boton_1_texto = pygame.sprite.GroupSingle()
interfaz_principal_boton_2_icono = pygame.sprite.GroupSingle()
interfaz_principal_boton_2_verif = pygame.sprite.GroupSingle()
interfaz_principal_boton_2_texto = pygame.sprite.GroupSingle()
interfaz_principal_boton_3_icono = pygame.sprite.GroupSingle()
interfaz_principal_boton_3_verif = pygame.sprite.GroupSingle()
interfaz_principal_boton_3_texto = pygame.sprite.GroupSingle()
interfaz_principal_boton_4_icono = pygame.sprite.GroupSingle()
interfaz_principal_boton_4_verif = pygame.sprite.GroupSingle()
interfaz_principal_boton_4_texto = pygame.sprite.GroupSingle()
interfaz_principal_boton_5_icono = pygame.sprite.GroupSingle()
interfaz_principal_boton_5_verif = pygame.sprite.GroupSingle()
interfaz_principal_boton_5_texto = pygame.sprite.GroupSingle()
interfaz_principal_boton_6_icono = pygame.sprite.GroupSingle()
interfaz_principal_boton_6_verif = pygame.sprite.GroupSingle()
interfaz_principal_boton_6_texto = pygame.sprite.GroupSingle()
interfaz_principal_boton_7_icono = pygame.sprite.GroupSingle()
interfaz_principal_boton_7_verif = pygame.sprite.GroupSingle()
interfaz_principal_boton_7_texto = pygame.sprite.GroupSingle()
interfaz_principal_boton_8_icono = pygame.sprite.GroupSingle()
interfaz_principal_boton_8_verif = pygame.sprite.GroupSingle()
interfaz_principal_boton_8_texto = pygame.sprite.GroupSingle()
sprites_interfaz_principal = [interfaz_principal_panel,
                              interfaz_principal_boton_1_icono, interfaz_principal_boton_1_verif, interfaz_principal_boton_1_texto,
                              interfaz_principal_boton_2_icono, interfaz_principal_boton_2_verif, interfaz_principal_boton_2_texto,
                              interfaz_principal_boton_3_icono, interfaz_principal_boton_3_verif, interfaz_principal_boton_3_texto,
                              interfaz_principal_boton_4_icono, interfaz_principal_boton_4_verif, interfaz_principal_boton_4_texto,
                              interfaz_principal_boton_5_icono, interfaz_principal_boton_5_verif, interfaz_principal_boton_5_texto,
                              interfaz_principal_boton_6_icono, interfaz_principal_boton_6_verif, interfaz_principal_boton_6_texto,
                              interfaz_principal_boton_7_icono, interfaz_principal_boton_7_verif, interfaz_principal_boton_7_texto,
                              interfaz_principal_boton_8_icono, interfaz_principal_boton_8_verif, interfaz_principal_boton_8_texto,
                              ]