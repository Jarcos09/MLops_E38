import numpy as np
import pandas as pd
from scipy.stats import skew

def clean_process(df):
    """
    Proceso de limpieza de datos:

    1. Unificación de valores no válidos:
       - Reemplaza cadenas de texto no numéricas, vacías o con espacios en blanco por NaN.

    2. Conversión de tipos:
       - Convierte todas las columnas a tipo numérico (float).
       - Valores que no puedan transformarse también se marcan como NaN.

    Parámetros:
        df (pd.DataFrame): DataFrame de entrada.

    Retorno:
        pd.DataFrame: DataFrame limpio, numérico y con NaN donde haya valores inválidos.
    """

    # 1) Duplicamos el DataFrame
    df_copy = df.copy()

    # 2) Reemplazamos strings vacíos o con espacios por NaN
    df_copy.replace(r'^\s*$', np.nan, regex=True, inplace=True)

    # 3) Forzamos conversión de todas las columnas a numérico
    df_clean = df_copy.apply(pd.to_numeric, errors='coerce')

    return df_clean

def impute_missing_values(df):
    """
    Imputa automáticamente los valores faltantes en un DataFrame numérico
    basándose en la distribución de cada columna:
        - Media para distribuciones aproximadamente simétricas.
        - Mediana para distribuciones sesgadas.

    Parámetros:
        df (pd.DataFrame): DataFrame de entrada con valores faltantes.

    Retorno:
        pd.DataFrame: Copia del DataFrame con valores imputados.
    """

    # Crear copia para no modificar el original
    df_imputed = df.copy()

    for col in df_imputed.columns:
        # Calcular asimetría
        col_skew = skew(df_imputed[col].dropna())

        # Decidir estrategia
        if -0.5 <= col_skew <= 0.5:
            # Aproximadamente simétrica → media
            df_imputed[col] = df_imputed[col].fillna(df_imputed[col].mean())
        else:
            # Altamente sesgada → mediana
            df_imputed[col] = df_imputed[col].fillna(df_imputed[col].median())

    return df_imputed

def impute_outliers(df):
    """
    Aplica imputación por Capping (percentil 99) para tratar outliers
    en todas las columnas numéricas de un DataFrame.

    Parámetros:
        df (pd.DataFrame): DataFrame de entrada.

    Retorno:
        pd.DataFrame: DataFrame transformado (con outliers capados).
    """
    df_transformed = df.copy()

    # Iterar solo sobre columnas numéricas
    num_cols = df_transformed.select_dtypes(include=[np.number]).columns

    for col in num_cols:
        # Calcular percentil 99
        p99 = df_transformed[col].quantile(0.99)

        # Aplicar Capping
        df_transformed[col] = np.where(df_transformed[col] > p99, p99, df_transformed[col])

    return df_transformed