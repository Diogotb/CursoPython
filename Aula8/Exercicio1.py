# Crie gráficos com uma tabela Excel(xlsx)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

df = pd.read_excel('Aula8/filmes.xlsx')
 
print(df)
