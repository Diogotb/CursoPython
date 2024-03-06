import numpy as np

# criação de arrays

empty_array = np.empty((3, 3)) #criei um array de 3 linhas e 3 colunas vazios
print(empty_array)

ones_array = np.ones((2, 2)) #criação de array 2x2 preenchido com 1
print(ones_array)

zeros_array = np.zeros((4, 4)) #array 4x4 preenchido com 0
print(zeros_array)

random_array = np.random.rand(3, 3) #array 3x3 prenchido com rando
print(random_array)

#Indexação e Seleção:
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_array)
print(my_array[1, 2])  # Seleciona o elemento na segunda linha e terceira coluna (6)

#máximo e mínimo
max_value = np.max(my_array)
min_value = np.min(my_array)
print(f"Valor máximo: {max_value}, Valor mínimo: {min_value}")

total_sum = np.sum(my_array)
print(f"Soma total: {total_sum}")


# Manipulação de Arrays:

# unidimensionais
squeezed_array = np.squeeze(my_array)
print(squeezed_array)

# Adição de Matrizes: usamos o operador +. Aqui está um exemplo:
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 + matriz2
print("Resultado da adição de matrizes:")
print(resultado)

# Subtração de Matrizes: usamos o operador -. Aqui está um exemplo:
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = matriz1 - matriz2
print("Resultado da subtração de matrizes:")
print(resultado)

# Multiplicação de Matrizes: Para multiplicar matrizes em Python, podemos usar a função numpy.dot() ou o operador @. Aqui está um exemplo:
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
resultado = np.dot(matriz1, matriz2)
# Ou, alternativamente: resultado = matriz1 @ matriz2
print("Resultado da multiplicação de matrizes:")
print(resultado)

