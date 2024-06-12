import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Função para carregar os dados
@st.cache_data
def load_data():
    return pd.read_csv('vendas.csv')

# Carregar os dados
df = load_data()

# Título do aplicativo
st.title('Dashboard de Vendas Interativo')

# Barra lateral para filtros
st.sidebar.header('Filtros')

# Filtro por categoria
categorias = df['categoria'].unique()
categoria_selecionada = st.sidebar.multiselect('Categoria', categorias, default=categorias)

# Filtro por subcategoria
subcategorias = df['subcategoria'].unique()
subcategoria_selecionada = st.sidebar.multiselect('Subcategoria', subcategorias, default=subcategorias)

# Aplicar filtros
df_filtrado = df[df['categoria'].isin(categoria_selecionada) & df['subcategoria'].isin(subcategoria_selecionada)]

# Seção de visualização de dados
st.header('Visualização de Dados Filtrados')
st.write(df_filtrado)

# Seção de gráficos
st.header('Gráficos Interativos')

# Seleção do tipo de gráfico
tipo_grafico = st.selectbox('Selecione o tipo de gráfico', ['Barra', 'Linha', 'Dispersão', 'Histograma'])

# Função para criar gráficos
def criar_grafico(tipo):
    if tipo == 'Barra':
        fig = px.bar(df_filtrado, x='data', y='vendas', color='categoria', title='Vendas por Data e Categoria')
    elif tipo == 'Linha':
        fig = px.line(df_filtrado, x='data', y='vendas', color='categoria', title='Vendas por Data e Categoria')
    elif tipo == 'Dispersão':
        fig = px.scatter(df_filtrado, x='vendas', y='quantidade', color='categoria', title='Dispersão de Vendas e Quantidade')
    elif tipo == 'Histograma':
        fig = px.histogram(df_filtrado, x='vendas', color='categoria', title='Histograma de Vendas')
    st.plotly_chart(fig)

# Criar o gráfico selecionado
criar_grafico(tipo_grafico)

# Exibir as métricas
st.header('Métricas de Vendas')
st.metric('Total de Vendas', f'R$ {df_filtrado["vendas"].sum():,.2f}')
st.metric('Quantidade Total de Produtos Vendidos', int(df_filtrado['quantidade'].sum()))
