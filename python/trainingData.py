import tkinter as tk
import threading

import serial
import training_interface
import personal_interface

# Configurar el puerto serie
ser = serial.Serial('COM5', 9600)  # Asegúrate de reemplazar 'COM5' con el puerto correcto

# Lista para almacenar los datos recibidos
data_list = []

folder_path = "D:\\OneDrive\\URV\\5º Curso\\TFG BrainLink\\BrainLink"


def actualizar_interfaz(data):
    """
    Función para actualizar la interfaz gráfica con los datos recibidos.
    Aquí puedes agregar el código para actualizar los widgets de la interfaz gráfica.
    """
    pass  # Reemplaza esto con el código real para actualizar la interfaz gráfica

def recibir_datos():
    
    while True:
        """
        "signal strength, attention, meditation, delta, theta, low alpha, high alpha, low beta, high beta, low gamma, high gamma"

         Signal strength ranges from 0 - 200. Counterintuitively, 0 means the unit has connected successfully, 
         and 200 means there is no signal.s

         IMPORTANTE: descartar siempre los primeros 3 valores de la lectura y tomarlos como calibrado
         Además, filtrar el rango de la señal
        """
        try:
            # Leer una línea de datos desde el puerto serie
            data = ser.readline().decode().strip()

            # Filtrar datos vacíos y procesar los datos
            if data:
                print("Datos recibidos desde Arduino:", data)
                # Agregar los datos a la lista solo si no está vacío
                data_list.append(data)

                # Actualizar la interfaz gráfica con los nuevos datos
                actualizar_interfaz(data)

        except UnicodeDecodeError as e:
            print("Error de decodificación:", e)
            continue  # Continúa con la siguiente iteración del bucle

        except KeyboardInterrupt:
            # Cerrar el puerto serie al finalizar
            ser.close()
            print("Puerto serie cerrado")

print("-------Selección usuario-------")
selected_user = personal_interface.user_window(data_list)

# Crear un hilo para recibir los datos en segundo plano
hilo_recepcion = threading.Thread(target=recibir_datos)
hilo_recepcion.daemon = True  # El hilo se detendrá cuando se cierre el programa principal
hilo_recepcion.start()

print("-------Selección tipo de datos-------")
training_interface.dataType_window()


