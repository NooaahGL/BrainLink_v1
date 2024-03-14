import os
import tkinter as tk
from tkinter import simpledialog
from csv_functions import save_data

folder_path = "D:\\OneDrive\\URV\\5º Curso\\TFG BrainLink\\BrainLink\\trainingData"

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Selector usuario")
ventana.geometry("500x400")

# Variable global para almacenar el nombre del usuario seleccionado
selected_user = ""

def PI_actualizar_botones():
    global selected_user
    # Limpiar los botones anteriores
    for widget in ventana.winfo_children():
        widget.destroy()

    # Obtener lista de archivos CSV en la carpeta deseada
    archivos_csv = [archivo for archivo in os.listdir(folder_path) if archivo.endswith('.csv')]

    # Crear botones para cada archivo CSV
    for file_name in archivos_csv:
        name=file_name.replace(".csv", "")
        btn_cargar = tk.Button(ventana, text=name, command=lambda archivo=file_name: on_button_click(name), height=2, width=20)
        btn_cargar.pack()

    # Contenedor para los botones inferior
    frame_inferior = tk.Frame(ventana)
    frame_inferior.pack(side="bottom", fill="x")

    # Botón para crear un nuevo perfil
    btn_nuevoPerfil = tk.Button(frame_inferior, text="Nuevo perfil", command=lambda: PI_create_new_profil(), height=2, width=20)
    btn_nuevoPerfil.pack(side="left", padx=5, pady=5)  # Alinear botón a la izquierda y agregar espacio

    # Botón para salir
    btn_salir = tk.Button(frame_inferior, text="Salir", command=ventana.quit, height=2, width=20)
    btn_salir.pack(side="right", padx=5, pady=5)  # Alinear botón a la derecha y agregar espacio


def PI_create_new_profil():
    # Esta función se activará al hacer clic en el botón de "nuevo perfil"

    # Mostrar ventana emergente para que el usuario introduzca un nuevo nombre de perfil
    new_profil = simpledialog.askstring("Nuevo Perfil", "Introduce el nombre del nuevo perfil:")
    if new_profil:
        print("Nuevo perfil:", new_profil)
        file_name = new_profil+".csv"

        save_data(folder_path, file_name, None)

        # Actualizar los botones después de agregar un nuevo perfil
        PI_actualizar_botones()

def on_button_click(selected_user_name):
    global selected_user
    selected_user = selected_user_name
    ventana.destroy()

def user_window():

    # Etiqueta para solicitar el nombre del usuario
    lbl_usuario = tk.Label(ventana, text="¿Qué usuario está trabajando?", font=("Arial", 12))
    lbl_usuario.pack(pady=10)

    # Llamar a la función para actualizar los botones después de agregar un nuevo perfil
    PI_actualizar_botones()

    ventana.mainloop()

    return selected_user
