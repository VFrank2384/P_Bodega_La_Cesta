import mysql.connector
from mysql.connector import Error
from config.db_config import DB_CONFIG

def obtener_conexion():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"Error de conexión: {e}")
        return None

def obtener_inventario_db():
    conexion = obtener_conexion()
    if not conexion: 
        return []
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, stock, stock_minimo FROM productos")
        return cursor.fetchall()
    finally:
        conexion.close()

def actualizar_stock_db(id_producto, nuevo_stock):
    conexion = obtener_conexion()
    if not conexion: 
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("UPDATE productos SET stock = %s WHERE id = %s", (nuevo_stock, id_producto))
        conexion.commit()
        return True
    except Error:
        return False
    finally:
        conexion.close()

def agregar_producto_db(nombre, stock, stock_minimo):
    conexion = obtener_conexion()
    if not conexion: 
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (nombre, stock, stock_minimo) VALUES (%s, %s, %s)", (nombre, stock, stock_minimo))
        conexion.commit()
        return True
    except Error:
        return False
    finally:
        conexion.close()