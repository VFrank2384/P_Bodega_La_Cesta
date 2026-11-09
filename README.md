# 🛒 Bodega La Cesta - Sistema de Control de Stock

Sistema de escritorio desarrollado en Python para automatizar el control de inventario de la Bodega "La Cesta", detectando productos con stock crítico.

## 🚀 Tecnologías utilizadas
* Python 3
* Tkinter (Interfaz Gráfica)
* MySQL (Base de Datos)
* MySQL Connector

## 📂 Estructura del Proyecto
* `config/`: Archivo de configuración de la base de datos.
* `database/`: Script SQL y lógica de conexión (CRUD).
* `ui/`: Interfaz gráfica de usuario (Tkinter).
* `main.py`: Archivo principal de ejecución.

## ⚙️ Cómo ejecutar el proyecto
1. Clona el repositorio.
2. Crea la base de datos ejecutando el archivo `database/script_bd.sql` en MySQL Workbench.
3. Configura tus credenciales en `config/db_config.py`.
4. Instala las dependencias: `pip install mysql-connector-python`
5. Ejecuta el programa: `python main.py`

---
Desarrollado por [Tu Nombre] - Universidad Tecnológica del Perú
