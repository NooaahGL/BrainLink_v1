import os
import pandas as pd
from csv_functions import append_data


# Directorio que contiene los archivos CSV
folder_path = "D:\\OneDrive\\URV\\5º Curso\\TFG BrainLink\\BrainLink\\trainingData"
# Guardar el resultado en un nuevo archivo CSV
save_path = "D:\\OneDrive\\URV\\5º Curso\\TFG BrainLink\\BrainLink\\data"

# Lista para almacenar los datos procesados
procesed_data = []

# Iterar sobre cada archivo en el directorio
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        filepath = os.path.join(folder_path, filename)
        print("Leyendo archivo:", filepath)  # Imprimir el nombre del archivo antes de leerlo
        try:
            # Leer el archivo CSV
            df = pd.read_csv(filepath)
            # Agregar los datos del DataFrame a la lista procesed_data
            procesed_data.append(df.values.tolist())

        except Exception as e:
            print("Error al leer el archivo:", filepath)
            print("Mensaje de error:", str(e))

# Verificar si se han almacenado datos en procesed_data
if procesed_data:
    # Guardar los datos procesados en un archivo CSV
    append_data(save_path, 'media.csv', procesed_data)
    print("Datos procesados guardados correctamente.")
else:
    print("No se encontraron datos para procesar.")
