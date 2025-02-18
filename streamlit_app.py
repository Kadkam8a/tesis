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
add_sidebar = st.sidebar.selectbox('Sustantivos', ('Sustantivos','Adjetivos'))

if add_sidebar == 'Sustantivos':

    metrica_conteo= st.selectbox('Selecciona la métrica',( 'Frecuencia', 'TF-IDF'))
    
    if metrica_conteo == 'Frecuencia':
        df2 = pd.read_csv("sustantivos.csv")
        st.write(df2)

if add_sidebar == 'Adjetivos':

     metrica_conteo= st.selectbox('Selecciona la métrica',('Frecuencia', 'TF-IDF'))

     if metrica_conteo == 'Frecuencia':
        df4 = pd.read_csv("adjetivos.csv")
        st.write(df4)


