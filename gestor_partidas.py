import sqlite3 as sql
import var_glob
from objets.construcciones.parra_de_vid import Parra_de_vid
from objets.construcciones.lagar_de_cuero import Lagar_de_cuero

class Guardado():
    def __init__(self):
        conn = sql.connect(f"./partidas/{var_glob.partida_guardada_actual}.db")
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS inventario (
                nombre_partida text,
                dias_jugados integer,
                dinero integer,
                contador_de_uvas_violetas integer,
                contador_de_uvas_amarillas integer,
                UNIQUE (nombre_partida)
            )"""
        )
        cursor.execute(f"INSERT OR IGNORE INTO Inventario VALUES('partida_guardada_uno', 0, 0, 0, 0)")
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS construcciones (
                nombre text,
                fila integer,
                columna integer,
                ancho integer,
                alto integer,
                dias_construido integer,
                dias_para_producir integer,
                produccion integer,
                recoleccion boolean,
                PRIMARY KEY (fila, columna)
                UNIQUE (fila, columna)
            )"""
        )
        cursor.execute("SELECT * from inventario")
        datos_inventario = cursor.fetchall()
        var_glob.contador_de_uvas_violetas = datos_inventario[0][3]
        conn.commit()
        conn.close()
        self.cargar_partida()

    def detectar_casillas_disponibles(fila, columna, ancho, alto):
        nuevas_casillas = set()
        for x in range(fila, fila + ancho):
            for y in range(columna, columna + alto):
                nuevas_casillas.add((x, y))
        
        conn = sql.connect(f"./partidas/{var_glob.partida_guardada_actual}.db")
        cursor = conn.cursor()
        cursor.execute("SELECT fila, columna, ancho, alto FROM construcciones")
        construcciones = cursor.fetchall()

        # Comprobar casillas ocupadas
        if not construcciones:
            return True
        if len(construcciones) >= 1:
            for c_fila, c_columna, c_ancho, c_alto in construcciones:
                casillas_ocupadas = set()
                for x in range(c_fila, c_fila + c_ancho):
                    for y in range(c_columna, c_columna + c_alto):
                        casillas_ocupadas.add((x, y))

                if nuevas_casillas & casillas_ocupadas:
                    return False
            return True
    
    def consulta_datos_de_construccion(self, fila_consulta, columna_consulta):
        conn = sql.connect(f"./partidas/{var_glob.partida_guardada_actual}.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM construcciones
            WHERE ? >= fila AND ? < fila + ancho
            AND ? >= columna AND ? < columna + alto
        """, (fila_consulta, fila_consulta, columna_consulta, columna_consulta))
        resultado = cursor.fetchone()
        if resultado == None:
            valores_construccion = None
        else:
            valores_construccion = resultado
        conn.commit()
        conn.close()
        return valores_construccion

    def guardar_construccion(nombre, fila, columna, ancho, alto):
        conn = sql.connect(f"./partidas/{var_glob.partida_guardada_actual}.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM construcciones WHERE fila=? AND columna=?", (fila, columna))
        resultado = cursor.fetchone()
        if resultado == None:
            instruccion = f"INSERT OR IGNORE INTO construcciones VALUES('{nombre}', {fila}, {columna}, {ancho}, {alto}, 0, 0, 0, 0)"
            cursor.execute(instruccion)
            conn.commit()
            conn.close()
            return True
        else:
            return False
    
    def actualizar_dias(self):
        conn = sql.connect(f"./partidas/{var_glob.partida_guardada_actual}.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE construcciones SET dias_construido = dias_construido + 1")
        cursor.execute("SELECT * FROM construcciones WHERE dias_construido < 26")
        vid_para_actualizar = cursor.fetchall()
        cursor.execute("""UPDATE construcciones
                        SET 
                            dias_para_producir = CASE 
                                WHEN dias_para_producir < 9 THEN dias_para_producir + 1 
                                ELSE 0 
                            END,
                            produccion = CASE 
                                WHEN dias_para_producir = 9 THEN produccion + 1 
                                ELSE produccion 
                            END,
                            recoleccion = CASE 
                                WHEN dias_para_producir = 9 THEN 1 
                                ELSE recoleccion
                            END
                        WHERE nombre = 'Parra' AND dias_construido > 16 AND recoleccion = 0""")
        cursor.execute("SELECT * FROM construcciones WHERE recoleccion = 1")
        vid_para_dar_uva = cursor.fetchall()

        # Crecimiento de la parra de vid
        for parra in vid_para_actualizar:
            if parra[0] == "Parra":
                x_de_la_parra = parra[1] * 24
                y_de_la_parra = parra[2] * 24 - 8
                for sprite in var_glob.sprites_de_construcciones:
                    if isinstance(sprite, Parra_de_vid) and sprite.rect.topleft == (x_de_la_parra, y_de_la_parra):
                        sprite.kill()
                Parra_de_vid((x_de_la_parra, y_de_la_parra), [var_glob.sprites_de_construcciones], parra[5], rec = False)

        # Produccion de la parra de vid
        for parra in vid_para_dar_uva:
            x_de_la_parra = parra[1] * 24
            y_de_la_parra = parra[2] * 24 - 8
            for sprite in var_glob.sprites_de_construcciones:
                if isinstance(sprite, Parra_de_vid) and sprite.rect.topleft == (x_de_la_parra, y_de_la_parra):
                    sprite.kill()
            Parra_de_vid((x_de_la_parra, y_de_la_parra), [var_glob.sprites_de_construcciones], parra[5], rec = True)
        
        # Actualizar datos de inventario
        cursor.execute("UPDATE inventario SET dias_jugados = dias_jugados + 1")
        cursor.execute("SELECT * from inventario")
        datos_inventario = cursor.fetchall()
        var_glob.dia_de_juego = datos_inventario[0][1]
        conn.commit()
        conn.close()

    def eliminar_construccion(fila_consulta, columna_consulta):
        conn = sql.connect(f"./partidas/{var_glob.partida_guardada_actual}.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM construcciones
            WHERE ? >= fila AND ? < fila + ancho
            AND ? >= columna AND ? < columna + alto
        """, (fila_consulta, fila_consulta, columna_consulta, columna_consulta))
        resultado = cursor.fetchone()
        if resultado == None:
            valores_construccion = None
        else:
            valores_construccion = (resultado[0], resultado[1], resultado[2])
            cursor.execute("DELETE FROM construcciones WHERE fila=? AND columna=?", (resultado[1], resultado[2]))
        conn.commit()
        conn.close()
        return valores_construccion

    def recoleccion_de_produccion(fila, columna):
        conn = sql.connect(f"./partidas/{var_glob.partida_guardada_actual}.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM construcciones WHERE fila=? AND columna=?", (fila, columna))
        parra = cursor.fetchone()
        if parra is None:
            pass
        else:
            if parra[8] == 1:
                for sprite in var_glob.sprites_de_construcciones:
                    x_de_la_parra = parra[1] * 24
                    y_de_la_parra = parra[2] * 24 - 8
                    if isinstance(sprite, Parra_de_vid) and sprite.rect.topleft == (x_de_la_parra, y_de_la_parra):
                        sprite.kill()
                Parra_de_vid((x_de_la_parra, y_de_la_parra), [var_glob.sprites_de_construcciones], parra[5], rec = False)
                cursor.execute("UPDATE construcciones SET recoleccion = 0 WHERE fila=? AND columna=?", (fila, columna))
                uvas_producidas = 1 # Agregar función de número random, basado en los años y calidad de la parra
                cursor.execute(f"UPDATE inventario SET contador_de_uvas_violetas = contador_de_uvas_violetas + {uvas_producidas}")
                cursor.execute("SELECT * from inventario")
                datos_inventario = cursor.fetchall()
                var_glob.contador_de_uvas_violetas = datos_inventario[0][3]

            else:
                pass
        conn.commit()
        conn.close()

    def cargar_partida(self):
        conn = sql.connect(f"./partidas/{var_glob.partida_guardada_actual}.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM construcciones")
        datos = cursor.fetchall()                                
        conn.commit()
        conn.close()
        for construccion in datos:
            if construccion[0] == "Parra":
                x_de_la_construccion = construccion[1] * 24
                y_de_la_construccion = construccion[2] * 24 - 8
                if construccion[8] == 1:
                    valor_recoleccion = True
                else:
                    valor_recoleccion = False
                Parra_de_vid((x_de_la_construccion, y_de_la_construccion), [var_glob.sprites_de_construcciones], construccion[5], rec = valor_recoleccion)
                
            if construccion[0] == "Lagar":
                x_de_la_construccion = construccion[1] * 24
                y_de_la_construccion = construccion[2] * 24
                Lagar_de_cuero((x_de_la_construccion, y_de_la_construccion), [var_glob.sprites_de_construcciones])