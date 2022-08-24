"""
2. Leia um número inteiro e informe e retorne se ele é positivo
• Função para ler o valor (não recebe parâmetro e retorna o valor lido)
• Função para positivo (recebe como parâmetro o valor lido e retorna
verdadeiro se for positivo ou falso se for negativo)
"""


def leitura(msg):  # Função para ler o valor (não recebe parâmetro e retorna o valor lido)
    valor = int(input(msg))  # Recebe o valor lido e converte para inteiro
    return valor  # Retorna o valor lido


def positivo(valor):  # Função para positivo (recebe como parâmetro o valor lido e retorna
    # verdadeiro se for positivo ou falso se for negativo)
    if valor > 0:  # Se o valor for maior que 0
        return True  # Retorna verdadeiro
    else:  # Se o valor for menor ou igual a 0
        return False  # Retorna falso


if __name__ == '__main__':  # Se o nome do módulo for main
    val = leitura(' informe o valor!\n')  # Chama a função leitura e armazena o valor lido
    if positivo(val):  # Chama a função positivo passando como parâmetro o valor lido
        print("O valor é positivo!")  # Imprime se o valor for positivo
    else:  # Se o valor não for positivo
        print("O valor é negativo!")  # Imprime se o valor for negativo
