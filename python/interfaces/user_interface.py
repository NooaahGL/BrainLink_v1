import os
import tkinter as tk
from tkinter import simpledialog
from csv_functions import save_data

class UserWindow:
        
    def __init__(self):

        self.folder_path = "D:\\OneDrive\\URV\\5º Curso\\TFG BrainLink\\BrainLink\\trainingData"
        
        # Variable global para almacenar el nombre del usuario seleccionado
        self.selected_user = None

        # Crear ventana principal
        self.window = tk.Tk()
        self.window.title("Selector usuario")
        self.window.geometry("500x400")


    def UI_actualizar_botones(self):
        global selected_user
        # Limpiar los botones anteriores
        for widget in self.window.winfo_children():
            widget.destroy()

        # Obtener lista de archivos CSV en la carpeta deseada
        archivos_csv = [archivo for archivo in os.listdir(self.folder_path) if archivo.endswith('.csv')]

        # Texto principal
        self.lbl_usuario = tk.Label(self.window, text="¿Qué usuario está trabajando?", font=("Arial", 12))
        self.lbl_usuario.pack(pady=10)
        
        # Crear botones para cada archivo CSV
        for file_name in archivos_csv:
            name=file_name.replace(".csv", "")
            btn_cargar = tk.Button(self.window, text=name, command=lambda archivo=file_name: self.on_button_click(name), height=2, width=20)
            btn_cargar.pack()

        # Contenedor para los botones inferior
        frame_inferior = tk.Frame(self.window)
        frame_inferior.pack(side="bottom", fill="x")

        # Botón para crear un nuevo perfil
        btn_nuevoPerfil = tk.Button(frame_inferior, text="Nuevo perfil", command=self.UI_create_new_profil, height=2, width=20)
        btn_nuevoPerfil.pack(side="left", padx=5, pady=5)  # Alinear botón a la izquierda y agregar espacio

        # Botón para salir
        btn_salir = tk.Button(frame_inferior, text="Salir", command=self.window.quit, height=2, width=20)
        btn_salir.pack(side="right", padx=5, pady=5)  # Alinear botón a la derecha y agregar espacio


    def UI_create_new_profil(self):
        # Esta función se activará al hacer clic en el botón de "nuevo perfil"

        # Mostrar window emergente para que el usuario introduzca un nuevo nombre de perfil
        new_profil = simpledialog.askstring("Nuevo Perfil", "Introduce el nombre del nuevo perfil:")
        if new_profil:
            print("Nuevo perfil:", new_profil)
            file_name = new_profil+".csv"

            save_data(self.folder_path, file_name, None)

            # Actualizar los botones después de agregar un nuevo perfil
            self.UI_actualizar_botones()

    def on_button_click(self, selected_user_name):
        global selected_user
        selected_user = selected_user_name
        self.window.destroy()

    def user_window(self):

        # Etiqueta para solicitar el nombre del usuario
        lbl_usuario = tk.Label(self.window, text="¿Qué usuario está trabajando?", font=("Arial", 12))
        lbl_usuario.pack(pady=10)

        # Llamar a la función para actualizar los botones después de agregar un nuevo perfil
        self.UI_actualizar_botones()

        self.window.mainloop()

        return selected_user
