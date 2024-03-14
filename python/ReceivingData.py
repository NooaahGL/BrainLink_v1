import serial
from datetime import datetime
from csv_functions import save_data

import interfaces.user_interface as user_interface


# Configurar el puerto serie
ser = serial.Serial('COM5', 9600)  # Asegúrate de reemplazar 'COM4' con el puerto correcto

# Lista para almacenar los datos recibidos
data_list = []

folder_path = "D:\\OneDrive\\URV\\5º Curso\\TFG BrainLink\\BrainLink"

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

        # Filtrar datos vacíos y procesado de los datos
        if data:
            print("Datos recibidos desde Arduino:", data)
            # Agregar los datos a la lista solo si no está vacío
            data_list.append(data)

    except UnicodeDecodeError as e:
        print("Error de decodificación:", e)
        continue  # Continúa con la siguiente iteración del bucle

    except KeyboardInterrupt:
        # Cerrar el puerto serie al finalizar
        ser.close()
        print("Puerto serie cerrado")

        #show_data(data_list)
        file_name =  "data\\"+ datetime.now().strftime('%Y_%m_%d') + ".csv"
        save_data(folder_path, file_name, data_list)

        print("-------CREACIÓN DE LA INTERFAZ DE USUARIO-------")
        selected_user = user_interface.user_window()
        print("Usuario seleccionado: " +selected_user)
        break


        
    