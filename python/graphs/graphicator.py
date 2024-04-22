import os

# Importa la clase AllDataGraphic del código anterior
from plot_functions import AllDataGraphic

def process_csv_files(input_folder, output_folder):
    """Filtra los archivos CSV en la carpeta de entrada y genera los gráficos en la carpeta de salida."""
    # Crea una instancia de la clase AllDataGraphic
    graphic_processor = AllDataGraphic(input_folder)
    
    # Procesa todos los archivos CSV en la carpeta de entrada
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):
            file_path = os.path.join(input_folder, file_name)
            graphic_processor.meditation_and_attention(file_path, output_folder)


# Rutas de entrada y salida
input_folder = "D:\\OneDrive\\URV\\5º Curso\\TFG BrainLink\\BrainLink\\trainingData"  # Cambia esto por tu ruta de entrada
output_folder = "D:\\OneDrive\\URV\\5º Curso\\TFG BrainLink\\BrainLink\\trainingData\\Graphics"  # Cambia esto por tu ruta de salida

# Procesa los archivos CSV en la carpeta de entrada y guarda los gráficos en la carpeta de salida
process_csv_files(input_folder, output_folder)

