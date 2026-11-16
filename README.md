# Data Analytics and Machine Learning Challenge

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)](https://www.json.org/)
[![Markdown](https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white)](https://www.markdownguide.org/)

## Descripción

Repositorio individual para el ML Challenge de la asignatura Data Analytics (2026-2).

El proyecto aborda la predicción de retrasos en entregas de comercio electrónico utilizando el conjunto de datos Olist, mediante técnicas de aprendizaje automático, evaluación de modelos, reducción de dimensionalidad y validación estadística.

Los experimentos se desarrollan progresivamente en notebooks de Jupyter, manteniendo criterios de reproducibilidad y separación de los conjuntos de entrenamiento, validación y prueba.

## Configuración del Estudiante

- **ID asignado:** 19.
- **Semilla de partición:** 1019.
- **Tamaño de muestra:** 35.000 pedidos.
- **Entrenamiento:** 24.500 pedidos (70 %).
- **Validación:** 5.250 pedidos (15 %).
- **Prueba:** 5.250 pedidos (15 %).
- **Variables predictoras:** 28 (24 numéricas y 4 categóricas).

## Estado del Proyecto

**Semana 14 completada.**

| Semana | Actividades principales | Estado |
|---|---|---|
| 12 | Modelos de clasificación y regresión, métricas de evaluación y análisis de costos. | Completada |
| 14 | Reducción dimensional con PCA, comparación de modelos de clasificación, regularización y prueba Kolmogorov-Smirnov. | Completada |

## Resultados Destacados

### Semana 12 - Modelos base

Se desarrollaron modelos para predecir retrasos en las entregas y estimar su duración.

La regresión logística con ponderación de clases obtuvo los siguientes resultados en validación:

| Métrica | Resultado |
|---|---:|
| Accuracy | 0.6547 |
| Precision | 0.1183 |
| Recall | 0.6366 |
| F1 | 0.1996 |
| ROC-AUC | 0.6925 |
| AP | 0.1402 |
| Costo empresarial | 17.987 BRL |

Adicionalmente, se evaluó un modelo de regresión Ridge para estimar la magnitud de los retrasos, obteniendo un MAE de 5.21 días.

### Semana 14 - PCA y validación estadística

Se aplicó PCA sobre las 24 variables numéricas, conservando al menos el 90 % de la varianza explicada.

| Indicador | Resultado |
|---|---:|
| Variables numéricas originales | 24 |
| Componentes principales seleccionados | 15 |
| Reducción de dimensionalidad | 37.50 % |
| Varianza explicada acumulada | 90.62 % |

Posteriormente, se evaluaron cuatro configuraciones de regresión logística, variando la aplicación de PCA y el parámetro de regularización `C`.

| Modelo | PCA | C | F1 | AP | Costo (BRL) |
|---|---|---:|---:|---:|---:|
| A | No | 1.0 | 0.1996 | 0.1402 | 17.987 |
| B | Sí | 1.0 | 0.1872 | 0.1130 | 18.589 |
| C | Sí | 0.1 | 0.1846 | 0.1138 | 18.710 |
| D | Sí | 10.0 | 0.1874 | 0.1122 | 18.610 |

El modelo A, sin PCA, presentó el mejor rendimiento entre las configuraciones evaluadas.

Sin embargo, su costo empresarial de 17.987 BRL superó el costo de referencia de 12.425 BRL correspondiente a una estrategia sin alertas.

Esto evidencia que una mejora en las métricas predictivas no garantiza una reducción de los costos empresariales.

También se aplicó la prueba de Kolmogorov-Smirnov sobre `valor_flete`, obteniendo:

- **Estadístico D:** 0.0092.
- **Valor p:** 0.852027.
- **Nivel de significancia:** 0.05.
- **Decisión:** No rechazar la hipótesis nula.

No se encontró evidencia estadísticamente significativa de diferencias entre las distribuciones de `valor_flete` en entrenamiento y validación.

## Estructura del Repositorio

```text
data-analytics-ml-challenge/
├── data/
│   ├── processed/
│   └── raw/
├── notebooks/
│   ├── Semana_12/
│   │   ├── Resultados-Semana_12.md
│   │   └── S12_ML_Challenge.ipynb
│   ├── Semana_14/
│   │   ├── Resultados-Semana_14.md
│   │   └── S14_ML_Challenge.ipynb
│   └── README.md
├── reports/
│   ├── S12_resultados_ID_19.json
│   └── S14_resultados_ID_19.json
├── src/
│   └── iniciarEntorno/
│       ├── __init__.py
│       └── gestor_dependencias.py
├── venv/
├── .gitignore
├── README.md
└── requirements.txt
```

La carpeta `venv/` corresponde al entorno virtual local y no debe incluirse en el repositorio remoto. Las carpetas `data/raw/` y `data/processed/` se utilizan para organizar los datos de trabajo, evitando publicar conjuntos de datos originales o muestras completas.

## Instalación y Ejecución

### 1. Clonar el repositorio

```powershell
git clone https://github.com/cMancillaValle/data-analytics-ml-challenge.git
cd data-analytics-ml-challenge
```

### 2. Crear y activar el entorno virtual

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

### 4. Ejecutar los notebooks

Abrir el proyecto en Visual Studio Code o Jupyter y seleccionar el intérprete de Python del entorno virtual.

Los notebooks se encuentran en:

- `notebooks/Semana_12/S12_ML_Challenge.ipynb`
- `notebooks/Semana_14/S14_ML_Challenge.ipynb`

Ejecutar las celdas en orden, desde la preparación del entorno hasta la generación de los resultados.

Los experimentos requieren acceso a los datos de Olist utilizados por el laboratorio.

## Reproducibilidad

Los experimentos utilizan el ID 19 y la semilla 1019 para mantener una muestra y unas particiones consistentes.

Los modelos se entrenan exclusivamente con el conjunto de entrenamiento y se comparan utilizando el conjunto de validación.

El conjunto de prueba permanece reservado para una evaluación independiente posterior.

La Semana 14 incorpora una sección de autoverificación que comprueba la integridad de las particiones, la configuración de PCA, la consistencia de las métricas y el cálculo de los costos.

Los resultados se exportan en formato JSON para facilitar su consulta y trazabilidad.

## Documentación y Resultados

| Semana | Notebook | Análisis | Reporte JSON |
|---|---|---|---|
| 12 | [S12_ML_Challenge.ipynb](notebooks/Semana_12/S12_ML_Challenge.ipynb) | [Resultados Semana 12](notebooks/Semana_12/Resultados-Semana_12.md) | [S12_resultados_ID_19.json](reports/S12_resultados_ID_19.json) |
| 14 | [S14_ML_Challenge.ipynb](notebooks/Semana_14/S14_ML_Challenge.ipynb) | [Resultados Semana 14](notebooks/Semana_14/Resultados-Semana_14.md) | [S14_resultados_ID_19.json](reports/S14_resultados_ID_19.json) |

## Próximas Mejoras

Como continuación de los experimentos, se propone:

1. Incorporar información geográfica mediante una variable que combine el estado del vendedor y el estado del cliente.
2. Evaluar distintos umbrales de clasificación para minimizar el costo empresarial de falsos positivos y falsos negativos.
3. Comparar las nuevas configuraciones con la línea base actual, conservando las mismas particiones y evitando utilizar el conjunto de prueba durante el ajuste.

Estas mejoras se consideran trabajo futuro y no forman parte de los resultados oficiales de la Semana 14.
