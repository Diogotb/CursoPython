# app.py
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def analyze_data(file_path):
    # Carregar dados
    df = pd.read_csv(file_path)
    
    # Realizar análises básicas
    summary = df.describe()
    
    # Gerar um gráfico com Matplotlib
    plt.figure(figsize=(10, 6))
    df['column_of_interest'].hist()
    plt.title('Histograma da Coluna de Interesse')
    plt.xlabel('Valores')
    plt.ylabel('Frequência')
    plt.savefig('static/plot.png')
    
    # Gerar um gráfico interativo com Plotly
    fig = px.histogram(df, x='column_of_interest', title='Histograma Interativo da Coluna de Interesse')
    fig.write_html('templates/plot.html')
    
    return summary
