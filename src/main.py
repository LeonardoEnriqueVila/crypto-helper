import tkinter as tk
from tkinter import ttk
import widgets
import functions
import support
import calculator

# Crear y posicionar la calculadora ANTES que el canvas, asi no se ve afectada por el scroll cuando se activa
frame_calculadora = calculator.crear_calculadora(support.ventana)
# Posicionar la calculadora en una parte fija de la ventana
frame_calculadora.pack(side=tk.TOP, anchor="nw", pady=10)  # nw (norwest)

# Empaquetar el canvas y la scrollbar
support.scrollbar.pack(side="right", fill="y")
support.canvas.pack(side="left", fill="both", expand=True)

# evento de seleccion del combobox        
def seleccion(event):
    opcion_seleccionada = combobox.get()
    match opcion_seleccionada:
        case "Percentage Difference":
            for widget in widgets.widgets:
                widget.pack_forget() # ocultar todos los widgets
            if len(functions.average_widgets) > 0:
                for widget_group in functions.average_widgets:
                    for widget in widget_group:
                        widget.pack_forget()
            for boton in functions.botones:
                boton.pack_forget()
            functions.set_calculadora_diferencia() # mostrar los widgets que corresponen a la opcion
        case "Crypto to USDT":
            for widget in widgets.widgets:
                widget.pack_forget()
            if len(functions.average_widgets) > 0:
                for widget_group in functions.average_widgets:
                    for widget in widget_group:
                        widget.pack_forget()
            for boton in functions.botones:
                boton.pack_forget()
            functions.set_calculadora_conversion()
        case "Add/Substract Percentage":
            for widget in widgets.widgets:
                widget.pack_forget()
            if len(functions.average_widgets) > 0:
                for widget_group in functions.average_widgets:
                    for widget in widget_group:
                        widget.pack_forget()
            for boton in functions.botones:
                boton.pack_forget()
            functions.set_operar_porcentaje()
        case "Value to Percentage":
            for widget in widgets.widgets:
                widget.pack_forget()
            if len(functions.average_widgets) > 0:
                for widget_group in functions.average_widgets:
                    for widget in widget_group:
                        widget.pack_forget()
            for boton in functions.botones:
                boton.pack_forget()
            functions.set_calcular_valor_porcentaje()
        case "Calculate ROI (Profit)":
            for widget in widgets.widgets:
                widget.pack_forget()
            if len(functions.average_widgets) > 0:
                for widget_group in functions.average_widgets:
                    for widget in widget_group:
                        widget.pack_forget()
            for function in functions.botones:
                function.pack_forget()
            functions.set_calculadora_roi()
        case "Calculate ROI (Total)":
            for widget in widgets.widgets:
                widget.pack_forget()
            if len(functions.average_widgets) > 0:
                for widget_group in functions.average_widgets:
                    for widget in widget_group:
                        widget.pack_forget()
            for function in functions.botones:
                function.pack_forget()
            functions.set_calculadora_roi_total()
        case "Calculate Percentage":
            for widget in widgets.widgets:
                widget.pack_forget()
            if len(functions.average_widgets) > 0:
                for widget_group in functions.average_widgets:
                    for widget in widget_group:
                        widget.pack_forget()
            for function in functions.botones:
                function.pack_forget()
            functions.set_calcular_porcentaje()
        case "Leverage Calculator":
            for widget in widgets.widgets:
                widget.pack_forget()
            if len(functions.average_widgets) > 0:
                for widget_group in functions.average_widgets:
                    for widget in widget_group:
                        widget.pack_forget()
            for function in functions.botones:
                function.pack_forget()
            functions.set_calcular_leverage()
        case "Calculate Sell Price":
            for widget in widgets.widgets:
                widget.pack_forget()
            if len(functions.average_widgets) > 0:
                for widget_group in functions.average_widgets:
                    for widget in widget_group:
                        widget.pack_forget()
            for function in functions.botones:
                function.pack_forget()
            functions.set_calcular_venta_limit()
        case "Average Price Operator":
            for widget in widgets.widgets:
                widget.pack_forget()
            if len(functions.average_widgets) > 0:
                for widget_group in functions.average_widgets:
                    for widget in widget_group:
                        widget.pack_forget()
            for function in functions.botones:
                function.pack_forget()
            functions.set_average_price()
        case "X Calculator":
            for widget in widgets.widgets:
                widget.pack_forget()
            if len(functions.average_widgets) > 0:
                for widget_group in functions.average_widgets:
                    for widget in widget_group:
                        widget.pack_forget()
            for function in functions.botones:
                function.pack_forget()
            functions.set_calcular_x()

# opciones para combobox
opciones = ["Percentage Difference", "Crypto to USDT", "Add/Substract Percentage",
             "Value to Percentage" , "Calculate ROI (Profit)", "Calculate ROI (Total)", "Calculate Percentage", "Leverage Calculator",
             "Calculate Sell Price", "Average Price Operator", "X Calculator"]
# Crear un combobox
combobox = ttk.Combobox(support.frame_dentro_canvas, values=opciones, state='readonly')
combobox.pack(pady=(0, 0))  # Posiciona el combobox
combobox.set("Select an option")
combobox.bind("<<ComboboxSelected>>", seleccion)

# Iniciar el bucle de la GUI
support.ventana.mainloop()

