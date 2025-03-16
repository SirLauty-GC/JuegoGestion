import pygame
import var_glob
from objets.interfaz.panel_de_la_interfaz import Panel_de_la_interfaz
from objets.interfaz.botoncito_menu_de_objeto import Botoncito_de_menu
from objets.interfaz.texto_menu_de_objeto import Texto_de_menu

icono_boton_cerrar = pygame.image.load(f"./assets/sprites/ui/menu/icono_boton_cerrar.png")

class Menu_de_objeto():
    def __init__(self):
        self.fuente_pixel_10 = pygame.font.Font("assets/fonts/pixeled_font.ttf", 10)
        self.fuente_pixel_12 = pygame.font.Font("assets/fonts/pixeled_font.ttf", 12)
        if var_glob.menu_de_objetos_en_pantalla == True:
            self.crear_menu_de_objeto()

    def crear_menu_de_objeto(self, menu_de_objetos_valores):
        self.valores_nombre = menu_de_objetos_valores[0]
        self.valores_dias_construidos = str(menu_de_objetos_valores[5])
        self.valores_produccion = str(menu_de_objetos_valores[7])
        self.panel_del_menu = Panel_de_la_interfaz(var_glob.menu_de_objeto_rectangulos[0],
                             var_glob.ubicacion_x_del_menu_de_objetos,
                             var_glob.ubicacion_y_del_menu_de_objetos,
                             var_glob.ancho_menu_de_objetos,
                             var_glob.alto_menu_de_objetos,
                             var_glob.color_azul_oscuro)
        self.rect_panel_del_menu = self.panel_del_menu.obtener_recta()

        self.boton_cerrar(icono_boton_cerrar)
        self.crear_barra_de_titulo()
        self.texto_nombre()
        self.texto_dias_construidos()
        self.texto_produccion()

    def crear_barra_de_titulo(self):
        self.rect_barra_de_titulo = Panel_de_la_interfaz(var_glob.menu_de_objeto_rectangulos[1],
                                                    var_glob.ubicacion_x_del_menu_de_objetos,
                                                    var_glob.ubicacion_y_del_menu_de_objetos,
                                                    var_glob.ancho_menu_de_objetos,
                                                    var_glob.alto_menu_de_objetos // 16,
                                                    var_glob.color_blanco)
        self.barra_de_titulo = self.rect_barra_de_titulo.obtener_recta()
    
    def boton_cerrar(self, icono):
        self.distancia_boton_cerrar_x = var_glob.ancho_menu_de_objetos - 15
        self.distancia_boton_cerrar_y = 1
        self.ubicacion_boton_cerrar = [var_glob.ubicacion_x_del_menu_de_objetos + self.distancia_boton_cerrar_x, var_glob.ubicacion_y_del_menu_de_objetos + self.distancia_boton_cerrar_y]
        self.botoncito_cerrar = Botoncito_de_menu(var_glob.menu_de_objeto_botones_o_datos[0], self.ubicacion_boton_cerrar, icono)
        self.rectangulo_boton_cerrar = self.botoncito_cerrar.obtener_recta()

    def texto_nombre(self):
        self.sprite_texto = self.fuente_pixel_12.render(self.valores_nombre, True, var_glob.color_blanco)
        texto_ancho = self.sprite_texto.get_width()
        self.distancia_texto_nombre_y = 32
        self.distancia_texto_nombre_x = (var_glob.ancho_menu_de_objetos - texto_ancho) // 2

        self.ubicacion_texto_nombre = [var_glob.ubicacion_x_del_menu_de_objetos + self.distancia_texto_nombre_x, 
                                       var_glob.ubicacion_y_del_menu_de_objetos + self.distancia_texto_nombre_y]
        Texto_de_menu(var_glob.menu_de_objeto_texto[0], self.sprite_texto, self.ubicacion_texto_nombre)

    def texto_dias_construidos(self):
        self.distancia_dias_construidos_y = 64

        # Valor
        self.sprite_texto_valor_dias_construidos = self.fuente_pixel_10.render(self.valores_dias_construidos, True, var_glob.color_blanco)
        texto_ancho = self.sprite_texto_valor_dias_construidos.get_width()
        self.distancia_texto_valor_dias_construidos_x = var_glob.ancho_menu_de_objetos - texto_ancho - 8
        self.ubicacion_texto_valor_dias_construidos = [var_glob.ubicacion_x_del_menu_de_objetos + self.distancia_texto_valor_dias_construidos_x,
                                                       var_glob.ubicacion_y_del_menu_de_objetos + self.distancia_dias_construidos_y]
        
        # Texto
        self.distancia_texto_dias_construidos_x = 8
        self.ubicacion_texto_panel_dias_construidos = [var_glob.ubicacion_x_del_menu_de_objetos + self.distancia_texto_dias_construidos_x,
                                                  var_glob.ubicacion_y_del_menu_de_objetos + self.distancia_dias_construidos_y]
        self.sprite_texto_panel_dias_construidos = self.fuente_pixel_10.render("Días:", True, var_glob.color_blanco)

        Texto_de_menu(var_glob.menu_de_objeto_texto[1], self.sprite_texto_valor_dias_construidos, self.ubicacion_texto_valor_dias_construidos)
        Texto_de_menu(var_glob.menu_de_objeto_texto[2], self.sprite_texto_panel_dias_construidos, self.ubicacion_texto_panel_dias_construidos)

    def texto_produccion(self):
        self.distancia_produccion_y = 96

        # Valor
        self.sprite_texto_valor_produccion = self.fuente_pixel_10.render(self.valores_produccion, True, var_glob.color_blanco)
        texto_ancho = self.sprite_texto_valor_produccion.get_width()
        self.distancia_texto_valor_produccion_x = var_glob.ancho_menu_de_objetos - texto_ancho - 8
        self.ubicacion_texto_valor_produccion = [var_glob.ubicacion_x_del_menu_de_objetos + self.distancia_texto_valor_produccion_x,
                                                       var_glob.ubicacion_y_del_menu_de_objetos + self.distancia_produccion_y]
        
        # Texto
        self.distancia_texto_produccion_x = 8
        self.ubicacion_texto_panel_produccion = [var_glob.ubicacion_x_del_menu_de_objetos + self.distancia_texto_produccion_x,
                                                  var_glob.ubicacion_y_del_menu_de_objetos + self.distancia_produccion_y]
        self.sprite_texto_panel_produccion = self.fuente_pixel_10.render("Prod.:", True, var_glob.color_blanco)

        Texto_de_menu(var_glob.menu_de_objeto_texto[3], self.sprite_texto_valor_produccion, self.ubicacion_texto_valor_produccion)
        Texto_de_menu(var_glob.menu_de_objeto_texto[4], self.sprite_texto_panel_produccion, self.ubicacion_texto_panel_produccion)

    def cerrar_ventana(self):
        for sprite in var_glob.menu_de_objeto_rectangulos:
            sprite.empty()
        for sprite in var_glob.menu_de_objeto_botones_o_datos:
            sprite.empty()
        for sprite in var_glob.menu_de_objeto_texto:
            sprite.empty()

    def is_clicked(self, event):
        # Arrastrar la ventana
        if event.type == pygame.MOUSEBUTTONDOWN:            
            if self.rect_panel_del_menu.collidepoint(event.pos):
                var_glob.boton_interfaz = "panel"
                if self.rectangulo_boton_cerrar.collidepoint(event.pos):
                    self.cerrar_ventana()

                elif self.barra_de_titulo.collidepoint(event.pos):
                    var_glob.verificacion_de_arrastrando_menu = True
                    mouse_x, mouse_y = event.pos
                    self.menu_offset_x = self.barra_de_titulo.x - mouse_x
                    self.menu_offset_y = self.barra_de_titulo.y - mouse_y
                    self.boton_cerrar_offset_x = self.rectangulo_boton_cerrar.x - mouse_x
                    self.boton_cerrar_offset_y = self.rectangulo_boton_cerrar.y - mouse_y
                    

        elif event.type == pygame.MOUSEMOTION:
            if var_glob.verificacion_de_arrastrando_menu:
                mouse_x, mouse_y = event.pos
                self.barra_de_titulo.x = self.rect_panel_del_menu.x = self.ubicacion_boton_cerrar[0] = mouse_x + self.menu_offset_x
                self.barra_de_titulo.y = self.rect_panel_del_menu.y = self.ubicacion_boton_cerrar[1] = mouse_y + self.menu_offset_y
                self.rectangulo_boton_cerrar.x = self.ubicacion_boton_cerrar[0] = mouse_x + self.menu_offset_x + self.distancia_boton_cerrar_x
                self.rectangulo_boton_cerrar.y = self.ubicacion_boton_cerrar[1] = mouse_y + self.menu_offset_y + self.distancia_boton_cerrar_y

                self.ubicacion_texto_nombre[0] = mouse_x + self.menu_offset_x + self.distancia_texto_nombre_x
                self.ubicacion_texto_nombre[1] = mouse_y + self.menu_offset_y + self.distancia_texto_nombre_y

                self.ubicacion_texto_valor_dias_construidos[0] = mouse_x + self.menu_offset_x + self.distancia_texto_valor_dias_construidos_x
                self.ubicacion_texto_valor_dias_construidos[1] = mouse_y + self.menu_offset_y + self.distancia_dias_construidos_y
                self.ubicacion_texto_panel_dias_construidos[0] = mouse_x + self.menu_offset_x + self.distancia_texto_dias_construidos_x
                self.ubicacion_texto_panel_dias_construidos[1] = mouse_y + self.menu_offset_y + self.distancia_dias_construidos_y

                self.ubicacion_texto_valor_produccion[0] = mouse_x + self.menu_offset_x + self.distancia_texto_valor_produccion_x
                self.ubicacion_texto_valor_produccion[1] = mouse_y + self.menu_offset_y + self.distancia_produccion_y
                self.ubicacion_texto_panel_produccion[0] = mouse_x + self.menu_offset_x + self.distancia_texto_produccion_x
                self.ubicacion_texto_panel_produccion[1] = mouse_y + self.menu_offset_y + self.distancia_produccion_y

        elif event.type == pygame.MOUSEBUTTONUP:
            var_glob.verificacion_de_arrastrando_menu = False

        # Clickear botones 