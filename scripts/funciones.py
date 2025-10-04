import numpy as np
import pandas as pd

def clean_process(df):
    #duplicamos df
    df_copy = df.copy()

    #reemplazar string por NaN
    df_copy.replace(r'^\s*$', np.nan, regex=True, inplace=True)

    #convertir a numericos
    df_num = df_copy.apply(pd.to_numeric, errors='coerce')

    #imputar los NaN a la media
    df_clean = df_num.fillna(df_num.mean())

    return df_clean


def impute_outliers(df, skew_cols):
    """
    Aplica imputación por Capping (percentil 99) y transformación logarítmica
    a columnas altamente sesgadas de un DataFrame.

    Parámetros:
        df (pd.DataFrame): DataFrame de entrada (se modifica una copia).
        skew_cols (list): Lista de nombres de columnas a transformar.

    Retorno:
        pd.DataFrame: DataFrame transformado.
    """
    df_transformed = df.copy()

    for col in skew_cols:
        if col not in df_transformed.columns:
            continue

        # Calcular percentil 99
        p99 = df_transformed[col].quantile(0.99)

        # Aplicar Capping
        df_transformed[col] = np.where(df_transformed[col] > p99, p99, df_transformed[col])

        # Aplicar Transformación Logarítmica (log(1+x) para manejar ceros)
        df_transformed[col] = np.log1p(df_transformed[col])

    return df_transformed