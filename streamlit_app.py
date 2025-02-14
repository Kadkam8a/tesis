import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import time, datetime


def pos(fila):
    # Verifica si algún valor en la fila es 'VERB'
    if 'VERB' in fila.values:
        # Si es así, toda la fila se pone verde
        return ['background-color: #d4edb7'] * len(fila)
    elif 'NOUN' in fila.values:
        # Si es así, toda la fila se pone verde
        return ['background-color: #d8b7ed'] * len(fila)
    elif 'ADJ' in fila.values:
        # Si es así, toda la fila se pone verde
        return ['background-color: #edd4b7'] * len(fila)
    else:
        # Si no, deja la fila sin color
        return [''] * len(fila)

st.header('ACD y NLP')

# Ejemplo 1
add_sidebar = st.sidebar.selectbox('Selecciona la Generación', ('Generación A','Generación B'))

if add_sidebar == 'Generación A':

    metrica_conteo= st.selectbox('Selecciona la métrica',('TF-IDF', 'Frecuencia'))
    
    if metrica_conteo == 'TF-IDF':
        df1 = pd.read_csv("TF-IDF.csv", index_col=0)
        st.write(df1)

        dfaa = pd.read_csv("FrecuenciasTipoGenA.csv", index_col=0)
        st.write(dfaa)
    
    if metrica_conteo == 'Frecuencia':
        df2 = pd.read_csv("FrecuenciasTipoGenA.csv", index_col=0)
        df2['La Señal'] = df2['La Señal'].fillna(0).astype(int)
        df2['Los Recuerdos del Porvenir'] = df2['Los Recuerdos del Porvenir'].fillna(0).astype(int)
        df2['Oficio de Tinieblas'] = df2['Oficio de Tinieblas'].fillna(0).astype(int)
        intento1 = df2.style.apply(pos, axis=1)
        st.write('Inés')
        st.write(intento1)
        st.write('Elena')
        df3 = pd.read_csv("FrecuenciasTipoGenAelena.csv", index_col=0)
        df3['La Señal'] = df3['La Señal'].fillna(0).astype(int)
        df3['Los Recuerdos del Porvenir'] = df3['Los Recuerdos del Porvenir'].fillna(0).astype(int)
        df3['Oficio de Tinieblas'] = df3['Oficio de Tinieblas'].fillna(0).astype(int)
        intento2 = df3.style.apply(pos, axis=1)
        st.write(intento2)
        st.write('Rosario')
        df4 = pd.read_csv("FrecuenciasTipoGenArosario.csv", index_col=0)
        df4['La Señal'] = df4['La Señal'].fillna(0).astype(int)
        df4['Los Recuerdos del Porvenir'] = df4['Los Recuerdos del Porvenir'].fillna(0).astype(int)
        df4['Oficio de Tinieblas'] = df4['Oficio de Tinieblas'].fillna(0).astype(int)
        intento3 = df4.style.apply(pos, axis=1)
        st.write(intento3)
        


    
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
