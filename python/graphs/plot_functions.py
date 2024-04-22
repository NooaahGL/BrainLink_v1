import pandas as pd
import matplotlib.pyplot as plt
import os

class AllDataGraphic:

    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.categories = ["Meditation", "Memory1", "Memory2", "UP", "DOWN", "Segundito"]

    def _read_csv(self, file_name):
        """Lee el archivo CSV, asigna nombres de columnas y convierte el tiempo a datetime."""
        self.folder_path = os.path.join(self.folder_path, file_name)
        
        df = pd.read_csv(self.folder_path)
        df.columns = ["Tiempo", "Categoría", "attention", "meditation", "delta", "theta", "low alpha", "high alpha", "low beta", "high beta"]
        df['Tiempo'] = pd.to_datetime(df['Tiempo'], unit='s')
        return df

    def plot_Alldata(self, file_name, output_folder):
        """Genera gráficos para las categorías especificadas."""
        df = self._read_csv(file_name)
        
        for category in self.categories:
            df_category = df[df['Categoría'] == category]
            plt.figure(figsize=(10, 6))
            for column in df_category.columns[2:]:
                plt.plot(df_category['Tiempo'], df_category[column], label=column)
            plt.xlabel('Tiempo')
            plt.ylabel('Valores')
            plt.title(f'Gráfico de valores para la categoría {category} - {os.path.splitext(os.path.basename(self.folder_path))[0]}')
            plt.legend()
            plt.grid(True)

            if output_folder:
                output_file_name = f"{category}_{os.path.splitext(os.path.basename(file_name))[0]}.png"
                output_path = os.path.join(output_folder, output_file_name)
                plt.savefig(output_path)
                plt.close()
            else: 
                plt.show()

    def meditation_and_attention(self, file_name, output_folder):
        """Genera gráficos de atención y meditación para cada categoría."""
        df = self._read_csv(file_name)
        df = df[["Tiempo", "Categoría", "attention", "meditation"]]

        for category in self.categories:
            df_category = df[df['Categoría'] == category]
            plt.figure(figsize=(10, 6))
            for column in df_category.columns[2:]:
                plt.plot(df_category['Tiempo'], df_category[column], label=column)
            plt.xlabel('Tiempo')
            plt.ylabel('Valores')
            plt.title(f'Gráfico de valores para la categoría {category} - {os.path.splitext(os.path.basename(self.folder_path))[0]}')
            plt.legend()
            plt.grid(True)

            if output_folder:
                output_file_name = f"{category}_{os.path.splitext(os.path.basename(file_name))[0]}.png"
                output_path = os.path.join(output_folder, output_file_name)
                plt.savefig(output_path)
                plt.close()
            else: 
                plt.show()


    def plot_waves(self, file_name, output_folder):
        """Genera gráficos de ondas para las categorías especificadas."""
        df = self._read_csv(file_name)
        df = df[["Tiempo", "Categoría", "delta", "theta", "low alpha", "high alpha", "low beta", "high beta"]]

        for category in self.categories:
            df_category = df[df['Categoría'] == category]
            plt.figure(figsize=(10, 6))
            for column in df_category.columns[2:]:
                plt.plot(df_category['Tiempo'], df_category[column], label=column)
            plt.xlabel('Tiempo')
            plt.ylabel('Valores')
            plt.title(f'Gráfico de valores para la categoría {category} - {os.path.splitext(os.path.basename(self.folder_path))[0]}')
            plt.legend()
            plt.grid(True)
            
            if output_folder:
                output_file_name = f"{category}_{os.path.splitext(os.path.basename(file_name))[0]}.png"
                output_path = os.path.join(output_folder, output_file_name)
                plt.savefig(output_path)
                plt.close()
            else: 
                plt.show()