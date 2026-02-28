# Análisis de Efectividad Global de Equipos (OEE) en la Industria del Empaque

Este proyecto es un caso de estudio práctico desarrollado para el **Certificado de Análisis de Datos de Google**. Siguiendo las directrices del currículo para documentar el caso, a continuación se presentan los entregables requeridos sobre el análisis elaborado.

## 1. Tarea Empresarial (Business Task)
El objetivo principal de este análisis es procesar un conjunto de datos reales de telemetría industrial de máquinas empacadoras para identificar las causas principales de tiempo de inactividad (downtime) y calcular la **Disponibilidad** general de los equipos. La meta final es proporcionar información respaldada por datos que permita a los gerentes de operaciones reducir ineficiencias, priorizar mantenimientos y asentar las bases para la medición del indicador mundial operativo OEE (Overall Equipment Effectiveness).

## 2. Fuentes de Datos
Se utilizó el "Packaging Industry Anomaly Detection Dataset" obtenido de fuente pública en [Kaggle](https://www.kaggle.com/datasets/orvile/packaging-industry-anomaly-detection-dataset).
Este conjunto contiene registros exhaustivos y minute-by-minute sobre el estado operativo, pausas y fallas de 5 máquinas empacadoras a lo largo de un periodo de trabajo productivo. El análisis se concentró fundamentalmente en el archivo principal `raw_data.csv`.

## 3. Limpieza y Manipulación de Datos
La limpieza y el procesamiento de los datos se llevaron a cabo paso a paso usando el entorno **Jupyter Notebook** (`notebooks/01_exploracion_y_limpieza.ipynb`) y haciendo uso de bibliotecas de Python como `pandas`, `matplotlib` y `seaborn`.

Los principales pasos llevados a cabo fueron:
* Verificación de valores nulos e información de las estructuras de datos (EDA Inicial).
* Transformación de valores temporales, como la columna `interval_start`, cambiada al tipo `datetime` de pandas para permitir un análisis agrupado por fechas para las series de tiempo.
* Filtrado del DataFrame original separando periodos regulares de operación (`production`) frente a inactividad o fallos.
* Creación de un diccionario para renombrar los IDs de los equipos (p. ej., transformar 's_1' en 'Máquina 1') y facilitar la lectura en los gráficos.

## 4. Resumen del Análisis
El análisis de los datos se enfocó en comprender profundamente cómo se pierde el tiempo a nivel general en la planta, identificando los obstáculos más importantes que detienen la producción. Para ello:
1. Calculamos la **Disponibilidad General de la Planta**, que representa el tiempo trabajando frente al tiempo total disponible.
2. Agrupamos los lapsos de inactividad por el tipo específico de detención a fin de aplicar el "Principio de Pareto" y visualizar si una pequeña cantidad de problemas causan la mayoría de los tiempos perdidos.
3. Comparamos el trabajo y producción bruta de cada una de las 5 máquinas.
4. Sumamos las horas de producción efectivas día con día para crear una visualización temporal sobre el ritmo productivo.
5. Formulamos el cálculo del **OEE (Efectividad Global del Equipo)** integrando Rendimiento (desempeño de velocidad de la máquina) y Calidad (porcentaje de piezas buenas `po` sobre el total `pi`).

## 5. Visualizaciones y Hallazgos Clave
Las librerías visuales demostraron tres hechos principales:
* La principal causa de interrupción de las máquinas es el estado de **"Inactividad no justificada (Idle)"**, responsable de un abrumador **41.49%** de las paradas. Le sigue el **"Mantenimiento Planeado"** (26.41%) y la **"Pérdida de Rendimiento"** (19.37%). ([Ver Gráfico de Pareto](visualizaciones/pareto_downtime.png)).
* Al observar el desempeño individual, la máquina con el mayor volumen de producción acumulado constante ha sido la **Máquina 2**. ([Ver Gráfico Producción](visualizaciones/produccion_equipos.png)).
* Los volúmenes diarios en horas máquina fluctúan considerablemente, validado así gracias a nuestro modelado temporal de productividad. ([Ver Serie de Tiempo Temporal](visualizaciones/produccion_temporal.png)).

* Finalmente, se logró calcular el **OEE Completo** por máquina, desglosando y graficando sus 3 pilares, lo que brinda una perspectiva de las mermas productivas holística. ([Ver Gráfico OEE](visualizaciones/oee_componentes.png)).

## 6. Siguientes Pasos y Entregables Adicionales
Para complementar estos hallazgos, en fases posteriores valdría la pena expandir la indagación actual hacia áreas de analítica descriptiva avanzada o ingeniería predictiva:
* **Modelos Predictivos (Machine Learning)**: Con la data comprimida ofrecida en este repositorio (archivo `sequences_1h_data.csv`), se podría diseñar un algoritmo predictivo para alertar con antelación cuáles máquinas y a qué hora precisa podrían sufrir el próximo fallo inminente.
* **Dashboard interactivo en Tableau o Looker Studio**: Brindar este mismo resultado visual pero actualizado automáticamente a los directivos de producción en sus reportes diarios.

## 7. Conclusiones y Recomendaciones Relevantes (Top Insights)
* **Oportunidad de Mejora por "Inactividad (Idle)"**: Puesto que un 41.5% del tiempo perdido simplemente se cataloga como tiempo inactivo "idle", la planta tiene un inmenso techo de crecimiento. Se recomienda revisar urgentemente tiempos ociosos ligados a fallas logísticas o falta temprana de material de empaque, arranques fríos, cambios de personal de turno y fallas que no se catalogan apropiadamente. 
* **Evaluación de Mantenimientos**: Teniendo al "Mantenimiento Planeado" (26.4%) en la segunda posición como destructor de margen de tiempo disponible, se debe reestructurar y optimizar el calendario actual para realizar mantenimientos rutinarios sin obstaculizar masivamente las franjas más productivas.
