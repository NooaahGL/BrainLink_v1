import csv
import os


def show_data(data_list):
    """
    Imprime los datos almacenados en la lista en formato de matriz.

    Args:
    data_list: Lista de datos a imprimir en formato de matriz.
    """
    for row in data_list:
        print(row.split(','))  # Datos separados por comas


def verify_and_create(ruta_completa, file_name):
    """
    Verifica si un archivo CSV existe en una carpeta.
    Si no existe, crea un nuevo archivo CSV vacío en la carpeta especificada.

    Args:
    folder_path: Ruta de la carpeta donde se debe verificar la existencia del archivo CSV.
    file_name: Nombre del archivo CSV.
    """

    # Verificar si el archivo CSV existe
    if not os.path.exists(ruta_completa):
        # Si el archivo no existe, crear un nuevo archivo CSV vacío
        with open(ruta_completa, 'w', newline='') as archivo_csv:
            # Utilizar csv.writer para crear el archivo CSV vacío
            escritor_csv = csv.writer(archivo_csv)
            print(f"El archivo CSV '{file_name}' no existe. Se ha creado un nuevo archivo CSV vacío en '{ruta_completa}'.")
    #else:
        # print(f"El archivo CSV '{file_name}' ya existe en '{file_name}'.")


def save_data(folder_path, file_name, data_list):
    """
    Guarda los datos almacenados en la lista en un archivo CSV.

    Args:
    folder_path: Ruta de la carpeta donde se debe guardar el archivo CSV.
    data_list: Lista de datos a guardar en el archivo CSV.
    """   
    ruta_completa = os.path.join(folder_path, file_name)
    #print("Ruta en save Data: " + ruta_completa)
    verify_and_create(ruta_completa, file_name)
    

    with open(ruta_completa, 'a', newline='') as archivo_csv: # Modificado para abrir en modo de agregar ('a')
        escritor_csv = csv.writer(archivo_csv)
        for row in data_list:
            escritor_csv.writerow(row.split(','))  
