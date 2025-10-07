import os
import argparse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, PowerTransformer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error, r2_score
import xgboost as xgb

# Función de preprocesamiento
def preprocess_features_and_split(df, test_size=0.2, random_state=42):
    X = df.drop(columns=["Y1", "Y2", "mixed_type_col"])
    y = df[["Y1", "Y2"]].copy()


    cat_features = X.columns.tolist()
    for col in cat_features:
        X[col] = X[col].astype("category")


    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(drop="first", sparse_output=False, handle_unknown='ignore'), cat_features)
        ],
        remainder='drop'
    )

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    yao_transformer = PowerTransformer(method='yeo-johnson')
    yao_transformer.fit(y_train)

    y_train = pd.DataFrame(yao_transformer.transform(y_train), columns=["Y1", "Y2"], index=y_train.index)
    y_test = pd.DataFrame(yao_transformer.transform(y_test), columns=["Y1", "Y2"], index=y_test.index)


    full_pipeline = Pipeline(steps=[("preprocessor", preprocessor)])
    X_train_processed = full_pipeline.fit_transform(X_train)
    X_test_processed = full_pipeline.transform(X_test)
    
    return X_train_processed, X_test_processed, y_train, y_test

# Función de entrenamiento
def random_forest_multioutput_regression(X_train, X_test, y_train, y_test, random_state=42, param_grid=None):
    rf_base = RandomForestRegressor(random_state=random_state)
    multioutput_rf = MultiOutputRegressor(rf_base)

    if param_grid is None:
        param_grid = {
            "estimator__n_estimators": [100, 200],
            "estimator__max_depth": [8, 12, None],
            "estimator__min_samples_split": [5, 10]
        }

    grid_reg = GridSearchCV(multioutput_rf, param_grid, cv=5, scoring="neg_mean_squared_error", n_jobs=-1, verbose=1)
    grid_reg.fit(X_train, y_train.values)

    best_rf_reg = grid_reg.best_estimator_
    y_pred = best_rf_reg.predict(X_test)

    rmse_y1 = np.sqrt(mean_squared_error(y_test["Y1"], y_pred[:, 0]))
    rmse_y2 = np.sqrt(mean_squared_error(y_test["Y2"], y_pred[:, 1]))
    r2_y1 = r2_score(y_test["Y1"], y_pred[:, 0])
    r2_y2 = r2_score(y_test["Y2"], y_pred[:, 1])

    with open("metrics.txt", "w") as f:
        f.write("=== Random Forest Regressor Multi-Output ===\n")
        f.write(f"Mejores parámetros: {grid_reg.best_params_}\n")
        f.write("--- Resultados de Evaluación ---\n")
        f.write(f"Métricas para Y1:\n  RMSE: {rmse_y1:.4f}\n  R^2 Score: {r2_y1:.4f}\n")
        f.write(f"Métricas para Y2:\n  RMSE: {rmse_y2:.4f}\n  R^2 Score: {r2_y2:.4f}\n")

    return best_rf_reg, y_pred

def train_and_evaluate_xgb(X_train, X_test, y_train, y_test,best_rf_reg, random_state=42):
    """
    Entrena un modelo XGBoost Regressor Multi-Output para predecir Y1 y Y2,
    evalúa el desempeño en el conjunto de prueba y muestra métricas de rendimiento.

    Parámetros:
        X_train (array-like)  : Features de entrenamiento.
        X_test (array-like)   : Features de prueba.
        y_train (pd.DataFrame): Variables objetivo de entrenamiento (Y1 y Y2).
        y_test (pd.DataFrame) : Variables objetivo de prueba (Y1 y Y2).
        random_state (int)    : Semilla para reproducibilidad (por defecto 42).

    Retorno:
        multioutput_model (MultiOutputRegressor) : Modelo entrenado listo para predicciones futuras.
    """

    rf_params = best_rf_reg.estimator.get_params()

    # 1) Inicializar modelo XGBoost base y envoltura multi-output
    print("--- Inicializando Modelo XGBoost Multi-Output ---")
    xgb_base = xgb.XGBRegressor(
        objective='reg:squarederror',
        n_estimators=rf_params.get('n_estimators', 100),      # Número de árboles
        learning_rate=0.05,                 # Tasa de aprendizaje
        max_depth=rf_params.get('max_depth', 6),                        # Profundidad máxima
        random_state=rf_params.get('random_state', random_state),
        n_jobs=-1
    )
    multioutput_model = MultiOutputRegressor(xgb_base)

    # 2) Entrenar modelo
    print("Iniciando entrenamiento...")
    multioutput_model.fit(X_train, y_train) # Ajuste sobre conjunto de entrenamiento
    print("Entrenamiento completado.")

    # 3) Realizar predicciones sobre conjunto de prueba
    y_pred_test = multioutput_model.predict(X_test)

    # 4) Calcular métricas de error y R^2
    mse_y1 = mean_squared_error(y_test["Y1"], y_pred_test[:, 0])
    mse_y2 = mean_squared_error(y_test["Y2"], y_pred_test[:, 1])
    rmse_y1 = np.sqrt(mse_y1)
    rmse_y2 = np.sqrt(mse_y2)
    r2_y1 = r2_score(y_test["Y1"], y_pred_test[:, 0])
    r2_y2 = r2_score(y_test["Y2"], y_pred_test[:, 1])

    # 5) Mostrar resultados de evaluación
    print("\n--- Resultados de Evaluación (XGBoost) ---")
    print(f"Número de Features (después de OHE): {X_train.shape[1]}")
    print(f"Tamaño del set de prueba: {X_test.shape[0]} observaciones\n")

    print(f"Métricas para Y1 (Heating Load):")
    print(f"  RMSE (Error Cuadrático Medio): {rmse_y1:.4f}")
    print(f"  R^2 Score: {r2_y1:.4f}")

    print(f"\nMétricas para Y2 (Cooling Load):")
    print(f"  RMSE (Error Cuadrático Medio): {rmse_y2:.4f}")
    print(f"  R^2 Score: {r2_y2:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preprocesamiento y entrenamiento de modelo RandomForest multi-output.")
    parser.add_argument("csv_path", help="Ruta al archivo CSV con los datos.")
    args = parser.parse_args()

    df = pd.read_csv(args.csv_path)
    X_train, X_test, y_train, y_test = preprocess_features_and_split(df)
    best_rf_reg, y_pred = random_forest_multioutput_regression(X_train, X_test, y_train, y_test)
    train_and_evaluate_xgb(X_train, X_test, y_train, y_test,best_rf_reg)

    
