import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# 1. Generar datos aleatorios
# -------------------------------
np.random.seed(42)  # Para reproducibilidad
fechas = pd.date_range(start="2025-01-01", periods=10, freq="D")
categorias = ["A", "B", "C"]

df = pd.DataFrame({
    "Fecha": fechas,
    "Categoria": np.random.choice(categorias, size=10),
    "Valor": np.random.randint(10, 100, size=10)
})

# -------------------------------
# 2. Análisis exploratorio básico
# -------------------------------
print("=== Vista previa de los datos ===")
print(df.head())

print("\n=== Información general ===")
print(df.info())

print("\n=== Estadísticas descriptivas ===")
print(df.describe())

print("\n=== Conteo por categoría ===")
print(df["Categoria"].value_counts())

print("\n=== Valores nulos ===")
print(df.isnull().sum())

# -------------------------------
# 3. Visualización - Gráfico de Barras
# -------------------------------
conteo_cat = df["Categoria"].value_counts()

plt.figure(figsize=(6,4))
conteo_cat.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Cantidad de registros por categoría")
plt.xlabel("Categoría")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()

# -------------------------------
# 4. Visualización - Gráfico de Líneas
# -------------------------------
plt.figure(figsize=(8,5))
plt.plot(df["Fecha"], df["Valor"], marker="o", linestyle="-", color="orange")
plt.title("Evolución de Valor en el tiempo")
plt.xlabel("Fecha")
plt.ylabel("Valor")
plt.grid(True)
plt.tight_layout()
plt.show()
