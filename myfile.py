import streamlit as st
import pandas as pd
import numpy as np

st.title('Titulo del Proyecto')

num = st.slider("num", 0, 100, step=1)
st.write("El numero ingresado es {}".format(num))
df = pd.DataFrame(np.random.randn(1000,2) / [50,50] + [37.76, -122.4], columns=['lat','lon'])
#Mostrar mapa
st.map(df)

n = st.slider("n", 5,100,step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)
