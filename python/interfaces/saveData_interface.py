import os
import tkinter as tk
from tkinter import simpledialog
import pandas as pd
from csv_functions import save_data

class SaveDataWindow:

    def __init__(self, parent, data_type):
        self.parent = parent
        self.data_type = data_type

        self.window = tk.Toplevel(parent)
        self.window.title("Guardar Datos")
        self.window.geometry("500x400")

        self.lbl_data_type = tk.Label(self.window, text="Tipo de Datos: " + data_type)
        self.lbl_data_type.pack(pady=10)

        self.btn_guardar = tk.Button(self.window, text="Guardar", command=self.guardar_datos)
        self.btn_guardar.pack(pady=10)

        self.folder_path = "D:\\OneDrive\\URV\\5º Curso\\TFG BrainLink\\BrainLink\\trainingData"


    def DI_cargar_archivo(self, file_name, data):
        
        # Añadir más adelante un filtrado de los datos
        if data:

            print ("**Últimos archivos guardados en el fichero: " + file_name+"**")
            ruta_completa = os.path.join(folder_path, file_name)

            save_data(folder_path, file_name, data)

            # Esta función se activará al hacer clic en un botón de archivo
            df = pd.read_csv(ruta_completa)

            # Aquí puedes agregar el código para trabajar con el archivo cargado, por ejemplo:
            print("Archivo cargado con éxito:", file_name)
            print(df)




