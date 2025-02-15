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
add_sidebar = st.sidebar.selectbox('Generación A', ('Generación A','Generación B'))

if add_sidebar == 'Generación A':

    metrica_conteo= st.selectbox('Selecciona la métrica',('TF-IDF', 'Frecuencia'))
    
    if metrica_conteo == 'TF-IDF':
        df1 = pd.read_csv("TF-IDF.csv", index_col=0)
        st.write(df1)

    
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


if add_sidebar == 'Generación B':

     metrica_conteo= st.selectbox('Selecciona la métrica',('TF-IDF', 'Frecuencia'))

     if metrica_conteo == 'TF-IDF':
        df4 = pd.read_csv("TF-IDFB.csv", index_col=0)
        st.write(df4)


