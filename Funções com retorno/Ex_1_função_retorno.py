"""
1. Crie um programa que leia três valores e calcule a média
aritmética dos valores lidos
• Função para ler valores (não recebe parâmetro e retorna o valor
lido)
• Função para calcular a média (recebe como parâmetro os três
valores e retorna o resultado)
• Função para mostrar o resultado (recebe como parâmetro o valor
da média e imprime o valor, não retorna nada)
"""


def leitura(msg):  # Função para ler valores (não recebe parâmetro e retorna o valor lido)
    valor = int(input(msg))  # Recebe o valor lido e converte para inteiro
    return valor  # Retorna o valor lido


def calculo(v1, v2, v3):  # Função para calcular a média (recebe como parâmetro os três valores e retorna o resultado)
    return (v1 + v2 + v3) / 3  # Retorna a média aritmética


def resultado(md):
    print(f'A média aritmética é!\n {md}')  # Função para mostrar o resultado
    # (recebe como parâmetro o valor da média e imprime o valor, não retorna nada)


if __name__ == '__main__':  # Se o nome do módulo for main
    valor1 = leitura(' informe o valor 1!\n')  # Chama a função leitura e armazena o valor lido
    valor2 = leitura(' informe o valor 2!\n')
    valor3 = leitura(' informe o valor 3!\n')
    media = calculo(valor1, valor2, valor3)  # Chama a função calculo passando como parâmetro os três valores
    resultado(media)  # Chama a função resultado passando como parâmetro a média aritmética
