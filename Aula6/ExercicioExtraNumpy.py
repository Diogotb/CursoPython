import numpy as np
import matplotlib.pyplot as plt

# Dados fictícios de preços médios diários para duas ações (em dólares)
preco_medio_acao1 = np.array([50, 52, 48, 55, 53, 51, 49, 50, 54, 52])
preco_medio_acao2 = np.array([120, 122, 118, 125, 123, 121, 119, 120, 124, 122])

# Número de ações que o investidor possui de cada empresa
acoes_acao1 = 100 # Exemplo: o investidor possui 100 ações da Ação 1
acoes_acao2 = 50  # Exemplo: o investidor possui 50 ações da Ação 2

# Calculando o valor do investimento em cada dia
investimento_acao1 =acoes_acao1 * preco_medio_acao1
investimento_acao2 = acoes_acao2 * preco_medio_acao2

# Calculando o patrimônio total do investidor em cada dia
patrimonio_total = investimento_acao1 + investimento_acao2

# Plotando o gráfico da evolução patrimonial do investidor e das ações
dias = list(range(1, 11))

# Linha do Patrimônio Total
plt.plot(dias, patrimonio_total, label='Patrimônio Total', marker='o', linestyle='-', color='b')

# Linha do Valor Total das Ações da Ação 1
plt.plot(dias, investimento_acao1, label='Valor Ação 1', marker='o', linestyle='-', color='g')

# Linha do Valor Total das Ações da Ação 2
plt.plot(dias, investimento_acao2, label='Valor Ação 2', marker='o', linestyle='-', color='r')

plt.xlabel('Dia')
plt.ylabel('Valor ($)')
plt.title('Evolução Patrimonial e de Ações do Investidor')
# plt.grid(True)
plt.legend()
plt.show()
