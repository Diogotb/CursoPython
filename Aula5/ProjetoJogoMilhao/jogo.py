# jogo.py

import perguntas

def exibir_pergunta(pergunta):
    print(pergunta['pergunta'])
    for opcao in pergunta['opcoes']:
        print(opcao)
    resposta = input('Escolha a opção correta (A, B, C, ou D): ')
    return resposta.upper()

def jogar():
    dinheiro_acumulado = 0

    for indice, pergunta in enumerate(perguntas.perguntas):
        print(f"\n\nPergunta {indice}:")
        resposta_usuario = exibir_pergunta(pergunta)

        if resposta_usuario == pergunta['resposta_correta']:
            dinheiro_acumulado += 1000
            print(f"Resposta Correta! Você ganhou ${dinheiro_acumulado}.")
        else:
            print("Resposta Incorreta. Fim de Jogo.")
            break

    else:
        print(f"\n\nParabéns! Você ganhou um total de ${dinheiro_acumulado}.")

jogar()
