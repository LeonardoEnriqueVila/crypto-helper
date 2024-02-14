import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.iconbitmap('C:\\Users\\leona\\Desktop\\Python\\cripto_app\\btc-icon.ico')
ventana.title("Crypto Helper v0.2")
ventana.geometry("280x400")

# Crear un Canvas y una Scrollbar
canvas = tk.Canvas(ventana)
scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)

# Configurar el canvas
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Crear un Frame dentro del Canvas
frame_dentro_canvas = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame_dentro_canvas, anchor="nw")

frame_dentro_canvas.config(highlightthickness=0)  # Quitar el borde destacado
canvas.config(borderwidth=0, highlightthickness=0)  # Quitar el borde del canvas

# Función que se llama cuando es necesario reajustar el canvas, 
# permite que aparezca o desaparezca el scrollbar de manera automatica
def actualizar_canvas():
    frame_dentro_canvas.update_idletasks()  # Actualizar el frame
    canvas.config(scrollregion=canvas.bbox("all"))  # Ajustar la scrollregion

