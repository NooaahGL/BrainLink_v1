import os
import tkinter as tk
from tkinter import simpledialog
import pandas as pd
from csv_functions import save_procesed_data

class SaveDataWindow:

    def __init__(self, file_name, data):

        self.window = tk.Tk()
        self.window.title("Guardar Datos")
        self.window.geometry("300x100")

        self.file_name = file_name
        self.data = data

        self.folder_path = "D:\\OneDrive\\URV\\5º Curso\\TFG BrainLink\\BrainLink\\trainingData"

    def create_window(self):

        self.lbl_data_type = tk.Label(self.window, text="Se guardarán los datos del usuario: " + self.file_name)
        self.lbl_data_type.pack(pady=10)

        # Contenedor para los botones inferior
        frame_inferior = tk.Frame(self.window)
        frame_inferior.pack(side="bottom", fill="x")

        self.btn_guardar = tk.Button(frame_inferior, text="Guardar", command=self.DI_cargar_archivo)
        self.btn_guardar.pack(side="left", padx=30, pady=10)

        self.btn_no_guardar = tk.Button(frame_inferior, text="No guardar", command=self.no_guardar_archivo)
        self.btn_no_guardar.pack(side="right", padx=30, pady=10)

        self.window.mainloop()

    def no_guardar_archivo(self):
        print("Datos no guardados.")
        self.window.destroy()

    def DI_cargar_archivo(self):
        
        # Añadir más adelante un filtrado de los datos
        if self.data:

            print ("**Los archivos serán guardados en el fichero: " + self.file_name+"**")

            file = self.file_name+".csv"
            ruta_completa = os.path.join(self.folder_path, file)
            save_procesed_data(self.folder_path, file, self.data)

            # Esta función se activará al hacer clic en un botón de archivo
            df = pd.read_csv(ruta_completa)

            # Aquí puedes agregar el código para trabajar con el archivo cargado, por ejemplo:
            print("Archivo cargado con éxito:", self.file_name)
            print(df)

            self.window.destroy()



