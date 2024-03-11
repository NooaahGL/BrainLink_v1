import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

def cargar_archivo(nombre_archivo):
    # Esta función se activará al hacer clic en un botón de archivo
    df = pd.read_csv(nombre_archivo)
    # Aquí puedes agregar el código para trabajar con el archivo cargado, por ejemplo:
    print("Archivo cargado con éxito:", nombre_archivo)
    print(df)

def guardar_datos(datos):
    # Esta función se activará al hacer clic en el botón de guardar
    nombre_archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if nombre_archivo:
        # Aquí puedes agregar el código para guardar los datos en el archivo seleccionado
        print("Datos guardados en:", nombre_archivo)

def crear_ventana():
    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Selector de archivos CSV")

    # Obtener lista de archivos CSV en la carpeta deseada
    ruta_carpeta = "D:\OneDrive\URV\5º Curso\TFG BrainLink\BrainLink\trainingData" 
    archivos_csv = [archivo for archivo in os.listdir(ruta_carpeta) if archivo.endswith('.csv')]

    # Crear botones para cada archivo CSV
    for nombre_archivo in archivos_csv:
        btn_cargar = tk.Button(ventana, text=nombre_archivo, command=lambda archivo=nombre_archivo: cargar_archivo(os.path.join(ruta_carpeta, archivo)))
        btn_cargar.pack()

    # Botón para guardar datos
    btn_guardar = tk.Button(ventana, text="Guardar datos", command=lambda: guardar_datos("datos_a_guardar"))
    btn_guardar.pack()

    ventana.mainloop()
