from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from preprocess import cargar_datos

def entrenar_modelo():
    """
    Entrena un modelo Random Forest para la detección de tráfico malicioso.
    
    Returns:
        modelo: El modelo entrenado.
    """
    # Cargar los datos preprocesados
    X_train, X_test, y_train, y_test = cargar_datos()

    # Crear el modelo Random Forest
    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Entrenar el modelo
    print("Entrenando el modelo Random Forest...")
    modelo.fit(X_train, y_train)
    
    # Hacer predicciones en el conjunto de prueba
    y_pred = modelo.predict(X_test)
    
    # Evaluar el modelo
    print("Evaluación del modelo:")
    print(f"Exactitud: {accuracy_score(y_test, y_pred):.4f}")
    print(classification_report(y_test, y_pred))
    
    return modelo

if __name__ == "__main__":
    # Entrenar el modelo y evaluar los resultados
    modelo_entrenado = entrenar_modelo()
