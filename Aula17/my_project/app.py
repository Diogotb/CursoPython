# app.py
from flask import Flask, render_template, send_from_directory
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

app = Flask(__name__)

def analyze_data(file_path):
    df = pd.read_csv(file_path)
    summary = df.describe()
    
    plot_histogram(df, 'column_of_interest')
    plot_scatter(df, 'column_x', 'column_y')
    plot_bar(df, 'category')
    plot_boxplot(df, 'column_of_interest')
    plot_line(df, 'date', 'value')

    fig = px.histogram(df, x='column_of_interest', title='Histograma Interativo da Coluna de Interesse')
    fig.write_html('templates/plot.html')
    
    return summary

def plot_histogram(df, column):
    plt.figure(figsize=(10, 6))
    df[column].hist()
    plt.title(f'Histograma da Coluna {column}')
    plt.xlabel('Valores')
    plt.ylabel('Frequência')
    plt.savefig(f'static/hist_{column}.png')

def plot_scatter(df, column_x, column_y):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[column_x], df[column_y])
    plt.title(f'Gráfico de Dispersão entre {column_x} e {column_y}')
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.savefig(f'static/scatter_{column_x}_{column_y}.png')

def plot_bar(df, column):
    plt.figure(figsize=(10, 6))
    df[column].value_counts().plot(kind='bar')
    plt.title(f'Gráfico de Barras da Coluna {column}')
    plt.xlabel(column)
    plt.ylabel('Contagem')
    plt.savefig(f'static/bar_{column}.png')

def plot_boxplot(df, column):
    plt.figure(figsize=(10, 6))
    df.boxplot(column=column)
    plt.title(f'Boxplot da Coluna {column}')
    plt.savefig(f'static/boxplot_{column}.png')

def plot_line(df, date_column, value_column):
    plt.figure(figsize=(10, 6))
    plt.plot(df[date_column], df[value_column])
    plt.title(f'Gráfico de Linha de {value_column} ao longo do tempo')
    plt.xlabel(date_column)
    plt.ylabel(value_column)
    plt.savefig(f'static/line_{value_column}.png')

@app.route('/')
def index():
    summary = analyze_data('data.csv')
    return render_template('index.html', summary=summary.to_html())

@app.route('/plot/<plot_type>/<column>')
def plot(plot_type, column):
    return send_from_directory('static', f'{plot_type}_{column}.png')

@app.route('/plot/scatter/<column_x>/<column_y>')
def plot_scatter_route(column_x, column_y):
    return send_from_directory('static', f'scatter_{column_x}_{column_y}.png')

@app.route('/plot_interactive')
def plot_interactive():
    return render_template('plot.html')

if __name__ == '__main__':
    app.run(debug=True)
