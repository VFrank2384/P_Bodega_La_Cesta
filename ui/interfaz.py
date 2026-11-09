import tkinter as tk
from tkinter import messagebox
from database.conexion import obtener_inventario_db, actualizar_stock_db, agregar_producto_db
from config.db_config import STOCK_MINIMO_GLOBAL

class AppBodega:
    def __init__(self, root):
        self.root = root

        self.root.title("Bodega La Cesta - Sistema de Control de Stock")
        self.root.geometry("650x550")
        self.root.config(padx=20, pady=20)

        tk.Label(root, text="🛒 Inventario de Bodega La Cesta", font=("Arial", 16, "bold")).pack(pady=10)

        self.lista_productos = tk.Listbox(root, height=15, width=70, font=("Courier", 10))
        self.lista_productos.pack(pady=10)

        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Actualizar", bg="#2196F3", fg="white", command=self.cargar_datos).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Vender (-1)", bg="#f44336", fg="white", command=self.accion_vender).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Reabastecer", bg="#4CAF50", fg="white", command=self.accion_reabastecer).grid(row=0, column=2, padx=5)
        tk.Button(frame_botones, text="+ Nuevo Producto", bg="#9C27B0", fg="white", command=self.accion_agregar).grid(row=0, column=3, padx=5)

        self.cargar_datos()

    def cargar_datos(self):
        self.lista_productos.delete(0, tk.END)
        productos = obtener_inventario_db()
        
        self.lista_productos.insert(tk.END, f"{'ID':<5} | {'PRODUCTO':<25} | {'STOCK':<8} | {'ESTADO'}")
        self.lista_productos.insert(tk.END, "-" * 70)
        
        for prod in productos:
            id_p, nombre, stock, min_stock = prod
            estado = "⚠️ CRÍTICO" if stock <= min_stock else "✅ OK"
            # Ajustamos el ancho para nombres más largos
            self.lista_productos.insert(tk.END, f"{id_p:<5} | {nombre:<25} | {stock:<8} | {estado}")

    def obtener_producto_seleccionado(self):
        seleccion = self.lista_productos.curselection()
        if not seleccion or seleccion[0] < 2:
            messagebox.showwarning("Atención", "Selecciona un producto válido de la lista.")
            return None
        index = seleccion[0] - 2
        productos = obtener_inventario_db()
        return productos[index]

    def accion_vender(self):
        prod = self.obtener_producto_seleccionado()
        if prod:
            id_p, nombre, stock, _ = prod
            if stock <= 0:
                messagebox.showwarning("Sin Stock", f"No hay unidades de {nombre}.")
                return
            
            if actualizar_stock_db(id_p, stock - 1):
                messagebox.showinfo("Venta", f"Se vendió 1 unidad de {nombre}.")
                self.cargar_datos()

    def accion_reabastecer(self):
        prod = self.obtener_producto_seleccionado()
        if prod:
            id_p, nombre, stock, _ = prod
            self.crear_ventana_emergente("Reabastecer", f"¿Cuántas unidades de {nombre} llegaron?", lambda c: self.ejecutar_reabastecer(id_p, stock, c))

    def ejecutar_reabastecer(self, id_p, stock_actual, cantidad):
        if actualizar_stock_db(id_p, stock_actual + cantidad):
            messagebox.showinfo("Éxito", f"Se agregaron {cantidad} unidades.")
            self.cargar_datos()

    def accion_agregar(self):
        self.crear_ventana_emergente("Nuevo Producto", "Ingrese: nombre,stock,stock_minimo\n(Ej: Jabón,10,3)", self.ejecutar_agregar, es_compuesta=True)

    def ejecutar_agregar(self, datos_string):
        try:
            nombre, stock, min_stock = datos_string.split(",")
            if agregar_producto_db(nombre.strip().title(), int(stock), int(min_stock)):
                messagebox.showinfo("Éxito", "Producto agregado correctamente.")
                self.cargar_datos()
            else:
                messagebox.showerror("Error", "No se pudo agregar. ¿El producto ya existe?")
        except ValueError:
             messagebox.showerror("Error", "Formato incorrecto. Use: Nombre,Cantidad,Minimo")

    def crear_ventana_emergente(self, titulo, mensaje, callback, es_compuesta=False):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.geometry("350x180")
        
        tk.Label(ventana, text=mensaje).pack(pady=10)
        entry = tk.Entry(ventana)
        entry.pack(pady=5)

        def confirmar():
            try:
                valor = entry.get() if es_compuesta else int(entry.get())
                callback(valor)
                ventana.destroy()
            except ValueError:
                messagebox.showerror("Error", "Ingrese un valor válido.")

        tk.Button(ventana, text="Confirmar", command=confirmar).pack(pady=10)