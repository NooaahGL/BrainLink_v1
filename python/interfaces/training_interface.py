import tkinter as tk
from tkinter import ttk

class DataTypeWindow:
    
   
    def __init__(self):
        # Tipos de datos disponibles
        self.tipos_datos = ["Attention", "Meditation", "Delta"]
        # Crear checkboxes para los tipos de datos
        self.checkboxes = []
        # Selected datatype
        self.data_type = None

    # Función para manejar el evento de selección/deselección de los checkboxes
    def checkbox_callback(self):
        for i, tipo in enumerate(self.tipos_datos):
            if self.checkboxes[i].get():
                if self.data_type != tipo:  # Solo actualiza selected si la selección cambia
                    #print(f"Seleccionado: {tipo}")
                    self.data_type = tipo
            #else:
                #print(f"Deseleccionado: {tipo}")
                    
    def getDataType(self):
        return self.data_type

    def create_window(self):
        # Crear una nueva instancia de Tk para la ventana de datos
        window = tk.Tk()
        window.title("Selección de Datos")
        window.geometry("400x300")

        for tipo in self.tipos_datos:
            var = tk.BooleanVar()
            checkbox = ttk.Checkbutton(window, text=tipo, variable=var, command=self.checkbox_callback)
            checkbox.pack(anchor=tk.W)
            self.checkboxes.append(var)

        # Crear botón para salir
        btn_salir = tk.Button(window, text="Salir", command=window.quit, height=2, width=20)
        btn_salir.pack(side=tk.BOTTOM)

        window.mainloop()
        
    
