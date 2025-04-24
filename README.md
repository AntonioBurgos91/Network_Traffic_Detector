# 🌐 Network Traffic Detector | Análisis Avanzado de Tráfico de Red

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Active%20Development-yellowgreen)]()

**Repositorio:** [github.com/AntonioBurgos91/Network_Traffic_Detector](https://github.com/AntonioBurgos91/Network_Traffic_Detector)

## 🚀 Descripción del Proyecto
Sistema de análisis de tráfico de red para detección de patrones sospechosos y clasificación de tráfico mediante técnicas de machine learning. Desarrollado como herramienta para:
- Monitoreo en tiempo real
- Detección de anomalías
- Clasificación de protocolos
- Identificación de posibles amenazas de seguridad

## 🔍 Características Clave
- **Análisis Multicapa:** Inspección desde capa 2 hasta capa 7 del modelo OSI
- **Motor de ML Integrado:** Modelos preentrenados para detección de intrusiones
- **Visualización Interactiva:** Dashboard con métricas en tiempo real
- **Soporte para PCAP:** Procesamiento de capturas de tráfico profesional

## 📊 Dataset (Consideraciones Especiales)
**Nombre:** CIC-IDS-2017 Dataset (Custom Extended Version)  
**Tamaño Total:** ~48 GB  
**Contenido:**
- Capturas completas de tráfico de red (`*.peap`) 
- Checksums de verificación (`*.md5`)
- Tráfico etiquetado (ataques DDoS, Botnets, inyecciones SQL)

⚠️ **Nota importante:** Debido a las políticas de GitHub sobre archivos grandes (>100MB), los archivos originales del dataset no están incluidos en este repositorio. [Consulta la sección de descarga del dataset](#https://www.unb.ca/cic/datasets/ids-2017.html) para obtener instrucciones de acceso.

## 🛠️ Tecnologías Utilizadas
| Categoría          | Herramientas                                                                 |
|---------------------|------------------------------------------------------------------------------|
| **Lenguajes**       | Python 3.8, SQL                                                             |
| **ML Framework**    | TensorFlow 2.8, Scikit-learn 1.0                                             |
| **Procesamiento**   | Apache Spark, Pandas, NumPy                                                  |
| **Visualización**   | Grafana, Plotly                                                              |
| **Herramientas**    | Wireshark, Zeek (Bro IDS), Elastic Stack                                    |

## 📥 Instalación
```bash
# Clonar repositorio
git clone https://github.com/AntonioBurgos91/Network_Traffic_Detector.git

# Instalar dependencias
pip install -r requirements.txt

# Configurar entorno (ver docs/setup_guide.md)
python setup.py --configure
