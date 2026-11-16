# Data Analytics and Machine Learning Challenge

> **Nota importante para Google Colab:** Si se ejecutan los cuadernos desde Google Colab, se deben omitir las instrucciones de instalación del entorno virtual local descritas en este `README.md`. Las dependencias se gestionan en el entorno de Colab, y los cuadernos y entregables de cada etapa se encuentran organizados dentro de la carpeta correspondiente a cada semana.

---

## Cuadernos disponibles

| Semana | Cuaderno | Actividades principales | Estado |
|---|---|---|---|
| 12 | [S12_ML_Challenge.ipynb](Semana_12/S12_ML_Challenge.ipynb) | Clasificación, regresión, métricas y análisis de costos. | Completada |
| 14 | [S14_ML_Challenge.ipynb](Semana_14/S14_ML_Challenge.ipynb) | PCA, comparación de modelos, regularización y prueba Kolmogorov-Smirnov. | Completada |

Cada semana cuenta con un documento Markdown de resultados y un reporte JSON generado por el notebook.

### Documentación de resultados

- **Semana 12:** [Resultados-Semana_12.md](Semana_12/Resultados-Semana_12.md)
- **Semana 14:** [Resultados-Semana_14.md](Semana_14/Resultados-Semana_14.md)

Los reportes estructurados se almacenan en la carpeta `reports/` de la raíz del proyecto.

---

## Configuración e instalación del entorno local

Para ejecutar los cuadernos en un entorno local, por ejemplo, desde Visual Studio Code, se deben seguir los siguientes pasos para configurar el entorno virtual e instalar las dependencias necesarias.

### 1. Crear el entorno virtual (`venv`)

Abrir una terminal en la raíz del proyecto (`data-analytics-ml-challenge`) y ejecutar:

```bash
python -m venv venv
```

### 2. Activar el entorno virtual

El comando de activación depende del sistema operativo y de la terminal utilizada.

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**Solución de problemas:** Si aparece un error relacionado con las políticas de ejecución de PowerShell, ejecutar:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope Process
```

A continuación, volver a ejecutar el comando de activación.

Este cambio se aplica únicamente al proceso actual de PowerShell y deja de tener efecto al cerrar la sesión.

**Windows (CMD):**

```bat
.\venv\Scripts\activate.bat
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Seleccionar el kernel en VS Code / Jupyter

Abrir el notebook correspondiente y seleccionar el intérprete de Python del entorno virtual `venv/` como kernel activo.

Los cuadernos disponibles son:

- `notebooks/Semana_12/S12_ML_Challenge.ipynb`
- `notebooks/Semana_14/S14_ML_Challenge.ipynb`

En Windows, el intérprete del entorno virtual se encuentra en:

```text
venv/Scripts/python.exe
```

### 4. Instalación de dependencias

Los cuadernos utilizan el módulo `src/iniciarEntorno/gestor_dependencias.py`, encargado de verificar e instalar las librerías necesarias especificadas en `requirements.txt`.

Al ejecutar la celda de preparación del entorno, se invoca este módulo para gestionar las dependencias requeridas.

Como alternativa, las dependencias pueden instalarse manualmente desde la raíz del proyecto:

```powershell
python -m pip install -r requirements.txt
```

### 5. Ejecutar el cuaderno

Una vez seleccionado el kernel y preparadas las dependencias:

1. Abrir el notebook de la semana correspondiente.
2. Ejecutar las celdas en orden, desde la preparación de datos hasta la evaluación.
3. Revisar los resultados y las verificaciones disponibles.
4. Comprobar que el reporte JSON se haya generado en la carpeta `reports/`.

Para la Semana 14, el notebook incluye una sección de autoverificación que comprueba la integridad de las particiones, la configuración de PCA, las métricas de clasificación, los costos empresariales y los resultados de la prueba KS.

### 6. Reproducibilidad

Los experimentos utilizan los siguientes parámetros:

| Parámetro | Valor |
|---|---|
| ID del estudiante | 19 |
| Semilla | 1019 |
| Tamaño de muestra | 35.000 pedidos |
| Entrenamiento | 24.500 pedidos |
| Validación | 5.250 pedidos |
| Prueba | 5.250 pedidos |

Los modelos se entrenan utilizando el conjunto de entrenamiento y se comparan mediante el conjunto de validación.

El conjunto de prueba permanece reservado para una evaluación independiente posterior.

Los datos originales y las muestras completas no se incluyen en el repositorio.