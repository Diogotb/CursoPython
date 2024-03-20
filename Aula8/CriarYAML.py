import yaml

# Dados fictícios
dados = {
    'alunos': ['Joao', 'Maria', 'Pedro', 'Ana', 'Carla'],
    'notas': [8, 7, 9, 6, 8],
    'idade': [20, 22, 21, 19, 20],
    'altura': [1.75, 1.65, 1.80, 1.70, 1.68]
}

# Salvar os dados em um arquivo YAML
with open('Aula8/dados.yaml', 'w') as file:
    yaml.dump(dados, file)

print("Arquivo YAML criado com sucesso!")
