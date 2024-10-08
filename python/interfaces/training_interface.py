import tkinter as tk
from tkinter import ttk



class DataTypeWindow:
    
    def __init__(self, selected_user):
        # Tipos de datos disponibles
        self.tipos_datos = ["Calibration", "Meditation", "Memory1", "Memory2", "UP", "DOWN", "Segundito"]
        # Crear checkboxes para los tipos de datos
        self.checkboxes = []
        # Selected datatype
        self.data_type = None
        self.selected_user = selected_user

        # Crear una nueva instancia de Tk para la ventana de datos
        self.window = tk.Tk()
        self.window.title("Selección de Datos")
        self.window.geometry("400x300")

        # Crear un estilo personalizado para los Checkbuttons
        self.style = ttk.Style()
        self.style.configure('Checkbutton.TCheckbutton', font=('Arial', 10))  # Establecer tamaño de fuente


    # Función para manejar el evento de selección/deselección de los checkboxes
    def checkbox_callback(self, checkbox_index):
        for i, tipo in enumerate(self.tipos_datos):
            if i != checkbox_index:
                self.checkboxes[i].set(False)  # Deseleccionar las otras checkboxes
            else:
                if self.checkboxes[i].get():
                    if self.data_type != tipo:  # Solo actualiza selected si la selección cambia
                        self.data_type = tipo
                else:
                    self.data_type = None
                        
    def getDataType(self):
        return self.data_type

    def exit(self):
        global save
        save = True
        self.window.destroy()

    def create_window(self):
        global save
        save = False

        # Texto principal: este no sale 
        self.lbl_usuario = tk.Label(self.window, text="Selecciona el tipo de datos que se están registrando:", font=("Arial", 12))
        self.lbl_usuario.pack(pady=10)

        for i, tipo in enumerate(self.tipos_datos):
            var = tk.BooleanVar()
            checkbox = ttk.Checkbutton(self.window, text=tipo, variable=var, command=lambda i=i: self.checkbox_callback(i), padding=(10, 10), style='Checkbutton.TCheckbutton')
            checkbox.pack(anchor=tk.W)
            self.checkboxes.append(var)

        # Crear botón para salir
        btn_salir = tk.Button(self.window, text="Salir", command=self.exit, height=2, width=20)
        btn_salir.pack(side=tk.BOTTOM)

        self.window.mainloop()
        
        return save
        