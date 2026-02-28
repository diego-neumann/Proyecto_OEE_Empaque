import pandas as pd
import numpy as np

# Cargar los datos
df = pd.read_csv('c:/Users/Diego/OneDrive/GitHub/Proyecto_OEE_Empaque/datos/raw_data.csv')

# Filtrar a solo las máquinas
# df_machines = ... actually all are machines.
print("Total rows:", len(df))

# Convert elapsed from generic units? Let's check max elapsed
print("Elapsed max:", df['elapsed'].max())
print("Elapsed mean:", df['elapsed'].mean())

# Calcular tiempo total, planeado y operativo
# Tiempos en 'elapsed' parecen ser milisegundos dado el log. (Ej. 63050. Wait, 63050 ms = 63 segundos = 1 minuto. So yes, ms)
agrupado = df.groupby(['equipment_ID', 'type'])['elapsed'].sum().unstack(fill_value=0)

print("\n--- Agrupado por Tipo (en horas) ---")
agrupado_hrs = agrupado / 1000 / 3600
print(agrupado_hrs)

# Disponibilidad
total_time = agrupado.sum(axis=1)
scheduled_downtime = agrupado.get('scheduled_downtime', 0)
planned_production_time = total_time - scheduled_downtime

# Operating time = production + performance_loss ? O solo production?
operating_time = agrupado.get('production', 0) + agrupado.get('performance_loss', 0)

availability = operating_time / planned_production_time
print("\n--- Availability ---")
print(availability)

# Rendimiento (Performance)
# Necesitamos total_units_produced. 
# pi is cumulative? Let's just do max(pi) - min(pi)
total_pi = df.groupby('equipment_ID')['pi'].max() - df.groupby('equipment_ID')['pi'].min()

# El Ideal Cycle Time (ICT) es 1 / speed. 
# Si speed es unidades / hora, entonces ICT en horas es 1/speed.
# Speed varies per row?
mean_speed = df[df['speed'] > 0].groupby('equipment_ID')['speed'].mean()
print("\n--- Mean Speed (units/hr) ---")
print(mean_speed)

# Expected units = operating_time (hours) * speed (units/hr)
# Operating time in hours:
operating_time_hrs = operating_time / 1000 / 3600

# Usamos la velocidad promedio máxima o la moda de velocidad para la máquina
max_speed = df[df['speed'] > 0].groupby('equipment_ID')['speed'].max()

expected_units = operating_time_hrs * max_speed

performance = total_pi / expected_units

print("\n--- Performance ---")
print(performance)

# Calidad (Quality)
total_po = df.groupby('equipment_ID')['po'].max() - df.groupby('equipment_ID')['po'].min()

quality = total_po / total_pi

print("\n--- Quality ---")
print(quality)

# OEE Final
oee = availability * performance * quality
print("\n--- OEE ---")
print(oee)

# Componentes en dataframe
oee_df = pd.DataFrame({
    'Availability': availability,
    'Performance': performance,
    'Quality': quality,
    'OEE': oee
})

print("\n=== FINAL OEE TABLE ===")
print(oee_df)
