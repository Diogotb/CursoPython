import streamlit as st
import pandas as pd

st.title('Título da Aplicação')
st.header('Cabeçalho Secundário')
st.subheader('Subcabeçalho Terciário')
st.text('Este é um texto simples.')
st.markdown('**Este é um texto em negrito usando Markdown.**')

# Sidebar: Adiciona uma barra lateral para inserir elementos de interface.
st.sidebar.title('Título na Barra Lateral')
st.sidebar.markdown('Texto na barra lateral.')

# Columns: Cria uma disposição em colunas para organizar elementos horizontalmente.
col1, col2 = st.columns(2)
col1.write('Este é o conteúdo da primeira coluna.')
col2.write('Este é o conteúdo da segunda coluna.')

#botões
if col1.button('Clique aqui'):
    col1.write('Botão clicado!')

#Caixa de seleção
if col2.checkbox('Marque-me'):
    col2.write('Caixa marcada!')


#Sliders
age = col1.slider('Selecione sua idade', 0, 100, 20)
col1.write(f'Sua idade é: {age}')

#inputs
nome = col2.text_input('Digite seu nome')
col2.write(f'Seu nome é: {nome}')

#DataFrames
data = {'Coluna 1': [1, 2, 3], 'Coluna 2': [4, 5, 6]}
df = pd.DataFrame(data)
st.write(df)

#Tabela
col2.table(df)

#Json
json_data = {'chave': 'valor', 'lista': [1, 2, 3]}
st.json(json_data)
