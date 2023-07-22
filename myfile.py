import streamlit as st
import pandas as pd
import numpy as np

st.title('Titulo del Proyecto')

option = st.selectbox('¿Cómo desea ser contactado/a?',('Email','Teléfono','Whatsapp'))
st.write('Seleccionó:', option)

df = pd.DataFrame(
  np.random.randn(1000,2) / [50, 50] + [37.76,-122.4],
  columns=['lat', 'lon'])
