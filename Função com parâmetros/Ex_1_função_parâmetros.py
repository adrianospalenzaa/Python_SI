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


def v_caixa():
    global comprimento
    comprimento = float(input('Informe comprimento:\n'))
    global largura
    largura = float(input('Informe a largura:\n'))
    global altura
    altura = float(input('Informe a altura:\n'))


def calculo(comp, lar, alt):
    global volume
    volume = comp * lar * alt


def resultado(vol):
    print(f'O volume da caixa e: {vol}')


if __name__ == '__main__':
    v_caixa()
    calculo(comprimento, largura, altura)
    resultado(volume)
