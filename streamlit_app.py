import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import time, datetime


st.header('ACD y NLP')

# Ejemplo 1
add_sidebar = st.sidebar.selectbox('Generación A', ('Generación A','Generación B'))

if add_sidebar == 'Generación A':

    metrica_conteo= st.selectbox('Selecciona la métrica',('TF-IDF', 'Frecuencia'))
    
    if metrica_conteo == 'TF-IDF':
        df1 = pd.read_csv("TF-IDF.csv", index_col=0)
        st.write(df1)

        dfaa = pd.read_csv("FrecuenciasTipoGenA.csv", index_col=0)
        st.write(dfaa)
    
    if metrica_conteo == 'Frecuencia':
        df2 = pd.read_csv("FrecuenciasGenA.csv", index_col=0)
        st.write(df2)
    
    df_agg_metrics = df_agg[['Video publish time','Views','Likes','Subscribers','Shares','Comments added','RPM(USD)','Average % viewed',
                             'Avg_duration_sec', 'Engagement_ratio','Views / sub gained']]

st.write('Hello, *World!* :sunglasses:')

# Ejemplo 2

st.write(1234)

# Ejemplo 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Ejemplo 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Ejemplo 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']).interactive()
st.write(c)


st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)
