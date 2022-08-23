"""
1. Ler os valores de comprimento, largura e altura e apresentar
o valor do volume de uma caixa retangular. Utilize para o
cálculo a fórmula: VOLUME = COMPRIMENTO * LARGURA *
ALTURA.
    1. Função para ler os valores (não recebe parâmetro)
    2. Função para efetuar o cálculo do volume, recebendo como
        parâmetro o comprimento, a largura e altura
    3. Função para apresentar o resultado (recebe o resultado)
"""


comprimento = 0
largura = 0
altura = 0
volume = 0


def v_caixa():  # Função para ler os valores de comprimento, largura e altura
    global comprimento  # Declaração do comprimento como variável global
    comprimento = float(input('Informe comprimento:\n'))  # Recebe o valor do comprimento
    global largura
    largura = float(input('Informe a largura:\n'))
    global altura
    altura = float(input('Informe a altura:\n'))


def calculo(comp, lar, alt):  # Função para efetuar o cálculo do volume, recebendo como parâmetro o comprimento,
    # a largura e altura
    global volume
    volume = comp * lar * alt  # Calcula o volume


def resultado(vol):  # Função para apresentar o resultado
    print(f'O volume da caixa e: {vol}')  # Mostra o resultado


if __name__ == '__main__':  # Executa o programa
    v_caixa()  # Chama a função para ler os valores de comprimento, largura e altura
    calculo(comprimento, largura, altura)  # Chama a função para efetuar o cálculo do volume, recebendo como
    # parâmetro o comprimento, a largura e altura
    resultado(volume)  # Chama a função para apresentar o resultado
