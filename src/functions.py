import widgets
import support
import tkinter as tk
from tkinter import ttk

# funciones de operaciones
def calcular_diferencia():
    try:
        valor_inicial = float(widgets.entry_valor_inicial.get())
        valor_final = float(widgets.entry_valor_final.get())

        aumento = valor_final - valor_inicial
        porcentaje_aumento = (aumento / valor_inicial) * 100 if valor_inicial != 0 else "Infinito"

        widgets.label_resultado.config(text=f"Difference: {porcentaje_aumento:.2f}%.")
    except ValueError:
        widgets.label_resultado.config(text="Error: Invalid Entry.")

def calcular_conversion():
    try:
        valor_usdt = float(widgets.entry_value_usdt.get())
        fee = float(widgets.entry_fee.get())
        precio_cripto = float(widgets.entry_precio.get())

        conversion = (valor_usdt / precio_cripto) - fee

        widgets.label_resultado_conversion.config(text=f"Amount to operate: {conversion:.6f}.")
    except ValueError:
        widgets.label_resultado_conversion.config(text="Error: Invalid Entry.")

def restar_porcentaje():
    try:
        valor_origen = float(widgets.entry_origen.get())
        porcentaje = float(widgets.entry_porcentaje.get())

        nuevo_valor = (porcentaje * valor_origen) / 100
        valor_origen -= nuevo_valor

        widgets.label_resultado_operar_porcentaje.config(text=f"New Value: {valor_origen:.6f}.")
    except ValueError:
        widgets.label_resultado_operar_porcentaje.config(text="Error: Invalid Entry.")

def sumar_porcentaje():
    try:
        valor_origen = float(widgets.entry_origen.get())
        porcentaje = float(widgets.entry_porcentaje.get())

        nuevo_valor = (porcentaje * valor_origen) / 100
        valor_origen += nuevo_valor

        widgets.label_resultado_operar_porcentaje.config(text=f"New Value: {valor_origen:.6f}.")
    except ValueError:
        widgets.label_resultado_operar_porcentaje.config(text="Error: Invalid Entry.")

def calcular_valor_porcentaje():
        try:
            valor_origen = float(widgets.entry_valor_original.get())
            valor_calcular = float(widgets.entry_calcular_porcentaje.get())
            nuevo_valor = (valor_calcular * 100) / valor_origen

            widgets.label_resultado_porcentaje.config(text=f"Percentage: {nuevo_valor:.6f}%")
        except ValueError:
            widgets.label_resultado_porcentaje.config(text="Error: Invalid Entry.")

def calcular_roi():
    try:
        inversion = float(widgets.entry_inversion.get())
        profit = float(widgets.entry_profit.get())

        roi = (profit * 100) / inversion

        widgets.label_resultado_roi.config(text=f"ROI: {roi:.6f}.")
    except ValueError:
        widgets.label_resultado_roi.config(text="Error: Invalid Entry.")

def calcular_roi_total(): # similar a calcular roi pero teniendo en cuenta de total a total 
    try:
        inversion = float(widgets.entry_inversion_total.get())
        total = float(widgets.entry_profit_total.get())
        profit = total - inversion
        roi = (profit * 100) / inversion

        widgets.label_resultado_roi_total.config(text=f"ROI: {roi:.6f}.")
    except ValueError:
        widgets.label_resultado_roi_total.config(text="Error: Invalid Entry.")

def calcular_porcentaje():
    try:
        origen = float(widgets.entry_original.get())
        porcentaje = float(widgets.entry_porcentaje2.get())

        resultado = (porcentaje * origen) / 100

        widgets.label_resultado_calcular_porcentaje.config(text=f"New Value: {resultado:.6f}.")
    except ValueError:
        widgets.label_resultado_calcular_porcentaje.config(text="Error: Invalid Entry.")

def calcular_leverage():
    try:
        precio = float(widgets.entry_precio_l.get())
        leverage = float(widgets.entry_leverage.get())
        inversion = float(widgets.entry_inversion_l.get())
        aumento = float(widgets.entry_aumento.get())

        porcentaje = 100 / leverage # me dice cuanto es el porcentaje de liquidacion
        aumento_precio = (porcentaje * precio) / 100
        precio_liquidacion = precio - aumento_precio

        profit = ((inversion * aumento) / 100) * leverage

        widgets.label_resultado_leverage.config(text=(f"Liquidation Price: {precio_liquidacion:.6f}.\nProfit: {profit:.6f}"))
                                                           
    except ValueError:
        widgets.label_resultado_leverage.config(text="Error: Invalid Entry.")

def calcular_venta_limit():
    try:
        usdt_inicial = float(widgets.entry_usdt_inicial.get())
        usdt_objetivo = float(widgets.entry_usdt_objetivo.get())
        precio_inicial = float(widgets.entry_precio_inicial.get())

        venta = usdt_objetivo - usdt_inicial
        porcentaje_aumento = (venta * 100) / usdt_inicial
        aumento_precio = (porcentaje_aumento * precio_inicial) / 100
        precio_venta = precio_inicial + aumento_precio 

        widgets.label_resultado_venta_limit.config(text=(f"Sell Price: {precio_venta:.6f}.\n"
                                                         f"Percentage Increase: {porcentaje_aumento:.6f}\n"
                                                         f"Sell: {venta:.6f}"))
    except ValueError:
        widgets.label_resultado_venta_limit.config(text="Error: Invalid Entry.")

def calcular_average():
    inversiones = []
    precios = []

    for widget_group in average_widgets:
        # Suponiendo que la estructura es (label_investment, entry_investment, label_price, entry_price)
        entry_investment = widget_group[1]
        entry_price = widget_group[3]

        # Obtener los valores de las Entry y convertirlos a float
        try:
            valor_inversion = float(entry_investment.get())
            valor_precio = float(entry_price.get())
        except ValueError:
            # Manejar el caso en que la entrada no sea un número
            widgets.label_resultado_average.config(text="Error: Invalid Entry.")
            continue

        inversiones.append(valor_inversion)
        precios.append(valor_precio)

    # obtener total de unidades y de inversion
    total_unidades = 0
    total_inversion = 0
    for i in range(len(inversiones)):
        total_unidades += inversiones[i]/precios[i]
        total_inversion += inversiones[i]
    # obtener average
    average = total_inversion / total_unidades
    # Aquí ya has calculado total_unidades y total_inversion
    precio_actual = float(widgets.entry_precio_actual.get())  # Obtener el precio actual de la Entry
    profit, valor_actual = calcular_rendimiento(total_unidades, total_inversion, precio_actual)

    # Ahora puedes mostrar estos datos en tu interfaz
    widgets.label_resultado_average.config(text=(f"Total Investment: {total_inversion:.6f}.\n"
                                             f"Total Units: {total_unidades:.6f}\n"
                                             f"Average Buy: {average:.6f}\n"
                                             f"Current Price: {precio_actual:.6f}\n"
                                             f"Current Value: {valor_actual:.6f}\n"
                                             f"Profit/Loss: {profit:.6f}"))

def calcular_ratio():
    try:
        liquidez = float(widgets.entry_liquidez.get())
        exposicion = float(widgets.entry_exposicion.get())
        if exposicion > liquidez:
            porcentaje_exposicion = 100 - ((liquidez * 100) / exposicion)
            porcentaje_liquidez = 100 - porcentaje_exposicion
        elif exposicion < liquidez:
            porcentaje_liquidez = 100 - ((exposicion * 100) / liquidez)
            porcentaje_exposicion = 100 - porcentaje_liquidez
        else: 
            porcentaje_exposicion = 50
            porcentaje_liquidez = 50
        
        ratio = exposicion / liquidez

        widgets.label_ratio_resultado.config(text=(f"Exposure: {porcentaje_exposicion:.6f}%\n"
                                                    f"Liquidity: {porcentaje_liquidez:.6f}%\n"
                                                    f"Liquidity/Exposure Ratio: 1:{ratio:.6f}"))
    except ValueError:
        widgets.label_ratio_resultado.config(text="Error: Invalid Entry.")        

# permite calcular el rendimiento de una posicion
def calcular_rendimiento(total_unidades, total_inversion, precio_actual):
    valor_actual = total_unidades * precio_actual  # Valor de tus unidades al precio actual -> es decir, cuanto vale la posicion actualmente
    profit = valor_actual - total_inversion  # Diferencia entre el valor actual de la posicion y la inversión total
    
    return profit, valor_actual

def calcular_x():
    try:
        origin = float(widgets.entry_from_value.get())
        dest = float(widgets.entry_to_value.get())

        resultado = dest / origin

        widgets.label_fromto_result.config(text=f"Total X: {resultado:.2f}.")
    except ValueError:
        widgets.label_fromto_result.config(text="Error: Invalid Entry.")

#ej si quisiese que tenga margen: widgets.label_resultado_operar_porcentaje.pack(pady=(0, 10))   
# funciones de setteo de widgets
def start_operation(): # para average
    support.actualizar_canvas()
    try: 
        # ocultar los actuales
        if len(average_widgets) > 0:
            for widget_group in average_widgets:
                for widget in widget_group:
                    widget.destroy()
        # Vaciar la lista para poder agregar los widgets regenerados
        average_widgets.clear()
        average_boton.pack_forget()
        widgets.label_resultado_average.pack_forget()
        widgets.label_error_start_operations.pack() 
        try:
            num_operations = int(widgets.entry_total_operations.get()) # Obtener el número de operaciones
            # Manejar el caso en que la entrada no sea un número 
        except ValueError:
            widgets.label_error_start_operations.config(text="Error: Invalid Entry.")

        if num_operations > 0: 
            widgets.label_error_start_operations.config(text="Enter negative value for sell operation\nEnter positive value for buy operation") 
            # volver a generar widgets en base a numero de operaciones
            for i in range(1, num_operations + 1):
                # Crear y empaquetar los widgets para cada operación
                label_investment = tk.Label(support.frame_dentro_canvas, text=f"Buy/Sell {i}")
                label_investment.pack()
                entry_investment = tk.Entry(support.frame_dentro_canvas)  # Entry para investment
                entry_investment.pack()

                label_price = tk.Label(support.frame_dentro_canvas, text=f"Price {i}")
                label_price.pack()
                entry_price = tk.Entry(support.frame_dentro_canvas)  # Entry para price
                entry_price.pack()
                # Añadir los widgets a la lista
                average_widgets.append((label_investment, entry_investment, label_price, entry_price))
            average_boton.pack()
            widgets.label_resultado_average.pack()
        else:
            widgets.label_error_start_operations.config(text="Error: Invalid Entry.") 
    except ValueError:
        print("invalid.")
    support.actualizar_canvas() # permitir que se muestre scrollbar si los widgets exceden canvas

def set_calcular_x():
    support.actualizar_canvas()
    widgets.label_from_value.pack()
    widgets.entry_from_value.pack()
    widgets.label_to_value.pack()
    widgets.entry_to_value.pack()
    fromto_button.pack()
    widgets.label_fromto_result.pack()

def set_average_price():
    support.actualizar_canvas()
    widgets.label_total_operations.pack()
    widgets.entry_total_operations.pack()
    widgets.label_precio_actual.pack()
    widgets.entry_precio_actual.pack()
    start_button.pack()
    widgets.label_error_start_operations.pack()
    widgets.label_error_start_operations.config(text="") 

def set_calcular_venta_limit():
    support.actualizar_canvas()
    widgets.label_usdt_inicial.pack()
    widgets.entry_usdt_inicial.pack()
    widgets.label_usdt_objetivo.pack()
    widgets.entry_usdt_objetivo.pack()
    widgets.label_precio_inicial.pack()
    widgets.entry_precio_inicial.pack()
    boton_calcular_venta_limit.pack()
    widgets.label_resultado_venta_limit.pack()

def set_calcular_porcentaje():
    support.actualizar_canvas()
    widgets.label_original.pack()
    widgets.entry_original.pack()
    widgets.label_porcentaje2.pack()
    widgets.entry_porcentaje2.pack()
    boton_calcular_porcentaje2.pack()
    widgets.label_resultado_calcular_porcentaje.pack()    

def set_calcular_valor_porcentaje():
    support.actualizar_canvas()
    widgets.label_valor_original.pack()
    widgets.entry_valor_original.pack()
    widgets.label_calcular_porcentaje.pack()
    widgets.entry_calcular_porcentaje.pack()
    boton_calcular_porcentaje.pack()
    widgets.label_resultado_porcentaje.pack()

def set_calculadora_diferencia():
    support.actualizar_canvas()
    widgets.label_valor_inicial.pack() 
    widgets.entry_valor_inicial.pack()
    widgets.label_valor_final.pack()
    widgets.entry_valor_final.pack()
    boton_calcular_diferencia.pack()
    widgets.label_resultado.pack()

def set_calculadora_conversion():
    support.actualizar_canvas()
    widgets.label_usdt.pack()
    widgets.entry_value_usdt.pack()
    widgets.label_fee.pack()
    widgets.entry_fee.pack()
    widgets.label_precio.pack()
    widgets.entry_precio.pack()
    boton_calcular_conversion.pack()
    widgets.label_resultado_conversion.pack()

def set_operar_porcentaje():
    support.actualizar_canvas()
    widgets.label_origen.pack()
    widgets.entry_origen.pack()
    widgets.label_porcentaje.pack()
    widgets.entry_porcentaje.pack()
    boton_restar_porcentaje.pack()
    boton_sumar_porcentaje.pack()
    widgets.label_resultado_operar_porcentaje.pack()

def set_calculadora_roi():
    support.actualizar_canvas()
    widgets.label_inversion.pack()
    widgets.entry_inversion.pack()
    widgets.label_profit.pack()
    widgets.entry_profit.pack()
    boton_calcular_roi.pack()
    widgets.label_resultado_roi.pack()

def set_calculadora_roi_total():
    support.actualizar_canvas()
    widgets.label_inversion_total.pack()
    widgets.entry_inversion_total.pack()
    widgets.label_profit_total.pack()
    widgets.entry_profit_total.pack()
    boton_calcular_roi_total.pack()
    widgets.label_resultado_roi_total.pack()

def set_calcular_leverage():
    support.actualizar_canvas()
    widgets.label_precio_l.pack()
    widgets.entry_precio_l.pack()
    widgets.label_leverage.pack()
    widgets.entry_leverage.pack()
    widgets.label_inversion_l.pack()
    widgets.entry_inversion_l.pack()
    widgets.label_aumento.pack()
    widgets.entry_aumento.pack()
    boton_calcular_leverage.pack()
    widgets.label_resultado_leverage.pack()

def set_calcular_ratio():
    support.actualizar_canvas()
    widgets.label_liquidez.pack()
    widgets.entry_liquidez.pack()
    widgets.label_exposicion.pack()
    widgets.entry_exposicion.pack()
    boton_ratio.pack()
    widgets.label_ratio_resultado.pack()

#crear boton
boton_calcular_diferencia = tk.Button(support.frame_dentro_canvas, text="Calculate Difference", command=calcular_diferencia)
boton_calcular_conversion = tk.Button(support.frame_dentro_canvas, text="Calculate Value", command=calcular_conversion)
boton_restar_porcentaje = tk.Button(support.frame_dentro_canvas, text="Substract Percentage", command=restar_porcentaje)
boton_sumar_porcentaje = tk.Button(support.frame_dentro_canvas, text="Add Percentage", command=sumar_porcentaje)
boton_calcular_porcentaje = tk.Button(support.frame_dentro_canvas, text="Calculate Value", command=calcular_valor_porcentaje)
boton_calcular_roi = tk.Button(support.frame_dentro_canvas, text="Calculate ROI", command=calcular_roi)
boton_calcular_roi_total = tk.Button(support.frame_dentro_canvas, text="Calculate ROI", command=calcular_roi_total)
boton_calcular_porcentaje2 = tk.Button(support.frame_dentro_canvas, text="Calculate Percentage", command=calcular_porcentaje)
boton_calcular_leverage = tk.Button(support.frame_dentro_canvas, text="Calculate Liquidation/Profit", command=calcular_leverage)
boton_calcular_venta_limit = tk.Button(support.frame_dentro_canvas, text="Calculate Sell Price", command=calcular_venta_limit)
start_button = tk.Button(support.frame_dentro_canvas, text="Start Calculation", command=start_operation)
average_boton = tk.Button(support.frame_dentro_canvas, text="Calculate Average Price", command=calcular_average)
fromto_button = tk.Button(support.frame_dentro_canvas, text="Calculate X", command=calcular_x) 
boton_ratio = tk.Button(support.frame_dentro_canvas, text="Calculate Ratio", command=calcular_ratio)

average_widgets = [] # lista donde se guardan los widgets de la funcion "average" solamente

botones = [boton_calcular_diferencia, boton_calcular_conversion, 
boton_restar_porcentaje, boton_sumar_porcentaje, boton_calcular_porcentaje, boton_calcular_roi,
boton_calcular_porcentaje2, boton_calcular_leverage, boton_calcular_venta_limit, boton_calcular_roi_total,
start_button, average_boton, fromto_button, boton_ratio]