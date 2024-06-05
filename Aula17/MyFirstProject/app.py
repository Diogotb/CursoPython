import pandas as pd  # Biblioteca para manipulação e análise de dados
import matplotlib.pyplot as plt  # Biblioteca para criação de gráficos estáticos
import plotly.express as px  # Biblioteca para criação de gráficos interativos
from flask import Flask, render_template, send_from_directory  # Biblioteca para criação de aplicações web

def analyze_data(file_path):
    # Carregar dados do arquivo CSV para um DataFrame do Pandas
    df = pd.read_csv(file_path)
    
    # Realizar análises básicas (sumário estatístico) dos dados
    summary = df.describe()
    
    # Gerar um histograma da coluna 'column_of_interest' usando Matplotlib
    plt.figure(figsize=(10, 6))  # Definir o tamanho da figura
    df['column_of_interest'].hist()  # Criar o histograma
    plt.title('Histograma da Coluna de Interesse')  # Adicionar título ao gráfico
    plt.xlabel('Valores')  # Adicionar rótulo ao eixo X
    plt.ylabel('Frequência')  # Adicionar rótulo ao eixo Y
    plt.savefig('static/plot.png')  # Salvar o gráfico como um arquivo PNG na pasta 'static'
    plt.close()  # Fechar a figura para evitar sobreposição de gráficos

    # Gerar um histograma interativo da coluna 'column_of_interest' usando Plotly
    fig = px.histogram(df, x='column_of_interest', title='Histograma Interativo da Coluna de Interesse')
    fig.write_html('templates/plot.html')  # Salvar o gráfico interativo como um arquivo HTML na pasta 'templates'
    
    return summary  # Retornar o sumário estatístico

# Inicializa o aplicativo Flask
app = Flask(__name__)

@app.route('/')
def index():
    # Analisa os dados e gera os gráficos
    summary = analyze_data('data.csv')
    
    # Renderiza o template 'index.html' passando o sumário estatístico como parâmetro
    return render_template('index.html', summary=summary.to_html())

@app.route('/plot')
def plot():
    # Envia o arquivo de gráfico estático gerado com Matplotlib
    return send_from_directory('static', 'plot.png')

@app.route('/plot_interactive')
def plot_interactive():
    # Renderiza o template 'plot.html' que contém o gráfico interativo gerado com Plotly
    return render_template('plot.html')

if __name__ == '__main__':
    # Executa o servidor Flask no modo de depuração
    app.run(debug=True)
