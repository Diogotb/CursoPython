import streamlit as st
import pandas as pd

# Carregar dados de um arquivo CSV
df = pd.read_csv('movies.csv')

<<<<<<< HEAD

# Exibir os primeiros registros do DataFrame
st.write(df.head())

#Filtros de Seleção
filtro = st.sidebar.selectbox('Selecione o Filtro',df.columns)

valor = st.sidebar.text_input('Digite o valor do filtro')
=======
# Exibir os primeiros registros do DataFrame
st.write(df.head())

# Filtragem simples
filtro = st.sidebar.selectbox('Selecione uma coluna para filtrar:', df.columns)
valor = st.sidebar.text_input('Digite o valor a ser filtrado:')
>>>>>>> b833215a4d54b95b94e4d116ef54458795fff479

# Aplicar o filtro ao DataFrame
df_filtrado = df[df[filtro] == valor]
st.write(df_filtrado)
<<<<<<< HEAD
=======

>>>>>>> b833215a4d54b95b94e4d116ef54458795fff479
