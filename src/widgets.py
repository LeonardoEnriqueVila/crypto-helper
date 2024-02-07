import tkinter as tk
#from tkinter import ttk
import support

# crear labels
label_valor_inicial = tk.Label(support.frame_dentro_canvas, text="Initial Value:")
label_valor_final = tk.Label(support.frame_dentro_canvas, text="Final Value:")
label_resultado = tk.Label(support.frame_dentro_canvas, text="Result:")

label_usdt = tk.Label(support.frame_dentro_canvas, text="Value in USDT:")
label_fee = tk.Label(support.frame_dentro_canvas, text="Fee:")
label_precio = tk.Label(support.frame_dentro_canvas, text="Cripto Price:")
label_resultado_conversion = tk.Label(support.frame_dentro_canvas, text="Convertion:")

label_origen = tk.Label(support.frame_dentro_canvas, text="Origin Value:")
label_porcentaje = tk.Label(support.frame_dentro_canvas, text="Percentage:")
label_resultado_operar_porcentaje = tk.Label(support.frame_dentro_canvas, text="New Value:")

label_valor_original = tk.Label(support.frame_dentro_canvas, text="Origin Value:")
label_calcular_porcentaje = tk.Label(support.frame_dentro_canvas, text="Value for Percentage:")
label_resultado_porcentaje = tk.Label(support.frame_dentro_canvas, text="Value to Percentage:")

label_inversion = tk.Label(support.frame_dentro_canvas, text="Investment:")
label_profit = tk.Label(support.frame_dentro_canvas, text="Profit:")
label_resultado_roi = tk.Label(support.frame_dentro_canvas, text="ROI:")

label_inversion_total = tk.Label(support.frame_dentro_canvas, text="Initial Investment:")
label_profit_total = tk.Label(support.frame_dentro_canvas, text="Actual Amount:")
label_resultado_roi_total = tk.Label(support.frame_dentro_canvas, text="ROI:")

label_original = tk.Label(support.frame_dentro_canvas, text="Origin Value:")
label_porcentaje2 = tk.Label(support.frame_dentro_canvas, text="Percentage:")
label_resultado_calcular_porcentaje = tk.Label(support.frame_dentro_canvas, text="New Value:")

label_precio_l = tk.Label(support.frame_dentro_canvas, text="Origin Price:")
label_leverage = tk.Label(support.frame_dentro_canvas, text="Leverage:")
label_inversion_l = tk.Label(support.frame_dentro_canvas, text="Investment:")
label_aumento = tk.Label(support.frame_dentro_canvas, text="Percentage Desired:")
label_resultado_leverage = tk.Label(support.frame_dentro_canvas, text="Liquidation Price:\nProfit:")

label_usdt_inicial = tk.Label(support.frame_dentro_canvas, text="Initial USDT Amount:")
label_usdt_objetivo = tk.Label(support.frame_dentro_canvas, text="Desired USDT Amount:")
label_precio_inicial = tk.Label(support.frame_dentro_canvas, text="Price:")
label_resultado_venta_limit = tk.Label(support.frame_dentro_canvas, text="Sell Price:\nPercentage Increase:\nSell:")

label_total_operations = tk.Label(support.frame_dentro_canvas, text="Total Operations:")
label_precio_actual = tk.Label(support.frame_dentro_canvas, text="Actual Price:")
label_resultado_average = tk.Label(support.frame_dentro_canvas, text="Total Investment:\nTotal Units:\nAverage Buy:\nCurrent Price:\nCurrent Value:\nProfit/Loss:")                                           
label_error_start_operations = tk.Label(support.frame_dentro_canvas, text="")

label_from_value = tk.Label(support.frame_dentro_canvas, text="From Value:")
label_to_value = tk.Label(support.frame_dentro_canvas, text="To Value:")
label_fromto_result = tk.Label(support.frame_dentro_canvas, text="Total X:")

# crear entrys
entry_valor_final = tk.Entry(support.frame_dentro_canvas)
entry_valor_inicial = tk.Entry(support.frame_dentro_canvas)

entry_value_usdt = tk.Entry(support.frame_dentro_canvas)
entry_fee = tk.Entry(support.frame_dentro_canvas)
entry_precio = tk.Entry(support.frame_dentro_canvas)

entry_origen = tk.Entry(support.frame_dentro_canvas)
entry_porcentaje = tk.Entry(support.frame_dentro_canvas)

entry_valor_original = tk.Entry(support.frame_dentro_canvas)
entry_calcular_porcentaje = tk.Entry(support.frame_dentro_canvas)

entry_inversion = tk.Entry(support.frame_dentro_canvas)
entry_profit = tk.Entry(support.frame_dentro_canvas)

entry_inversion_total = tk.Entry(support.frame_dentro_canvas)
entry_profit_total = tk.Entry(support.frame_dentro_canvas)

entry_original = tk.Entry(support.frame_dentro_canvas)
entry_porcentaje2 = tk.Entry(support.frame_dentro_canvas)

entry_precio_l = tk.Entry(support.frame_dentro_canvas)
entry_leverage = tk.Entry(support.frame_dentro_canvas)
entry_inversion_l = tk.Entry(support.frame_dentro_canvas)
entry_aumento = tk.Entry(support.frame_dentro_canvas)

entry_usdt_inicial = tk.Entry(support.frame_dentro_canvas)
entry_usdt_objetivo = tk.Entry(support.frame_dentro_canvas)
entry_precio_inicial = tk.Entry(support.frame_dentro_canvas)

entry_total_operations = tk.Entry(support.frame_dentro_canvas)
entry_precio_actual = tk.Entry(support.frame_dentro_canvas)

entry_from_value = tk.Entry(support.frame_dentro_canvas)
entry_to_value = tk.Entry(support.frame_dentro_canvas)

widgets = [
    label_valor_inicial, entry_valor_inicial, label_valor_final, entry_valor_final, 
    label_resultado, label_usdt, entry_value_usdt, label_fee, entry_fee, 
    label_precio, entry_precio, label_resultado_conversion, 
    label_origen, entry_origen, label_porcentaje, entry_porcentaje, 
    label_resultado_operar_porcentaje, 
    label_valor_original, entry_valor_original, label_calcular_porcentaje, 
    entry_calcular_porcentaje, label_resultado_porcentaje, 
    label_inversion, label_profit, label_resultado_roi, entry_inversion, entry_profit,
    label_original, label_porcentaje2, label_resultado_calcular_porcentaje,
    entry_original, entry_porcentaje2, label_precio_l, label_leverage, label_inversion_l,
    label_aumento, label_resultado_leverage, entry_precio_l, entry_leverage, entry_inversion_l,
    entry_aumento, label_usdt_inicial, entry_usdt_inicial,
    label_usdt_objetivo, entry_usdt_objetivo,
    label_precio_inicial, entry_precio_inicial,
    label_resultado_venta_limit, entry_inversion_total, entry_profit_total,
    label_inversion_total, label_profit_total, label_resultado_roi_total,
    entry_total_operations, entry_precio_actual, label_precio_actual, label_total_operations, label_resultado_average, label_error_start_operations,
    label_from_value, label_to_value, label_fromto_result, entry_from_value, entry_to_value
]
