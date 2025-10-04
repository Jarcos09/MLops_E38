import os
from pathlib import Path
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Importar funciones personalizadas
from funciones import clean_process, impute_outliers

# Rutas relativas
base_dir = Path(__file__).resolve().parent.parent  # Asume que el script está en MLops_E38/scripts o similar

# Nombres de carpetas y archivos
nombre_carpeta = "Dataset"
nombre_dataset_original = "energy_efficiency_modified.csv"
nombre_dataset_limpio = "energy_efficiency_clean.csv"

# Construcción de rutas
ruta_dataset = base_dir / nombre_carpeta
ruta_modified = ruta_dataset / nombre_dataset_original
ruta_dataset_limpio = ruta_dataset / nombre_dataset_limpio

# Validar existencia del archivo original
if not ruta_modified.exists():
    raise FileNotFoundError(f"El archivo original no se encuentra en: {ruta_modified}")

# Cargar dataset original
df_modified = pd.read_csv(ruta_modified)

# Limpieza y procesamiento inicial
df_clean = clean_process(df_modified)

# Columnas altamente sesgadas
highly_bias_cols = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'Y1', 'Y2']

# Validar columnas esperadas
missing_cols = set(highly_bias_cols) - set(df_clean.columns)
if missing_cols:
    raise ValueError(f"Faltan columnas esperadas en el dataset limpio: {missing_cols}")

# Imputación
df_imputado = impute_outliers(df_clean, highly_bias_cols)

# Guardar el dataset imputado como limpio
df_imputado.to_csv(ruta_dataset_limpio, index=False)
print(f"Dataset limpio (imputado) guardado en: {ruta_dataset_limpio}")
