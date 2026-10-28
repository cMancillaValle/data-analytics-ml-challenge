# Resultados - Semana 12

## Resumen del Desafío

- **ID asignado:** `19`
- **Semilla de partición (`semilla`):** `1019`
- **Tamaño de muestra (`n_muestra`):** `35.000` pedidos (24.500 entrenamiento, 5.250 validación, 5.250 prueba)
- **Variables predictoras:** 28 (24 numéricas y 4 categóricas)
- **Tasa de entregas tardías en la muestra:** 6,8 %
- **Modelo oficial:** Regresión Logística con `class_weight='balanced'` y `max_iter=1000`
- **Penalización de costos:** **R$ 8** (Falso Positivo) vs. **R$ 35** (Falso Negativo)
- **Regresión (Ridge):** MAE = **5.21 días**

## Métricas en validación

| Modelo | Accuracy | Precision | Recall | F1 | ROC-AUC | AP | Costo (R$) |
|---|---|---|---|---|---|---|---|
| Referencia (Dummy) | 0.9324 | 0.0000 | 0.0000 | 0.0000 | 0.5000 | 0.0676 | 12.425 |
| Regresión Logística, `class_weight=None` | 0.9324 | 0.0000 | 0.0000 | 0.0000 | 0.6913 | 0.1459 | 12.425 |
| Regresión Logística, `class_weight='balanced'` | 0.6547 | 0.1183 | 0.6366 | 0.1996 | 0.6925 | 0.1402 | 17.987 |

Matriz de confusión del modelo oficial: 3.211 verdaderos negativos, 1.684 falsos positivos, 129 falsos negativos y 226 verdaderos positivos.

## Respuestas del Desafío

### ¿Qué pedidos llegarán tarde?

El modelo (**Regresión Logística**) estima la probabilidad de que un pedido llegue después de la fecha estimada de entrega y lo marca como tardío con el umbral por defecto de 0.5. En validación detecta 226 de los 355 pedidos realmente tardíos (Recall 0.637), pero emite 1.910 alertas, de las cuales solo 226 son correctas (Precision 0.118). Su capacidad de ordenar los pedidos por riesgo es moderada: ROC-AUC de 0.693 y AP de 0.140, aproximadamente el doble de la prevalencia de retrasos (0.068).

Los errores no se distribuyen de forma uniforme:

- **Por estado del cliente:** São Paulo tiene 18,4 % de error, mientras que RJ (65,5 %), BA (73,1 %), SC (62,1 %) y ES (57,4 %) presentan tasas mucho mayores. RJ, BA y SC reúnen el 20,3 % de los pedidos y el 38,9 % de los errores.
- **Por mes de compra:** el error es más alto en agosto (49,0 %) y marzo (44,2 %), y más bajo en diciembre (15,1 %).

Este análisis muestra dónde se concentran los errores, pero no identifica los factores que causan los retrasos: el notebook no mide la importancia de las variables ni separa falsos positivos y falsos negativos por segmento.

### ¿Cuánto cuesta equivocarse?

Con los costos del ejercicio (valores ilustrativos, no costos reales de Olist), el modelo oficial tiene un costo de **R$ 17.987**: R$ 13.472 por 1.684 falsos positivos y R$ 4.515 por 129 falsos negativos. Un sistema que nunca alerta costaría 355 × R$ 35 = R$ 12.425, menos que el modelo, porque con el umbral de 0.5 se generan demasiadas falsas alarmas.

Se eligió `class_weight='balanced'` por su capacidad de detección: sin ponderar, el modelo no predice ningún retraso y se comporta igual que la referencia.

### Mejora propuesta para la semana 13

- Elegir el umbral de decisión minimizando 8 × FP + 35 × FN sobre las probabilidades de validación, en lugar de usar 0.5.
- Agregar una variable de ruta (estado del vendedor y del cliente) o una tasa histórica de retraso por estado calculada solo con los datos de entrenamiento.
- Verificar con la misma muestra y la misma partición de validación, sin usar el conjunto de prueba.

## Entregable Generado

- **Ruta de salida:** `reports/S12_resultados_ID_19.json`