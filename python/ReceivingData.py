import serial

# Configurar el puerto serie
ser = serial.Serial('COM5', 9600)  # Asegúrate de reemplazar 'COM4' con el puerto correcto

# Lista para almacenar los datos recibidos
data_list = []

try:
    while True:
        # Leer una línea de datos desde el puerto serie
        data = ser.readline().decode().strip()
        
        # Procesar los datos como desees
        print("Datos recibidos desde Arduino:", data)

        # Agregar los datos a la lista
        data_list.append(data)

except KeyboardInterrupt:
    # Cerrar el puerto serie al finalizar
    ser.close()
    print("Puerto serie cerrado")
    