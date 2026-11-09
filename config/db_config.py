import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': os.getenv('DB_PASSWORD'),  # Lee la contraseña de forma segura
    'database': 'bodega_la_cesta'
}

STOCK_MINIMO_GLOBAL = 5
