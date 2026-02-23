# Análisis de Efectividad Global de Equipos (OEE) en la Industria del Empaque

## Descripción del Proyecto
Este proyecto es un caso de estudio práctico desarrollado para el Certificado de Análisis de Datos de Google. El objetivo principal es analizar un conjunto de datos reales de telemetría industrial para identificar las causas principales de los tiempos de inactividad (downtime) y las variaciones en el OEE a lo largo de los distintos turnos de producción.

La intención es aplicar técnicas de análisis de datos a problemas reales de manufactura para proponer mejoras en la disponibilidad de los equipos y optimizar la gestión operativa.

## Origen de los Datos
Se utilizó el "Packaging Industry Anomaly Detection Dataset" obtenido de Kaggle (https://www.kaggle.com/datasets/orvile/packaging-industry-anomaly-detection-dataset). Este conjunto contiene registros exhaustivos, minuto a minuto, del estado operativo de 5 máquinas empacadoras a lo largo de un periodo extendido, permitiendo un cálculo preciso del rendimiento, disponibilidad y calidad.

## Herramientas Utilizadas
* **Lenguaje:** Python (utilizando librerías como `pandas` para la manipulación de datos y limpieza).
* **Entorno:** Jupyter Notebooks para documentar el proceso analítico paso a paso.
* **Hojas de cálculo:** Para una revisión exploratoria inicial.

## Proceso de Trabajo
1.  **Limpieza de Datos:** Tratamiento de valores nulos, estandarización de variables (como los motivos de parada) y transformación de formatos de fechas/horas (`datetime`) para el análisis por turno.
2.  **Análisis:** Cálculo del OEE promedio por máquina, identificación de cuellos de botella y aplicación de la regla de Pareto para categorizar las fallas críticas[cite: 221].
3.  **Visualización:** Creación de gráficos para comunicar claramente las tendencias de eficiencia y la distribución de las paradas no planificadas[cite: 222].

## Hallazgos Clave
* *(Pendiente de completar al finalizar el análisis)*
* *(Pendiente de completar al finalizar el análisis)*
* *(Pendiente de completar al finalizar el análisis)*

## Próximos Pasos (Recomendaciones)
* *(Ejemplo: Ajustar los planes de mantenimiento preventivo enfocándose en los componentes críticos identificados).*
* *(Ejemplo: Evaluar la distribución de carga de trabajo y capacitación técnica en los turnos con menor OEE).*