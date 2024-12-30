import os
import sqlite3

# Ruta de la base de datos en la carpeta 'db' dentro del proyecto
DB_PATH = os.path.join(os.path.dirname(__file__),'inventario.db')

def conectar():
    # Conexion a la base de datos
    return sqlite3.connect(DB_PATH)

def inicializar_db():

    # Crear la tabla si no existe
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT,
            bajo_stock INTEGER NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

