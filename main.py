import tkinter as tk
from ui.interfaz import AppBodega

if __name__ == "__main__":
    print("Iniciando el sistema de Bodega La Cesta...")
    root = tk.Tk()
    app = AppBodega(root)
    root.mainloop()