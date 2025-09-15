# ============================================
# Titanic - EDA + Limpieza + Modelado (completo)
# ============================================

# 1) Importar librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix, roc_auc_score, RocCurveDisplay
)

pd.set_option("display.max_columns", None)

# 2) Cargar dataset
titanic_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(titanic_url)
print("--- Dataset Titanic cargado ---")
print(df.head())

# 3) LIMPIEZA DE DATOS ----------------------------------------------
print("\n--- 2. Limpieza de Datos ---")

# Valores perdidos (reporte inicial)
print("\nCantidad de valores perdidos por columna:")
print(df.isnull().sum())

# (Opcional) Visualización de nulos
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Mapa de Calor de Valores Perdidos")
plt.tight_layout()
plt.show()

# 3.1 Eliminar 'Cabin' por alto % de nulos
if "Cabin" in df.columns:
    print("\nEliminando 'Cabin' por alto porcentaje de nulos...")
    df = df.drop(columns=["Cabin"])

# 3.2 Imputación de 'Age' con mediana
print("Imputando 'Age' con la mediana...")
df["Age"] = df["Age"].fillna(df["Age"].median())

# 3.3 Imputación de 'Embarked' con la moda
print("Imputando 'Embarked' con la moda...")
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# 3.4 Eliminar columnas irrelevantes
for col in ["PassengerId", "Name", "Ticket"]:  # Ticket causa el error string→float
    if col in df.columns:
        print(f"Eliminando columna irrelevante: {col}")
        df = df.drop(columns=[col])

# 3.5 Convertir 'Sex' a numérico
print("Convirtiendo 'Sex' a valores numéricos (0=female, 1=male)...")
df["Sex"] = df["Sex"].map({"female": 0, "male": 1}).astype(int)

# 3.6 One-Hot Encoding de 'Embarked'
print("Aplicando One-Hot Encoding a 'Embarked'...")
df = pd.get_dummies(df, columns=["Embarked"], prefix="Embarked", drop_first=True)

# Verificar nulos post-limpieza
print("\nCantidad de valores perdidos después de la limpieza:")
print(df.isnull().sum())

print("\nDataFrame limpio (primeras filas):")
print(df.head())

# 4) ESTADÍSTICAS RELEVANTES ----------------------------------------
print("\n--- 3. Estadísticas Relevantes ---")
print("\nEstadísticas descriptivas del DataFrame limpio:")
print(df.describe())

print("\nDistribución de la variable 'Survived' (conteo):")
print(df["Survived"].value_counts())
print("\nDistribución de la variable 'Survived' (proporción):")
print(df["Survived"].value_counts(normalize=True))

print("\nTasa de supervivencia por género (0=female, 1=male):")
print(df.groupby("Sex")["Survived"].mean())

print("\nTasa de supervivencia por clase de pasajero:")
print(df.groupby("Pclass")["Survived"].mean())

print("\nDistribución de la edad:")
print(df["Age"].describe())

# 5) MATRIZ DE CORRELACIÓN -------------------------------------------
print("\n--- 4. Matriz de Variables Correlacionadas ---")
numeric_df = df.select_dtypes(include="number")
corr = numeric_df.corr()
print("\nMatriz de Correlación (vista parcial):")
print(corr.head())

plt.figure(figsize=(12, 10))
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5, square=True)
plt.title("Matriz de Correlación de Variables")
plt.tight_layout()
plt.show()

# 6) GRÁFICAS (EDA) --------------------------------------------------
print("\n--- 5. Gráficas con Matplotlib y Seaborn ---")

# 6.1 Histograma + KDE de Age
plt.figure(figsize=(10, 6))
sns.histplot(df["Age"], kde=True, bins=30)
plt.title("Distribución de la Edad de los Pasajeros")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()

# 6.2 Supervivencia por género
plt.figure(figsize=(7, 5))
sns.barplot(x="Sex", y="Survived", data=df, errorbar=None)
plt.title("Tasa de Supervivencia por Género")
plt.xlabel("Género (0=Femenino, 1=Masculino)")
plt.ylabel("Tasa de Supervivencia")
plt.xticks([0, 1], ["Femenino", "Masculino"])
plt.tight_layout()
plt.show()

# 6.3 Supervivencia por clase
plt.figure(figsize=(7, 5))
sns.barplot(x="Pclass", y="Survived", data=df, errorbar=None)
plt.title("Tasa de Supervivencia por Clase de Pasajero")
plt.xlabel("Clase de Pasajero")
plt.ylabel("Tasa de Supervivencia")
plt.tight_layout()
plt.show()

# 6.4 Supervivencia por puerto (si existen columnas)
if {"Embarked_Q", "Embarked_S"}.issubset(df.columns):
    mask_C = (df["Embarked_Q"] == 0) & (df["Embarked_S"] == 0)
    mask_Q = df["Embarked_Q"] == 1
    mask_S = df["Embarked_S"] == 1

    embarked_survival = pd.DataFrame({
        "Port": ["C", "Q", "S"],
        "Survived_Rate": [
            df.loc[mask_C, "Survived"].mean(),
            df.loc[mask_Q, "Survived"].mean(),
            df.loc[mask_S, "Survived"].mean()
        ]
    })
    plt.figure(figsize=(7, 5))
    sns.barplot(x="Port", y="Survived_Rate", data=embarked_survival, errorbar=None)
    plt.title("Tasa de Supervivencia por Puerto de Embarque")
    plt.xlabel("Puerto de Embarque")
    plt.ylabel("Tasa de Supervivencia")
    plt.tight_layout()
    plt.show()
else:
    print("\n[Aviso] No se encontraron 'Embarked_Q' y 'Embarked_S' (revisa one-hot encoding).")

# 6.5 Dispersión Age vs Fare (color por Survived)
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Age", y="Fare", hue="Survived", data=df, alpha=0.7)
plt.title("Relación entre Edad, Tarifa y Supervivencia")
plt.xlabel("Edad")
plt.ylabel("Tarifa")
plt.legend(title="Supervivencia")
plt.tight_layout()
plt.show()

# 6.6 Boxplot de Fare por Pclass
plt.figure(figsize=(10, 6))
sns.boxplot(x="Pclass", y="Fare", data=df)
plt.title("Distribución de la Tarifa por Clase de Pasajero")
plt.xlabel("Clase de Pasajero")
plt.ylabel("Tarifa")
plt.tight_layout()
plt.show()

# 7) MODELADO (split, escalado, entrenamiento, evaluación, tuning) ---
print("\n--- 6. Preparación y Modelado ---")

# X, y
y = df["Survived"]
X = df.drop(columns=["Survived"])

# Eliminar cualquier columna no numérica residual por seguridad
non_numeric = X.select_dtypes(exclude="number").columns.tolist()
if non_numeric:
    print("Eliminando columnas no numéricas:", non_numeric)
    X = X.drop(columns=non_numeric)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)
print(f"Shapes -> X_train: {X_train.shape}, X_test: {X_test.shape}")

# Pipelines
logreg_pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000))
])

rf_pipe = Pipeline([
    ("clf", RandomForestClassifier(random_state=42))
])

# Entrenar
logreg_pipe.fit(X_train, y_train)
rf_pipe.fit(X_train, y_train)

# Función de evaluación
def eval_model(name, model, X_te, y_te):
    y_pred = model.predict(X_te)
    y_prob = model.predict_proba(X_te)[:, 1] if hasattr(model, "predict_proba") else None

    print(f"\n=== {name} ===")
    print(f"Accuracy : {accuracy_score(y_te, y_pred):.3f}")
    print(f"Precision: {precision_score(y_te, y_pred):.3f}")
    print(f"Recall   : {recall_score(y_te, y_pred):.3f}")
    print(f"F1-score : {f1_score(y_te, y_pred):.3f}")
    print("\nReporte de Clasificación:\n", classification_report(y_te, y_pred, digits=3))
    print("Matriz de Confusión:\n", confusion_matrix(y_te, y_pred))
    if y_prob is not None:
        print(f"AUC-ROC  : {roc_auc_score(y_te, y_prob):.3f}")
        RocCurveDisplay.from_predictions(y_te, y_prob)
        plt.title(f"Curva ROC - {name}")
        plt.tight_layout()
        plt.show()

# Evaluación base
eval_model("Logistic Regression (base)", logreg_pipe, X_test, y_test)
eval_model("Random Forest (base)", rf_pipe, X_test, y_test)

# GridSearch breve (tuning)
logreg_grid = GridSearchCV(
    logreg_pipe,
    param_grid={
        "clf__C": [0.1, 1.0, 10.0],
        "clf__solver": ["lbfgs", "liblinear"]
    },
    scoring="f1",
    cv=5,
    n_jobs=-1
)
logreg_grid.fit(X_train, y_train)
print("\n[GridSearch] Mejor LR params:", logreg_grid.best_params_)
best_logreg = logreg_grid.best_estimator_
eval_model("Logistic Regression (tuned)", best_logreg, X_test, y_test)

rf_grid = GridSearchCV(
    rf_pipe,
    param_grid={
        "clf__n_estimators": [200, 400],
        "clf__max_depth": [None, 10, 15],
        "clf__min_samples_split": [2, 5],
        "clf__min_samples_leaf": [1, 2]
    },
    scoring="f1",
    cv=5,
    n_jobs=-1
)
rf_grid.fit(X_train, y_train)
print("[GridSearch] Mejor RF params:", rf_grid.best_params_)
best_rf = rf_grid.best_estimator_
eval_model("Random Forest (tuned)", best_rf, X_test, y_test)

print("\n✅ Pipeline completado sin columnas de texto problemáticas (p. ej., 'Ticket').")
