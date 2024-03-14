import threading
import serial
import time
import numpy as np

import interfaces.training_interface as TI
import interfaces.user_interface as UI

# Configurar el puerto serie
ser = serial.Serial('COM5', 9600)  # Asegúrate de reemplazar 'COM5' con el puerto correcto

# Lista para almacenar los datos recibidos y procesados
received_data = []
procesed_data = []

folder_path = "D:\\OneDrive\\URV\\5º Curso\\TFG BrainLink\\BrainLink"

counter = 0


def process_data(array):
    global counter
    """
    Función para actualizar la interfaz gráfica con los datos recibidos.
    Aquí puedes agregar el código para actualizar los widgets de la interfaz gráfica.
    """
    # Obtener la marca de tiempo de procesado (segundos desde el 1 de enero de 1970).
    # ¿es distinto el tiempo de procesado con el tiempo de pensamienot? 
    # ¿Cuanto error hay? ¿He de sumar el error del aparato, con el de recepción y tratamiento de datos?
    timestamp = int(time.time())

    #filtrar los primeros 4 valores como valores de calibrado y que la señal sea mayor de 200
    if (counter > 3): #and (array[0] != 200):

        # Seleccionar los elementos del 1 al 3 [timestamp, attention, meditation, delta]
        calibrated_values = array[1:4]
        
        #dataType = data_window.data_type
        calibrated_values = np.append([timestamp, data_window.data_type], calibrated_values)

        print("Datos procesados:", calibrated_values)
        
        procesed_data.append(calibrated_values)


    pass  # Reemplaza esto con el código real para actualizar la interfaz gráfica

def recibir_datos():
    global counter
    
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

                # Dividir la cadena en valores separados por comas y convertirlos en números
                values = [int(valor) for valor in data.split(',')]
                array = np.array(values)

                # Agregar los datos sin procesar a la lista solo si no está vacío
                received_data.append(array)

                # Procesa los datos recibidos
                process_data(array)

                counter += 1
                print ("counter:", counter)

        except UnicodeDecodeError as e:
            print("Error de decodificación:", e)
            continue  # Continúa con la siguiente iteración del bucle

        except KeyboardInterrupt:
            # Cerrar el puerto serie al finalizar
            ser.close()
            print("Puerto serie cerrado")

print("-------Selección usuario-------")
user_window = UI.UserWindow()
selected_user = user_window.user_window()
print("Usuario seleccionado: ", selected_user)

if selected_user:
    # Crear un hilo para recibir los datos en segundo plano
    hilo_recepcion = threading.Thread(target=recibir_datos)
    hilo_recepcion.daemon = True  # El hilo se detendrá cuando se cierre el programa principal
    hilo_recepcion.start()

    print("-------Selección tipo de datos-------")
    data_window = TI.DataTypeWindow()
    data_window.create_window()

else:
    print("No se ha seleccionado ningún usuario. Saliendo del programa.")

