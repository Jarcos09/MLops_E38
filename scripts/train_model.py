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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preprocesamiento y entrenamiento de modelo RandomForest multi-output.")
    parser.add_argument("csv_path", help="Ruta al archivo CSV con los datos.")
    args = parser.parse_args()

    df = pd.read_csv(args.csv_path)
    X_train, X_test, y_train, y_test = preprocess_features_and_split(df)
