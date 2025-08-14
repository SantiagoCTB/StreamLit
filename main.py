import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

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
st.title("Análisis Exploratorio de Datos")

st.subheader("Vista previa de los datos")
st.write(df.head())

st.subheader("Información general")
buffer = []
df.info(buf=buffer)
info_str = "\n".join(buffer)
st.text(info_str)

st.subheader("Estadísticas descriptivas")
st.write(df.describe())

st.subheader("Conteo por categoría")
st.write(df["Categoria"].value_counts())

st.subheader("Valores nulos")
st.write(df.isnull().sum())

# -------------------------------
# 3. Visualización - Gráfico de Barras
# -------------------------------
st.subheader("Cantidad de registros por categoría")
conteo_cat = df["Categoria"].value_counts()
fig1, ax1 = plt.subplots(figsize=(6,4))
conteo_cat.plot(kind="bar", color="skyblue", edgecolor="black", ax=ax1)
ax1.set_title("Cantidad de registros por categoría")
ax1.set_xlabel("Categoría")
ax1.set_ylabel("Frecuencia")
st.pyplot(fig1)

# -------------------------------
# 4. Visualización - Gráfico de Líneas
# -------------------------------
st.subheader("Evolución de Valor en el tiempo")
fig2, ax2 = plt.subplots(figsize=(8,5))
ax2.plot(df["Fecha"], df["Valor"], marker="o", linestyle="-", color="orange")
ax2.set_title("Evolución de Valor en el tiempo")
ax2.set_xlabel("Fecha")
ax2.set_ylabel("Valor")
ax2.grid(True)
st.pyplot(fig2)