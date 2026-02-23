# Análisis de Efectividad Global de Equipos (OEE) y Tiempos de Inactividad

## Descripción del Proyecto
Este proyecto es un caso de estudio práctico desarrollado para el Certificado de Análisis de Datos de Google. El objetivo principal es analizar un conjunto de datos sintético de telemetría industrial para identificar las causas principales de los tiempos de inactividad (downtime) y las variaciones en el OEE a lo largo de los distintos turnos de producción. 

La intención es aplicar técnicas de análisis de datos a problemas reales de manufactura para proponer mejoras en la disponibilidad de los equipos y optimizar la gestión de los turnos rotativos.

## Origen de los Datos
Se utilizó el "Factory OEE & Downtime (Synthetic) Starter Dataset" obtenido de Kaggle ([Insertar link de Kaggle aquí]). Aunque los datos son generados de manera sintética, la estructura simula con precisión los registros de fallas y la recolección de métricas de producción en un entorno industrial.

## Herramientas Utilizadas
* **Lenguaje:** R (aprovechando librerías como `tidyverse` y `ggplot2` para la limpieza y visualización).
* **Hojas de cálculo:** Para una revisión exploratoria inicial.

## Proceso de Trabajo
1.  **Limpieza de Datos:** Tratamiento de valores nulos, estandarización de variables (como los motivos de parada) y formato de fechas/horas para el análisis por turno.
2.  **Análisis:** Cálculo del OEE promedio por máquina, identificación de cuellos de botella y aplicación de la regla de Pareto para categorizar las fallas críticas.
3.  **Visualización:** Creación de gráficos para comunicar claramente las tendencias de eficiencia y la distribución de las paradas no planificadas.

## Hallazgos Clave
* *(Aquí escribirás tu conclusión 1 cuando termines el análisis. Ejemplo: El 40% del tiempo perdido se concentra en la máquina X durante el turno noche).*
* *(Aquí escribirás tu conclusión 2).*
* *(Aquí escribirás tu conclusión 3).*

## Próximos Pasos (Recomendaciones)
* *(Ejemplo: Ajustar los planes de mantenimiento preventivo enfocándose en los componentes críticos identificados).*
* *(Ejemplo: Evaluar la distribución de carga de trabajo y capacitación técnica en los turnos con menor OEE).*