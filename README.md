# Análisis de Efectividad Global de Equipos (OEE) en la Industria del Empaque

Este proyecto es un caso de estudio práctico desarrollado para el **Certificado de Análisis de Datos de Google**. Siguiendo las directrices del Case Study 3 ("Follow your own case study path"), el análisis sigue las 6 fases del proceso de análisis de datos: **Ask, Prepare, Process, Analyze, Share y Act**.

## 1. Tarea Empresarial (Business Task) — *Ask*
El objetivo principal es analizar datos de telemetría de 5 máquinas empacadoras para calcular el **OEE (Overall Equipment Effectiveness)** de cada equipo, identificar las causas principales de tiempo perdido, y generar recomendaciones accionables para que la gerencia de operaciones pueda reducir ineficiencias y priorizar mantenimientos.

## 2. Fuentes de Datos — *Prepare*
Se utilizó el **"Packaging Industry Anomaly Detection Dataset"** obtenido de [Kaggle](https://www.kaggle.com/datasets/orvile/packaging-industry-anomaly-detection-dataset). El dataset contiene dos archivos:

| Archivo | Descripción |
|---------|-------------|
| `raw_data.csv` | Registro evento por evento del estado de cada máquina: timestamps, tipo de estado (producción, idle, downtime, etc.), duración, contadores de piezas (`pi`, `po`) y velocidad |
| `sequences_1h_data.csv` | Datos agregados por hora con porcentajes de tiempo en cada estado (`%production`, `%idle`, `%downtime`, etc.) y conteo de alarmas por tipo |

## 3. Limpieza y Manipulación de Datos — *Process*
La limpieza se realiza en el notebook `notebooks/01_exploracion_y_limpieza.ipynb` usando Python con `pandas`, `matplotlib` y `seaborn`. Los pasos documentados incluyen:
* Verificación de valores nulos, duplicados e información de las estructuras de datos (EDA Inicial).
* Conversión de `interval_start` a formato `datetime` para análisis temporal.
* Estandarización de nombres: traducción de estados y renombrado de equipos (ej. `s_1` → `Máquina 1`).
* Validación de valores numéricos (no negativos en `elapsed`, `pi`, `po`, `speed`).
* Exploración del archivo `sequences_1h_data.csv` con sus columnas clave.

## 4. Resumen del Análisis — *Analyze*
El análisis se desarrolla en `notebooks/02_calculo_y_graficos_oee.ipynb`:
1. **Análisis de Pareto** de tiempo no productivo para identificar las causas principales.
2. **Cálculo de OEE por máquina** desglosando Disponibilidad, Rendimiento y Calidad.
3. **Análisis temporal** de las horas de producción diarias.
4. **Comparación de producción neta** entre las 5 máquinas.

## 5. Visualizaciones y Hallazgos Clave — *Share*
* La principal causa de pérdida de tiempo es la **"Inactividad (Idle)"**, responsable de ~41% de las paradas. Le siguen el **Mantenimiento Planeado** (~26%) y la **Pérdida de Rendimiento** (~19%). ([Ver Pareto](visualizaciones/pareto_downtime.png))
* La **Calidad** es consistentemente alta (>90%) en todas las máquinas, pero la **Disponibilidad** es el cuello de botella del OEE. ([Ver OEE](visualizaciones/oee_componentes.png))
* La producción diaria presenta alta variabilidad, sugiriendo irregularidades operativas. ([Ver Serie Temporal](visualizaciones/produccion_temporal.png))
* La máquina con mayor volumen de producción acumulado es la **Máquina 2**. ([Ver Producción](visualizaciones/produccion_equipos.png))

## 6. Conclusiones y Recomendaciones — *Act*
| # | Recomendación | Impacto |
|---|--------------|---------|
| 1 | **Investigar y subcategorizar el tiempo "Idle"** (espera material, cambio turno, sin clasificar) | Alto — 41% de pérdidas |
| 2 | **Optimizar calendario de mantenimiento** preventivo a horarios de menor demanda | Medio — 26% de paradas |
| 3 | **Monitorear patrones temporales** para detectar días de baja producción recurrente | Medio |

### Próximos pasos
* **Dashboard interactivo** en Looker Studio o Tableau para monitoreo continuo.
* **Análisis predictivo** con `sequences_1h_data.csv` para anticipar fallos.
* **Estandarizar registro de paradas** mejorando la categorización de eventos "idle".
