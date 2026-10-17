from funciones_red import calcular_metricas, guardar_resultados
import pandas as pd

# Lectura directa del dataset
df = pd.read_excel('dataset_set_D_telecomunicaciones.xlsx')

# Llamada a la función externa
metricas = calcular_metricas(df['latencia_ms'])

# Mostrar en pantalla de forma simple y directa (sin for)
print('Resultados de latencia:', metricas)

# Guardar con Joblib
guardar_resultados(metricas, 'metricas_latencia.joblib')
