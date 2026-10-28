# Data Analytics and Machine Learning Challenge

> **Nota importante para Google Colab:** Si se ejecuta el cuaderno desde Google Colab, se deben omitir las instrucciones de instalación de este `README.md`. Las dependencias se gestionan directamente en la nube, y los cuadernos y entregables de cada etapa se encuentran organizados dentro de la carpeta correspondiente a cada semana.

---

## Configuración e instalación del entorno local

Para ejecutar el cuaderno en un entorno local, por ejemplo, desde VS Code, se deben seguir los siguientes pasos para configurar el entorno virtual e instalar las dependencias necesarias.

### 1. Crear el entorno virtual (`venv`)

Abrir una terminal en la raíz del proyecto (`data-analytics-ml-challenge`) y ejecutar el siguiente comando:

```bash
python -m venv venv
```

### 2. Activar el entorno virtual

El comando de activación depende del sistema operativo y de la terminal utilizada.

- **Windows (PowerShell):**

  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

  **Solución de problemas:** Si se presenta un error al activar el entorno virtual debido a las políticas de ejecución de PowerShell, ejecutar el siguiente comando en la misma terminal:

  ```powershell
  Set-ExecutionPolicy Unrestricted -Scope Process
  ```

  A continuación, volver a ejecutar el comando de activación del entorno virtual. Este cambio se aplica únicamente al proceso actual de PowerShell y deja de tener efecto al cerrar la sesión.

- **Windows (CMD):**

  ```bat
  .\venv\Scripts\activate.bat
  ```

- **Linux / macOS:**

  ```bash
  source venv/bin/activate
  ```

### 3. Seleccionar el kernel en VS Code / Jupyter

Se debe seleccionar el ejecutable de Python ubicado en `venv/` como kernel activo para el cuaderno `notebooks/Semana_12/S12_ML_Challenge.ipynb`.

### 4. Instalación de dependencias

Al ejecutar la primera celda del cuaderno, se invocará automáticamente el módulo `src/iniciarEntorno/gestor_dependencias.py`, encargado de verificar e instalar las librerías necesarias especificadas en `requirements.txt`.