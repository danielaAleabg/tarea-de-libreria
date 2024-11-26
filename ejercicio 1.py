import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

def resistencia_serie(resistencias):
    return sum(resistencias)

def resistencia_paralelo(resistencias):
    inverso_total = sum(1 / r for r in resistencias)
    return 1 / inverso_total if inverso_total != 0 else float('inf')

def calcular():
    try:
        tipo_conexion = conexion.get()
        
        num_resistencias = int(entry_num_resistencias.get())
        resistencias = []
        
        for i in range(num_resistencias):
            valor_resistencia = float(entries_resistencias[i].get())
            resistencias.append(valor_resistencia)
        
        if tipo_conexion == "Serie":
            resultado = resistencia_serie(resistencias)
        elif tipo_conexion == "Paralelo":
            resultado = resistencia_paralelo(resistencias)
        else:
            raise ValueError("Tipo de conexión no válido")
        
        label_resultado.config(text=f"Resistencia Total: {resultado:.2f} Ω")
        
        graficar(resistencias, tipo_conexion)
        
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")

def graficar(resistencias, tipo_conexion):
    num_resistencias = len(resistencias)
    resistencias_totales = []
    
    for i in range(1, num_resistencias + 1):
        resistencias_parcial = resistencias[:i]
        
        if tipo_conexion == "Serie":
            resistencias_totales.append(resistencia_serie(resistencias_parcial))
        elif tipo_conexion == "Paralelo":
            resistencias_totales.append(resistencia_paralelo(resistencias_parcial))
    
    plt.plot(range(1, num_resistencias + 1), resistencias_totales, marker='o')
    plt.title(f"Resistencia Total vs Número de Resistencias ({tipo_conexion})")
    plt.xlabel("Número de Resistencias")
    plt.ylabel("Resistencia Total (Ω)")
    plt.grid(True)
    plt.show()

def crear_interfaz():
    window = tk.Tk()
    window.title("Cálculo de Resistencia Equivalente")
    
    label_tipo_conexion = tk.Label(window, text="Selecciona el tipo de conexión:")
    label_tipo_conexion.grid(row=0, column=0, padx=10, pady=10)
    
    global conexion
    conexion = tk.StringVar(value="Serie")
    radio_serie = tk.Radiobutton(window, text="Serie", variable=conexion, value="Serie")
    radio_paralelo = tk.Radiobutton(window, text="Paralelo", variable=conexion, value="Paralelo")
    radio_serie.grid(row=0, column=1, padx=10, pady=10)
    radio_paralelo.grid(row=0, column=2, padx=10, pady=10)
    
    label_num_resistencias = tk.Label(window, text="Número de resistencias:")
    label_num_resistencias.grid(row=1, column=0, padx=10, pady=10)
    
    global entry_num_resistencias
    entry_num_resistencias = tk.Entry(window)
    entry_num_resistencias.grid(row=1, column=1, padx=10, pady=10)
    
    def generar_campos_resistencias():
        num_resistencias = int(entry_num_resistencias.get())
        for widget in frame_resistencias.winfo_children():
            widget.destroy()
        
        global entries_resistencias
        entries_resistencias = []
        
        for i in range(num_resistencias):
            label = tk.Label(frame_resistencias, text=f"Resistencia {i + 1} (Ω):")
            label.grid(row=i, column=0, padx=10, pady=5)
            
            entry = tk.Entry(frame_resistencias)
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries_resistencias.append(entry)
    
    boton_generar_resistencias = tk.Button(window, text="Generar campos de resistencias", command=generar_campos_resistencias)
    boton_generar_resistencias.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
    
    frame_resistencias = tk.Frame(window)
    frame_resistencias.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
    
    boton_calcular = tk.Button(window, text="Calcular", command=calcular)
    boton_calcular.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
    
    global label_resultado
    label_resultado = tk.Label(window, text="Resistencia Total: ")
    label_resultado.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
    
    window.mainloop()

crear_interfaz()
