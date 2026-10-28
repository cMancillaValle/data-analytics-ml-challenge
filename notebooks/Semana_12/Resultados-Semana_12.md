# Resultados - Semana 12

## Resumen del Desafío

- **ID asignado:** `19`
- **Semilla de partición (`semilla`):** `1019`
- **Tamaño de muestra (`n_muestra`):** `35,000` registros
- **Métrica objetivo (Regresión):** MAE alcanzado = **5.21 días**
- **Métricas clave (Clasificación):**
  - `class_weight`: `'balanced'`
  - Penalización de costos: **R$ 8** (Falso Positivo) vs. **R$ 35** (Falso Negativo)

## Respuestas del Desafío

### ¿Qué pedidos llegarán tarde?

Para identificar qué pedidos llegarán con retraso, el modelo de clasificación supervisada (**Regresión Logística**) evalúa la probabilidad de que la fecha real de entrega supere la fecha estimada por la plataforma (`order_estimated_delivery_date`).

Los factores con mayor impacto y capacidad predictiva para clasificar un pedido como «con retraso» son:

1. **Distancia geográfica y logística:** los envíos entre estados con baja densidad de transporte o rutas interregionales largas presentan una probabilidad significativamente mayor de retraso.
2. **Tiempos de despacho del vendedor:** los retrasos en la entrega del paquete al operador logístico aumentan directamente el riesgo de incumplir la fecha límite estimada.
3. **Costo de flete y volumen:** los envíos con tarifas de flete atípicas o paquetes de gran volumen o peso suelen asociarse a rutas o procesos de transporte con mayor variabilidad en los tiempos de entrega.

Mediante el ajuste del umbral de decisión, considerando la matriz de costos (**R$ 8** por Falso Positivo frente a **R$ 35** por Falso Negativo), el modelo prioriza la detección temprana de estos pedidos críticos para minimizar el impacto económico en la operación.

## Entregable Generado

- **Ruta de salida:** `reports/S12_resultados_ID_19.json`