import io
import numpy as np
import pandas as pd
import streamlit as st
from datetime import date, timedelta

# -------------------------------
# Configuración de la página
# -------------------------------
st.set_page_config(page_title="EDA Aleatorio • Streamlit", layout="wide")

st.title("🔎 Análisis Exploratorio de Datos (EDA) con Datos Aleatorios")
st.markdown(
    "Este mini-app genera un dataset aleatorio y muestra un análisis exploratorio básico, "
    "incluyendo dos visualizaciones: **barras** y **líneas**."
)

# -------------------------------
# Barra lateral: controles
# -------------------------------
st.sidebar.header("⚙️ Parámetros de los datos")

seed = st.sidebar.number_input("Semilla aleatoria", min_value=0, value=42, step=1)
np.random.seed(seed)

n_filas = st.sidebar.slider("Número de filas (periodos)", min_value=10, max_value=365, value=60, step=5)

fecha_inicio = st.sidebar.date_input("Fecha de inicio", value=date.today() - timedelta(days=n_filas))
categorias_pred = st.sidebar.text_input(
    "Categorías (separadas por coma)",
    value="A,B,C"
)
categorias = [c.strip() for c in categorias_pred.split(",") if c.strip()]

valor_min = st.sidebar.number_input("Valor mínimo", value=10, step=1)
valor_max = st.sidebar.number_input("Valor máximo", value=100, step=1)
if valor_max <= valor_min:
    st.sidebar.error("⚠️ El valor máximo debe ser mayor que el mínimo.")

# -------------------------------
# 1) Generar datos aleatorios
# -------------------------------
fechas = pd.date_range(start=pd.to_datetime(fecha_inicio), periods=n_filas, freq="D")
df = pd.DataFrame({
    "Fecha": fechas,
    "Categoria": np.random.choice(categorias, size=n_filas),
    "Valor": np.random.randint(valor_min, max(valor_max, valor_min + 1), size=n_filas)
})

# -------------------------------
# 2) EDA básico
# -------------------------------
st.subheader("📄 Vista previa de los datos")
st.dataframe(df.head(10), use_container_width=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Filas", df.shape[0])
with col2:
    st.metric("Columnas", df.shape[1])
with col3:
    st.metric("Categorías únicas", df["Categoria"].nunique())

# Info del DataFrame (capturando el buffer de info())
buf = io.StringIO()
df.info(buf=buf)
info_str = buf.getvalue()

with st.expander("ℹ️ Información del DataFrame (df.info())"):
    st.text(info_str)

colA, colB = st.columns(2)

with colA:
    st.markdown("**📊 Estadísticas descriptivas**")
    st.dataframe(df.describe(include="all").transpose(), use_container_width=True)

with colB:
    st.markdown("**🧩 Valores nulos por columna**")
    st.dataframe(df.isnull().sum().to_frame("n_nulos"), use_container_width=True)

st.markdown("**🔢 Conteo por categoría**")
conteo_cat = df["Categoria"].value_counts().rename_axis("Categoria").to_frame("Frecuencia")
st.dataframe(conteo_cat, use_container_width=True)

# -------------------------------
# 3) Visualización - Barras
# -------------------------------
st.subheader("📊 Gráfico de Barras: cantidad de registros por categoría")
st.caption("Cada barra representa cuántos registros hay en cada categoría.")
st.bar_chart(conteo_cat)  # Streamlit acepta DataFrame con columna "Frecuencia"

# -------------------------------
# 4) Visualización - Líneas
# -------------------------------
st.subheader("📈 Gráfico de Líneas: evolución de 'Valor' en el tiempo")
st.caption("Serie temporal de 'Valor' por fecha.")
# Para line_chart, index temporal y una columna numérica
serie_tiempo = df.set_index("Fecha")[["Valor"]].sort_index()
st.line_chart(serie_tiempo)

# -------------------------------
# 5) Descarga de datos
# -------------------------------
st.subheader("💾 Descargar datos")
csv = df.to_csv(index=False).encode("utf-8")
st.download_button(
    label="Descargar CSV",
    data=csv,
    file_name="datos_aleatorios.csv",
    mime="text/csv"
)

st.markdown("---")
st.caption("Construido con ❤️ usando Streamlit, NumPy y pandas.")
