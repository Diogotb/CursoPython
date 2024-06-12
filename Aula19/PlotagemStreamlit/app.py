import streamlit as st
import pandas as pd
import numpy as np


# Criar um DataFrame de exemplo
np.random.seed(42)
data = {
    'categoria': ['A', 'B', 'C', 'D'] * 25,
    'valor1': np.random.randn(100),
    'valor2': np.random.rand(100) * 100
}
df = pd.DataFrame(data)


import matplotlib.pyplot as plt

# Gráfico de barras
fig, ax = plt.subplots()
df.groupby('categoria').mean()['valor1'].plot(kind='bar', ax=ax)
ax.set_title('Média de Valor2 por Categoria')
st.pyplot(fig)

import seaborn as sns

# Gráfico de dispersão com seaborn
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='valor1', y='valor2', hue='categoria', ax=ax)
ax.set_title('Dispersão de Valor1 vs Valor2')
st.pyplot(fig)


import plotly.express as px


# Gráfico de dispersão com plotly
fig = px.scatter(df, x='valor1', y='valor2', color='categoria', title='Dispersão de Valor1 vs Valor2')
st.plotly_chart(fig)
