import numpy as np

# Como criar uma matriz NumPy vazia e uma matriz preenchida com valores iguais a 1?
matriz_vazia = np.empty((3, 3))
matriz_ones = np.ones((3, 3))

# Crie uma matriz NumPy preenchida com todos os zeros.
matriz_zeros = np.zeros((3, 3))

# Crie uma matriz NumPy preenchida com valores aleatórios entre 0 e 1.
matriz_random = np.random.rand(3, 3)

# Crie um array unidimensional com os números de 1 a 5.
array_1d = np.array([1, 2, 3, 4, 5])

# Crie um array bidimensional (matriz) 2x3 com números inteiros.
matriz_2x3 = np.random.randint(10, size=(2, 3))

# Indexação e Seleção:
# Selecione elementos específicos de uma matriz NumPy.
elemento_matriz = matriz_2x3[1, 2]

# Encontre o valor máximo e mínimo em uma matriz fornecida.
max_valor = np.max(matriz_2x3)
min_valor = np.min(matriz_2x3)

# Calcule a soma dos valores em uma matriz.
soma_valores = np.sum(matriz_2x3)

# Manipulação de Arrays:
# Remova entradas unidimensionais de uma matriz.
array_flatten = matriz_2x3.flatten()

# Adicione ou subtraia matrizes em Python.
matriz_soma = matriz_2x3 + matriz_ones
matriz_subtracao = matriz_2x3 - matriz_ones

# Multiplique matrizes usando NumPy.
matriz_multiplicacao = np.dot(matriz_2x3, matriz_ones)

# Operações Estatísticas:
# Calcule a média, mediana e desvio padrão de uma matriz plana.
media_valores = np.mean(array_flatten)
mediana_valores = np.median(array_flatten)
desvio_padrao_valores = np.std(array_flatten)

# Calcule a soma dos elementos diagonais de uma matriz NumPy.
soma_diagonal = np.trace(matriz_2x3)

# Desafios Avançados:
# Encontre o número de linhas e colunas de uma matriz usando NumPy.
num_linhas, num_colunas = matriz_2x3.shape

# Verifique se um array NumPy contém uma linha específica.
linha_especifica = np.array([1, 2, 3])
contem_linha = np.any(np.all(matriz_2x3 == linha_especifica, axis=1))

# Troque dois eixos de uma matriz NumPy.
matriz_troca_eixos = np.swapaxes(matriz_2x3, 0, 1)

