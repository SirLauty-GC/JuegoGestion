import sqlite3 as sql
import var_glob
from objets.construcciones.parra_de_vid import Parra_de_vid

class Guardado():
    def __init__(self):
        conn = sql.connect(f"./partidas/{var_glob.partida_guardada_actual}.db")
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS inventario (
                nombre_partida text,
                dias_jugados integer,
                dinero integer,
                contador_de_uvas integer,
                UNIQUE (nombre_partida)
            )"""
        )
        cursor.execute(f"INSERT OR IGNORE INTO Inventario VALUES('partida_guardada_uno', 0, 0, 0)")
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS viñedos (
                nombre text,
                fila integer,
                columna integer,
                dias_construido integer,
                dias_para_producir integer,
                produccion integer,
                recoleccion boolean,
                PRIMARY KEY (fila, columna)
                UNIQUE (fila, columna)
            )"""
        )
        conn.commit()
        conn.close()
        self.cargar_partida()
    
    def guardar_construccion_de_parra(nombre, fila, columna):
        conn = sql.connect(f"./partidas/{var_glob.partida_guardada_actual}.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM viñedos WHERE fila=? AND columna=?", (fila, columna))
        resultado = cursor.fetchone()
        if resultado == None:
            instruccion = f"INSERT OR IGNORE INTO viñedos VALUES('{nombre}', {fila}, {columna}, 0, 0, 0, 0)"
            cursor.execute(instruccion)
            conn.commit()
            conn.close()
            return True
        else:
            return False
    
    def actualizar_dias(self):
        conn = sql.connect(f"./partidas/{var_glob.partida_guardada_actual}.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE viñedos SET dias_construido = dias_construido + 1")
        cursor.execute(f"SELECT * FROM viñedos")
        datos = cursor.fetchall()
        cursor.execute("SELECT * FROM viñedos WHERE dias_construido < 26")
        vid_para_actualizar = cursor.fetchall()
        cursor.execute("""UPDATE viñedos
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
                        WHERE dias_construido > 16 AND recoleccion = 0""")
        cursor.execute("SELECT * FROM viñedos WHERE recoleccion = 1")
        vid_para_dar_uva = cursor.fetchall()

        # Crecimiento de la parra de vid
        for parra in vid_para_actualizar:
            if parra[0] == "parra":
                x_de_la_parra = parra[1] * 24
                y_de_la_parra = parra[2] * 24 - 8
                for sprite in var_glob.sprites_de_construcciones:
                    if isinstance(sprite, Parra_de_vid) and sprite.rect.topleft == (x_de_la_parra, y_de_la_parra):
                        sprite.kill()
                Parra_de_vid((x_de_la_parra, y_de_la_parra), [var_glob.sprites_de_construcciones], parra[3], rec = False)

        # Produccion de la parra de vid
        for parra in vid_para_dar_uva:
            x_de_la_parra = parra[1] * 24
            y_de_la_parra = parra[2] * 24 - 8
            for sprite in var_glob.sprites_de_construcciones:
                if isinstance(sprite, Parra_de_vid) and sprite.rect.topleft == (x_de_la_parra, y_de_la_parra):
                    sprite.kill()
            Parra_de_vid((x_de_la_parra, y_de_la_parra), [var_glob.sprites_de_construcciones], parra[3], rec = True)
        
        # Actualizar datos de inventario
        cursor.execute("UPDATE inventario SET dias_jugados = dias_jugados + 1")
        cursor.execute("SELECT * from inventario")
        datos_inventario = cursor.fetchall()
        var_glob.dia_de_juego = datos_inventario[0][1]
        conn.commit()
        conn.close()

    def eliminar_construccion_de_parra(fila, columna):
        conn = sql.connect(f"./partidas/{var_glob.partida_guardada_actual}.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM viñedos WHERE fila=? AND columna=?", (fila, columna))
        resultado = cursor.fetchone()
        if resultado == None:
            pass
        else:
            cursor.execute("DELETE FROM viñedos WHERE fila=? AND columna=?", (fila, columna))
        conn.commit()
        conn.close()

    def recoleccion_de_produccion(fila, columna):
        conn = sql.connect(f"./partidas/{var_glob.partida_guardada_actual}.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM viñedos WHERE fila=? AND columna=?", (fila, columna))
        parra = cursor.fetchone()
        if parra is None:
            pass
        else:
            if parra[6] == 1:
                print("recoleccion efectuada")
                for sprite in var_glob.sprites_de_construcciones:
                    x_de_la_parra = parra[1] * 24
                    y_de_la_parra = parra[2] * 24 - 8
                    if isinstance(sprite, Parra_de_vid) and sprite.rect.topleft == (x_de_la_parra, y_de_la_parra):
                        sprite.kill()
                Parra_de_vid((x_de_la_parra, y_de_la_parra), [var_glob.sprites_de_construcciones], parra[3], rec = False)
                cursor.execute("UPDATE viñedos SET recoleccion = 0 WHERE fila=? AND columna=?", (fila, columna))
                uvas_producidas = 1 # Agregar función de número random, basado en los años y calidad de la parra
                cursor.execute(f"UPDATE inventario SET contador_de_uvas = contador_de_uvas + {uvas_producidas}")
                cursor.execute("SELECT * from inventario")
                datos_inventario = cursor.fetchall()
                var_glob.contador_de_uvas = datos_inventario[0][3]

            else:
                print("a")
                pass
        conn.commit()
        conn.close()

    def cargar_partida(self):
        conn = sql.connect(f"./partidas/{var_glob.partida_guardada_actual}.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM viñedos")
        datos = cursor.fetchall()                                
        conn.commit()
        conn.close()
        for parra in datos:
            if parra[0] == "parra":
                x_de_la_parra = parra[1] * 24
                y_de_la_parra = parra[2] * 24 - 8
                if parra[6] == 1:
                    valor_recoleccion = True
                else:
                    valor_recoleccion = False
                Parra_de_vid((x_de_la_parra, y_de_la_parra), [var_glob.sprites_de_construcciones], parra[3], rec = valor_recoleccion)