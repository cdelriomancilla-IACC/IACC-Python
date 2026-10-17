import joblib
import numpy as np
from scipy import stats


def calcular_metricas(serie_datos):
  # Conversión a arreglo NumPy y cálculos directos
  arreglo = np.array(serie_datos)
  media = np.mean(arreglo)
  desviacion = np.std(arreglo)

  # Cálculo estadístico con SciPy
  asimetria = stats.skew(arreglo)

  return {
      'promedio': round(float(media), 2),
      'desviacion': round(float(desviacion), 2),
  }


def guardar_resultados(datos, nombre_archivo):
  # Guardado directo en disco con Joblib
  joblib.dump(datos, nombre_archivo)
