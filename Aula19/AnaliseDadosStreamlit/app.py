import streamlit as st
import pandas as pd

# Carregar dados de um arquivo CSV
df = pd.read_csv('movies.csv')


# Exibir os primeiros registros do DataFrame
st.write(df.head())

#Filtros de Seleção
filtro = st.sidebar.selectbox('Selecione o Filtro',df.columns)

valor = st.sidebar.text_input('Digite o valor do filtro')

# Aplicar o filtro ao DataFrame
df_filtrado = df[df[filtro] == valor]
st.write(df_filtrado)
