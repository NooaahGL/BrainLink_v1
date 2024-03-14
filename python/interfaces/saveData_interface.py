import os
import tkinter as tk
from tkinter import simpledialog
import pandas as pd
from csv_functions import save_data

folder_path = "D:\\OneDrive\\URV\\5º Curso\\TFG BrainLink\\BrainLink\\trainingData"

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Selector usuario")
ventana.geometry("500x400")

def actualizar_botones(data):
    # Limpiar los botones anteriores
    for widget in ventana.winfo_children():
        widget.destroy()

    # Obtener lista de archivos CSV en la carpeta deseada
    archivos_csv = [archivo for archivo in os.listdir(folder_path) if archivo.endswith('.csv')]

    # Crear botones para cada archivo CSV
    for file_name in archivos_csv:
        name=file_name.replace(".csv", "")
        btn_cargar = tk.Button(ventana, text=name, command=lambda archivo=file_name: cargar_archivo(file_name, data), height=2, width=20)
        btn_cargar.pack()

    # Contenedor para los botones inferior
    frame_inferior = tk.Frame(ventana)
    frame_inferior.pack(side="bottom", fill="x")

    # Botón para crear un nuevo perfil
    btn_nuevoPerfil = tk.Button(frame_inferior, text="Nuevo perfil", command=lambda: create_new_profil(data), height=2, width=20)
    btn_nuevoPerfil.pack(side="left", padx=5, pady=5)  # Alinear botón a la izquierda y agregar espacio

    # Botón para salir
    btn_salir = tk.Button(frame_inferior, text="Salir", command=ventana.quit, height=2, width=20)
    btn_salir.pack(side="right", padx=5, pady=5)  # Alinear botón a la derecha y agregar espacio

    

def cargar_archivo(file_name, data):
    
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

def create_new_profil(data):
    # Esta función se activará al hacer clic en el botón de "nuevo perfil"

    # Mostrar ventana emergente para que el usuario introduzca un nuevo nombre de perfil
    new_profil = simpledialog.askstring("Nuevo Perfil", "Introduce el nombre del nuevo perfil:")
    if new_profil:
        print("Nuevo perfil:", new_profil)

        cargar_archivo(new_profil+".csv", data)

        # Actualizar los botones después de agregar un nuevo perfil
        actualizar_botones(data)


def saveData_window(data):

    # Etiqueta para solicitar el nombre del usuario
    lbl_usuario = tk.Label(ventana, text="¿Qué usuario está trabajando?", font=("Arial", 12))
    lbl_usuario.pack(pady=10)

    # Llamar a la función para actualizar los botones después de agregar un nuevo perfil
    actualizar_botones(data)

    ventana.mainloop()

