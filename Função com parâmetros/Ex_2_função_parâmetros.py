"""
2. Leia um número inteiro e informe se ele é positivo
ou negativo
1. Função para ler o número inteiro (recebe uma mensagem)
2. Função para apresentar se é positivo ou negativo, recebendo como
parâmetro o número lido
"""

numero = 0


def leitura(msg):
    global numero  # Declaração do numero como variável global
    numero = int(input(msg))


def resultado(nun):  # Função para apresentar se é positivo ou negativo, recebendo como parâmetro o número lido
    if nun >= 0:  # Se o número for maior ou igual a zero
        print(f'{nun} e positivo!\n')
    else:  # Se o número for menor que zero
        print(f'{nun} e negativo!\n')


if __name__ == '__main__':  # Executa o programa
    leitura('Digite um numero!\n')
    resultado(numero)
    leitura('Teste um numero negativo!\n')
    resultado(numero)

