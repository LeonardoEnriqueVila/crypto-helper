import tkinter as tk

def crear_calculadora(ventana):
    frame_calculadora = tk.Frame(ventana)
    # Definir una función para calcular la expresión introducida en el campo de entrada
    def calcular(event=None):  # Añadido event=None para manejar el evento de teclado
        try:
            resultado = eval(entrada.get())
            entrada.delete(0, tk.END)
            entrada.insert(0, str(resultado))
        except Exception as e:
            entrada.delete(0, tk.END)
            entrada.insert(0, "Error")

    # Crear el campo de entrada y empaquetarlo primero
    entrada = tk.Entry(frame_calculadora, width=20)
    entrada.pack()  # El campo de entrada se empaqueta primero, por lo que aparecerá en la parte superior


    # Definir los botones que se incluirán en la calculadora
    botones = [
        ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
        ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('/', 4, 3)  # (Texto del botón, fila, columna)
    ]

    # Crear un Frame para cada fila de botones
    for fila in range(5):  # 5 filas en total
        frame_fila = tk.Frame(frame_calculadora)
        frame_fila.pack()  # Empaquetar cada fila

        # Colocar botones en la fila actual
        for boton in botones[fila * 4:(fila + 1) * 4]:  # Ajustar el rango para cada fila
            texto = boton[0]
            if texto == "=":
                btn = tk.Button(frame_fila, text=texto, command=calcular)
            elif texto == "C":
                btn = tk.Button(frame_fila, text=texto, command=lambda: entrada.delete(0, tk.END))
            else:
                btn = tk.Button(frame_fila, text=texto, command=lambda txt=texto: entrada.insert(tk.END, txt))
            btn.pack(side=tk.LEFT)  # Empaquetar botones en la misma fila
            
    # Asegurar que el campo de entrada tenga el foco
    entrada.focus_set()

    # Asignar eventos de teclado a acciones
    def asignar_teclas():
        entrada.bind("<Return>", calcular)
        entrada.bind("<Escape>", lambda _: entrada.delete(0, tk.END))
    # Asignar las teclas a las acciones
    asignar_teclas()
    return frame_calculadora
