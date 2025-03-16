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
complete_screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla + 48))

partida_guardada_actual = "partida_guardada_uno"

# Botones
boton_menu_principal = ""
boton_interfaz = ""

# Mapa
mapa_cargardo = "."
partida_guardada = "."

# Inventario y gestion
contador_de_uvas_violetas = 0
contador_de_uvas_amarillas = 0

# Tiempo
segundos_de_juego = 0
dia_de_juego = 0

# Modos
modo_menu_inicio = True

modo_construccion = False
modo_demolicion = False
modo_recoleccion = False

# Construccion
modo_const_parra_de_vid = False
modo_const_lagar_de_cuero = False

# Colores
color_blanco = (255, 255, 255)
color_negro = (0, 0, 0)
color_azul_oscuro = (31, 52, 96)
color_borravino = (128, 0, 64)

# Menu pequeño de objetos
menu_de_objetos_en_pantalla = False
menu_de_objetos_valores = []
ancho_menu_de_objetos = 128
alto_menu_de_objetos = 256
ubicacion_x_del_menu_de_objetos = 16
ubicacion_y_del_menu_de_objetos = (alto_pantalla - 256) // 2
menu_de_objeto_accion = ""
verificacion_de_arrastrando_menu = False

menu_de_objeto_panel_1 = pygame.sprite.GroupSingle()
menu_de_objeto_panel_2 = pygame.sprite.GroupSingle()
menu_de_objeto_rectangulos = [menu_de_objeto_panel_1, menu_de_objeto_panel_2]

menu_de_objeto_panel_boton_cerrar = pygame.sprite.GroupSingle()
menu_de_objeto_botones_o_datos = [menu_de_objeto_panel_boton_cerrar]

menu_de_objeto_panel_texto_1 = pygame.sprite.GroupSingle()
menu_de_objeto_panel_texto_2 = pygame.sprite.GroupSingle()
menu_de_objeto_panel_texto_3 = pygame.sprite.GroupSingle()
menu_de_objeto_panel_texto_4 = pygame.sprite.GroupSingle()
menu_de_objeto_panel_texto_5 = pygame.sprite.GroupSingle()
menu_de_objeto_texto = [menu_de_objeto_panel_texto_1, menu_de_objeto_panel_texto_2,
                        menu_de_objeto_panel_texto_3, menu_de_objeto_panel_texto_4,
                        menu_de_objeto_panel_texto_5]

# Sprites grupos
sprites_de_fondo = pygame.sprite.Group()
sprites_de_construcciones = pygame.sprite.Group()

sprites_menu_principal = pygame.sprite.Group()

interfaz_principal_panel = pygame.sprite.GroupSingle()
rectangulos_interfaz_principal = [interfaz_principal_panel]

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

sprites_interfaz_principal = [interfaz_principal_boton_1_icono, interfaz_principal_boton_1_verif, interfaz_principal_boton_1_texto,
                              interfaz_principal_boton_2_icono, interfaz_principal_boton_2_verif, interfaz_principal_boton_2_texto,
                              interfaz_principal_boton_3_icono, interfaz_principal_boton_3_verif, interfaz_principal_boton_3_texto,
                              interfaz_principal_boton_4_icono, interfaz_principal_boton_4_verif, interfaz_principal_boton_4_texto,
                              interfaz_principal_boton_5_icono, interfaz_principal_boton_5_verif, interfaz_principal_boton_5_texto,
                              interfaz_principal_boton_6_icono, interfaz_principal_boton_6_verif, interfaz_principal_boton_6_texto,
                              interfaz_principal_boton_7_icono, interfaz_principal_boton_7_verif, interfaz_principal_boton_7_texto,
                              interfaz_principal_boton_8_icono, interfaz_principal_boton_8_verif, interfaz_principal_boton_8_texto,
                              ]