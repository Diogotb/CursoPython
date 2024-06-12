import streamlit as st
import pandas as pd

# Carregar dados de um arquivo CSV
df = pd.read_csv('movies.csv')

# Exibir os primeiros registros do DataFrame
st.write(df.head())

# Filtragem simples
filtro = st.sidebar.selectbox('Selecione uma coluna para filtrar:', df.columns)
valor = st.sidebar.text_input('Digite o valor a ser filtrado:')

# Aplicar o filtro ao DataFrame
df_filtrado = df[df[filtro] == valor]
st.write(df_filtrado)

