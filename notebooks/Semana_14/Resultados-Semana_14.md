# Resultados - Semana 14

## Resumen del Desafío

- **ID asignado:** `19`
- **Semilla de partición (`semilla`):** `1019`
- **Tamaño de muestra (`n_muestra`):** `35.000` pedidos (24.500 entrenamiento, 5.250 validación, 5.250 prueba)
- **Variables predictoras:** 28 (24 numéricas y 4 categóricas)
- **Tasa de entregas tardías en la muestra:** aproximadamente 6,8 %
- **Algoritmo de clasificación:** Regresión Logística con `class_weight='balanced'` y `max_iter=2000`
- **Configuraciones evaluadas:** cuatro modelos (A, B, C y D)
- **Umbral de clasificación:** `0.50`
- **Penalización de costos:** 8 BRL (Falso Positivo) y 35 BRL (Falso Negativo)
- **Reducción dimensional:** PCA con al menos 90 % de varianza explicada
- **Prueba estadística:** Kolmogorov-Smirnov de dos muestras sobre `valor_flete`

## Actividad 1 - Reducción de dimensionalidad mediante PCA

Se aplicó Análisis de Componentes Principales (PCA) sobre las 24 variables numéricas, después de completar los valores faltantes mediante la mediana y estandarizar las variables con `StandardScaler`.

El número de componentes se seleccionó automáticamente mediante `PCA(n_components=0.90, svd_solver='full')`, utilizando exclusivamente los datos de entrenamiento.

### Resultados de PCA

| Indicador | Resultado |
|---|---:|
| Variables numéricas originales | 24 |
| Componentes principales seleccionados | 15 |
| Dimensiones eliminadas | 9 |
| Reducción de dimensionalidad | 37.50 % |
| Varianza explicada acumulada | 90.62 % |

La curva de varianza explicada acumulada confirmó que el umbral del 90 % se alcanza con 15 componentes principales. Los componentes adicionales aportan incrementos progresivamente menores hasta aproximarse al 100 % de la varianza.

Aunque PCA permitió reducir la dimensionalidad, conservar la mayor parte de la varianza no garantiza preservar toda la información necesaria para predecir entregas tardías. Por ello, su utilidad se evaluó mediante la comparación de modelos de clasificación.

Las variables categóricas conservaron su preprocesamiento mediante imputación por categoría más frecuente y One-Hot Encoding, sin aplicar PCA sobre ellas.

## Actividad 2 - Comparación de modelos de clasificación

Se entrenaron cuatro configuraciones de regresión logística, variando la aplicación de PCA y la intensidad de regularización mediante el parámetro `C`.

| Modelo | PCA | C | Regularización |
|---|---|---:|---|
| A | No | 1.0 | Intermedia |
| B | Sí | 1.0 | Intermedia |
| C | Sí | 0.1 | Mayor |
| D | Sí | 10.0 | Menor |

Todos los modelos utilizaron `class_weight='balanced'`, `max_iter=2000`, `random_state=1019` y un umbral de clasificación de 0.50.

### Métricas en validación

| Modelo | Accuracy | Precision | Recall | F1 | AP | Costo (BRL) |
|---|---:|---:|---:|---:|---:|---:|
| A | 0.6547 | 0.1183 | 0.6366 | 0.1996 | 0.1402 | 17.987 |
| B | 0.6493 | 0.1110 | 0.5972 | 0.1872 | 0.1130 | 18.589 |
| C | 0.6484 | 0.1095 | 0.5887 | 0.1846 | 0.1138 | 18.710 |
| D | 0.6482 | 0.1111 | 0.6000 | 0.1874 | 0.1122 | 18.610 |

El modelo A, sin PCA y con `C=1.0`, obtuvo los mejores resultados en todas las métricas evaluadas.

Al comparar los modelos A y B, que utilizan el mismo valor de regularización, se observa que la incorporación de PCA redujo el Recall de 0.6366 a 0.5972, el F1 de 0.1996 a 0.1872 y el AP de 0.1402 a 0.1130.

Esto sugiere que la representación reducida mediante PCA no conservó completamente la información predictiva disponible en las variables originales.

Los cambios en la intensidad de regularización de los modelos B, C y D produjeron diferencias pequeñas y no permitieron superar al modelo A.

### ¿Qué pedidos llegarán tarde?

El modelo A estima la probabilidad de que un pedido llegue después de su fecha prevista de entrega y lo clasifica como tardío utilizando el umbral de 0.50.

En el conjunto de validación identificó correctamente 226 de los 355 pedidos realmente tardíos, alcanzando un Recall de aproximadamente 63.66 %.

Sin embargo, generó 1.910 alertas, de las cuales únicamente 226 fueron correctas. Esto corresponde a una Precision de aproximadamente 11.83 %.

Su AP de 0.1402 indica una capacidad de ordenamiento superior a la prevalencia de entregas tardías en validación, aunque todavía limitada para una aplicación empresarial directa.

Por tanto, el modelo A representa la mejor configuración predictiva entre las cuatro alternativas evaluadas, pero mantiene una cantidad elevada de falsas alertas.

### ¿Cuánto cuesta equivocarse?

Se utilizaron penalizaciones ilustrativas de 8 BRL por falso positivo y 35 BRL por falso negativo.

El costo total se calculó mediante:

**Costo total = 8 × FP + 35 × FN**

| Modelo | FP | FN | Costo FP (BRL) | Costo FN (BRL) | Costo total (BRL) |
|---|---:|---:|---:|---:|---:|
| A | 1.684 | 129 | 13.472 | 4.515 | 17.987 |
| B | 1.698 | 143 | 13.584 | 5.005 | 18.589 |
| C | 1.700 | 146 | 13.600 | 5.110 | 18.710 |
| D | 1.705 | 142 | 13.640 | 4.970 | 18.610 |

El modelo A presentó el menor costo entre las cuatro configuraciones, con 17.987 BRL.

Sin embargo, una estrategia que nunca emite alertas tendría un costo de 12.425 BRL, correspondiente a los 355 pedidos tardíos multiplicados por la penalización de 35 BRL.

| Estrategia | Costo (BRL) | Diferencia frente a no alertar (BRL) |
|---|---:|---:|
| Sin alertas | 12.425 | 0 |
| Modelo A | 17.987 | +5.562 |
| Modelo B | 18.589 | +6.164 |
| Modelo C | 18.710 | +6.285 |
| Modelo D | 18.610 | +6.185 |

Ninguno de los modelos logró reducir el costo empresarial frente a la estrategia sin alertas.

Aunque el modelo A ofrece la mejor combinación de métricas entre las configuraciones estudiadas, todavía no constituye una alternativa económicamente favorable bajo el umbral y las penalizaciones establecidos.

Los costos son exclusivamente ilustrativos y no corresponden a gastos reales registrados por Olist.

## Actividad 3 - Prueba de Kolmogorov-Smirnov

Se aplicó la prueba de Kolmogorov-Smirnov (KS) de dos muestras para comparar la distribución de `valor_flete` entre los conjuntos de entrenamiento y validación.

### Hipótesis estadísticas

- **H₀:** Las observaciones de `valor_flete` de entrenamiento y validación proceden de la misma distribución.
- **H₁:** Las observaciones de `valor_flete` de entrenamiento y validación proceden de distribuciones diferentes.

### Resultados

| Indicador | Resultado |
|---|---:|
| Variable analizada | `valor_flete` |
| Estadístico KS (D) | 0.0092 |
| Valor p | 0.852027 |
| Nivel de significancia | 0.05 |
| Decisión estadística | No rechazar H₀ |

El estadístico D indica una diferencia máxima aproximada de 0.92 puntos porcentuales entre las distribuciones acumuladas empíricas.

Como el valor p es superior a 0.05, no se rechaza la hipótesis nula.

En consecuencia, no se encontró evidencia estadísticamente significativa de diferencias entre las distribuciones de `valor_flete` en entrenamiento y validación.

Este resultado es compatible con una distribución similar de dicha variable en ambas particiones. Sin embargo, no demuestra que las distribuciones sean idénticas ni garantiza estabilidad en las demás variables o en el rendimiento futuro del modelo.

## Conclusiones del Desafío

Los resultados de la Semana 14 permiten establecer cuatro conclusiones principales:

1. **PCA redujo la dimensionalidad numérica:** se pasó de 24 variables a 15 componentes principales, conservando el 90.62 % de la varianza acumulada.

2. **La reducción dimensional no mejoró la clasificación:** el modelo A, sin PCA, obtuvo mejores métricas que las tres configuraciones con PCA.

3. **La regularización no compensó la pérdida de rendimiento:** los valores de `C` evaluados produjeron diferencias pequeñas y ninguno permitió superar al modelo A.

4. **El costo empresarial continúa siendo elevado:** aunque el modelo A fue el mejor de los cuatro, su costo de 17.987 BRL superó los 12.425 BRL de la estrategia sin alertas.

Adicionalmente, la prueba KS no encontró evidencia estadísticamente significativa de diferencias en la distribución de `valor_flete` entre entrenamiento y validación.

En conjunto, estos hallazgos muestran que conservar una proporción elevada de varianza mediante PCA no implica necesariamente mejorar el rendimiento predictivo o disminuir el costo de los errores.

## Mejoras propuestas

Como continuación del experimento, se plantean dos líneas de trabajo:

- **Incorporación de información geográfica:** construir una variable de ruta combinando el estado del vendedor y el estado del cliente para representar diferencias logísticas entre trayectos.
- **Optimización del umbral de clasificación:** evaluar distintos umbrales sobre las probabilidades de validación para minimizar el costo de falsos positivos y falsos negativos.

Estas mejoras deberán evaluarse utilizando la misma muestra y las mismas particiones, sin utilizar el conjunto de prueba durante la selección de configuraciones.

## Reproducibilidad y autoverificación

El experimento utiliza la semilla `1019` y conserva las particiones de entrenamiento, validación y prueba establecidas para el ID 19.

El notebook incluye verificaciones automáticas para comprobar:

- Los tamaños de la muestra y de las particiones.
- La ausencia de pedidos compartidos entre particiones.
- El número de componentes y la varianza explicada por PCA.
- La existencia de los cuatro modelos y la consistencia de sus métricas.
- El cálculo de los costos empresariales.
- Los rangos válidos del estadístico KS y su valor p.

La ejecución completa del notebook finalizó correctamente y la autoverificación fue superada.

El conjunto de prueba permanece reservado para una evaluación independiente posterior.

## Entregables Generados

- **Notebook:** `notebooks/Semana_14/S14_ML_Challenge.ipynb`
- **Reporte estructurado:** `reports/S14_resultados_ID_19.json`
- **Resumen de resultados:** `reports/S14_resultados.md`

El archivo JSON registra los parámetros de reproducibilidad, las versiones de las principales dependencias, la composición de la muestra, los resultados de PCA, las métricas de los cuatro modelos y los resultados de la prueba KS.
