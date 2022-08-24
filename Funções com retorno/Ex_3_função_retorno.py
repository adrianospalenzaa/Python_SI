"""
3. Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem,
utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o
usuário deve fornecer o tempo gasto na viagem e a velocidade média durante
ela. Desta forma, será possível obter a distância percorrida com a fórmula
DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a
quantidade de litros de combustível utilizada na viagem, com a fórmula:
LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da
velocidade média, tempo gasto na viagem, a distância percorrida e a
quantidade de litros utilizada na viagem
• Função para ler os valores (recebe como parâmetro uma mensagem para ser exibida
e retorna o valor lido)
• Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e
retorna a distância)
• Função para calcular a quantidade de litros (recebe como parâmetro a distância e
retorna os litros)
• Função para apresentar o resultado (recebe como parâmetro os valores e mostrar a
mensagem – não possui retorno)
"""



def leitura(msg):  # Função para ler o valor (não recebe parâmetro e retorna o valor lido)
    print(msg)  # Imprime a mensagem
    return float(input())  # Recebe o valor lido e converte para float


def calculo_dis(tempo, velocidade):  # Função para calcular a distância
    # (recebe como parâmetro o tempo e a velocidade e retorna a distância)
    return tempo * velocidade  # Retorna a distância


def calculo_litros(distancia):
    return distancia / 12


def resultado(t, v, d, l):  # Função para apresentar o resultado
    # (recebe como parâmetro os valores e mostrar a mensagem – não possui retorno)
    print(f'Tempo {t}')
    print(f'Velocidade {v}')
    print(f'Distancia {d}')
    print(f'Litros {l}')


if __name__ == '__main__':
    tempo = leitura("Informe o tempo gasto na viagem:")
    velocidade = leitura("Informe a velocidade média na viagem:")
    distancia = calculo_dis(tempo, velocidade)
    litros = calculo_litros(distancia)
    resultado(tempo, velocidade, distancia, litros)
