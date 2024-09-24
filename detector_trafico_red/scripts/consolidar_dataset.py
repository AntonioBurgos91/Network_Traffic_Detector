import os
import pandas as pd

def consolidar_csv(carpeta_origen, archivo_salida):
    """
    Combina todos los archivos CSV en la carpeta_origen y los guarda en un archivo CSV único.
    
    Args:
        carpeta_origen (str): Directorio donde están los CSV de CICIDS2017.
        archivo_salida (str): Nombre del archivo CSV de salida consolidado.
    """
    archivos_csv = [f for f in os.listdir(carpeta_origen) if f.endswith('.csv')]
    print(f"Archivos encontrados: {archivos_csv}")

    # Lista para almacenar todos los DataFrames
    dataframes = []

    # Leer cada archivo CSV y agregarlo a la lista
    for archivo in archivos_csv:
        ruta_completa = os.path.join(carpeta_origen, archivo)
        print(f"Leyendo archivo: {ruta_completa}")
        df = pd.read_csv(ruta_completa)
        dataframes.append(df)

    # Concatenar todos los DataFrames
    dataset_consolidado = pd.concat(dataframes, ignore_index=True)
    
    # Guardar el dataset consolidado en un nuevo archivo CSV
    dataset_consolidado.to_csv(archivo_salida, index=False)
    print(f"Dataset consolidado guardado en: {archivo_salida}")

if __name__ == "__main__":
    # Ruta de la carpeta donde están los CSV de CICIDS2017
    carpeta_origen = 'data/CICIDS2017/'
    
    # Nombre del archivo CSV de salida
    archivo_salida = 'data/dataset_consolidado.csv'
    
    # Ejecutar la función de consolidación
    consolidar_csv(carpeta_origen, archivo_salida)
