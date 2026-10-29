
import streamlit as st
import pandas as pd

df = pd.read_csv("canciones.csv")

st.title("🎵 Listado de canciones")

st.dataframe(df)
