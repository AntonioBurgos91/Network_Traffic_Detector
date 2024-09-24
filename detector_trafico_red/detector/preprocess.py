import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def cargar_datos(ruta='data/dataset_consolidado.csv'):
    # Cargar el dataset
    datos = pd.read_csv(ruta)

    # Limpiar los nombres de las columnas eliminando espacios
    datos.columns = datos.columns.str.strip()

    # Acceder a la columna de etiquetas
    etiquetas = datos['Label']

    # Eliminar columnas innecesarias
    columnas_a_eliminar = ['Flow ID', 'Src IP', 'Dst IP', 'Timestamp']  # Ajusta según sea necesario
    datos = datos.drop(columns=[col for col in columnas_a_eliminar if col in datos.columns])

    # Las características serán todas las columnas menos 'Label'
    caracteristicas = datos.drop(['Label'], axis=1)

    # Convertir las características a tipo numérico, forzando conversiones
    caracteristicas = caracteristicas.apply(pd.to_numeric, errors='coerce')

    # Verificar y manejar valores nulos
    nulos_antes = caracteristicas.isnull().sum().sum()
    if nulos_antes > 0:
        print(f"Valores nulos encontrados en las características: {nulos_antes}")
        # Rellenar valores nulos con la media
        caracteristicas = caracteristicas.fillna(caracteristicas.mean())
        nulos_despues = caracteristicas.isnull().sum().sum()
        print(f"Valores nulos después de rellenar: {nulos_despues}")

    # Verificar y manejar valores infinitos
    infinitos_antes = np.isinf(caracteristicas).sum().sum()
    if infinitos_antes > 0:
        print(f"Valores infinitos encontrados en las características: {infinitos_antes}")
        # Reemplazar valores infinitos con NaN y luego rellenar
        caracteristicas = caracteristicas.replace([np.inf, -np.inf], np.nan)
        caracteristicas = caracteristicas.fillna(caracteristicas.mean())
        infinitos_despues = np.isinf(caracteristicas).sum().sum()
        print(f"Valores infinitos después de rellenar: {infinitos_despues}")

    # Convertir a tipo numérico de forma explícita
    caracteristicas = caracteristicas.astype(float)

    # Dividir los datos en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(caracteristicas, etiquetas, test_size=0.3, random_state=42)

    # Normalizar las características
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # Configurar Pandas para evitar la advertencia de downcasting
    pd.set_option('future.no_silent_downcasting', True)
    
    X_train, X_test, y_train, y_test = cargar_datos()
    print(f"Forma del conjunto de entrenamiento: {X_train.shape}")
    print(f"Forma del conjunto de prueba: {X_test.shape}")