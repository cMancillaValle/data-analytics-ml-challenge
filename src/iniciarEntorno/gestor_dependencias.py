"""
Módulo src.iniciarEntorno.gestor_dependencias

Verifica e instala automáticamente los paquetes listados en requirements.txt
garantizando la compatibilidad del entorno local y Colab.
"""

import sys
import subprocess
from pathlib import Path


def preparar_entorno():
    # Detecta la raíz del proyecto subiendo dos niveles desde src/iniciarEntorno
    raiz = Path(__file__).resolve().parent.parent.parent
    requirements_path = raiz / 'requirements.txt'

    print(f"    [Iniciando Entorno] Raíz detectada: {raiz}")

    if not requirements_path.exists():
        print(f"Advertencia: No se encontró {requirements_path}")
        return

    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", str(requirements_path)]
        )
        print("    [Entorno Listo] Todas las dependencias están al día")
    except subprocess.CalledProcessError as err:
        print(f"Error durante la instalación de dependencias: {err}")