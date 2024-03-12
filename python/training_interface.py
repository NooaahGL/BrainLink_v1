import tkinter as tk
from tkinter import ttk

# Tipos de datos disponibles
tipos_datos = ["Attention", "Meditation", "Delta"]

# Crear window principal
window = tk.Tk()
window.title("Selección de Datos")
window.geometry("400x300")

# Crear checkboxes para los tipos de datos
checkboxes = []

# Función para manejar el evento de selección/deselección de los checkboxes
def checkbox_callback():
    for i, tipo in enumerate(tipos_datos):
        if checkboxes[i].get():
            print(f"Seleccionado: {tipo}")
        #else:
            #print(f"Deseleccionado: {tipo}")

# Función para salir de la aplicación
def salir():
    window.destroy()

def dataType_window():

    for tipo in tipos_datos:
        var = tk.BooleanVar()
        checkbox = ttk.Checkbutton(window, text=tipo, variable=var, command=checkbox_callback)
        checkbox.pack(anchor=tk.W)
        checkboxes.append(var)

    # Crear botón para salir
    btn_salir = tk.Button(window, text="Salir", command=salir)
    btn_salir.pack(side=tk.BOTTOM)


    window.mainloop()