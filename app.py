
import streamlit as st
import pandas as pd

df = pd.read_csv("canciones.csv")

st.title("🎵 Listado de canciones")

st.dataframe(df)


# ---------------------------------------------------------
# INSTRUCCIONES PARA EJECUTAR LA APP
#
# 1. Abrir una terminal en la carpeta del proyecto.
#
# 2. Crear un entorno virtual (solo la primera vez):
#    python3 -m venv .venv
#
# 3. Activar el entorno virtual:
#    source .venv/bin/activate
#
# 4. Instalar las librerías (solo la primera vez):
#    python -m pip install streamlit pandas
#
# 5. Ejecutar la aplicación:
#    python -m streamlit run app.py
#
# La aplicación se abrirá en el navegador.
# Para detenerla, presionar Ctrl + C en la terminal.
# ---------------------------------------------------------