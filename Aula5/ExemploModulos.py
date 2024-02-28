import math
from datetime import datetime  # noqa: E402

raiz_quadrada = math.sqrt(25)  # Calcula a raiz quadrada de 25
seno_30_graus = math.sin(math.radians(30))  # Calcula o seno de 30 graus convertidos para radianos

print(raiz_quadrada)
print(seno_30_graus)

data_atual = datetime.now()  # Obtém a data e hora atual
ano_atual = data_atual.year  # Obtém o ano atual
print(data_atual)
print(ano_atual)

import operacoes  # noqa: E402
resultado_soma = operacoes.somar(5, 3)
resultado_subtracao = operacoes.subtrair(10, 4)

print(resultado_soma)
print(resultado_subtracao)

import estatisticas

dados = [2, 3, 5, 7, 11, 13, 17]
media = estatisticas.calcular_media(dados)
mediana = estatisticas.calcular_mediana(dados)
print(media)
print(mediana)

