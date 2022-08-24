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
    valor = int(input(msg))  # Recebe o valor lido e converte para inteiro
    return valor  # Retorna o valor lido


def distancia(tempo, velocidade):  # Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
    return tempo * velocidade  # Retorna a distância


def litros(distancia):  # Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
    return distancia / 12  # Retorna os litros


def resultado(velocidade, tempo, distancia, litros):  # Função para apresentar o resultado (recebe como parâmetro os valores e mostrar a mensagem – não possui retorno)
    print("Velocidade média: {} Km/h".format(velocidade))  # Imprime a velocidade média
    print("Tempo gasto: {} horas".format(tempo))  # Imprime o tempo gasto
    print("Distância percorrida: {} Km".format(distancia))  # Imprime a distância percorrida
    print("Quantidade de litros utilizada: {} litros".format(litros))  # Imprime a quantidade de litros utilizada


if __name__ == '__main__':  # Se o nome do módulo for main
    velocidade = leitura('Informe a velocidade média!\n')  # Chama a função leitura e armazena o valor lido
    tempo = leitura('Informe o tempo gasto!\n')  # Chama a função leitura e armazena o valor lido
    distancia = distancia(tempo, velocidade)  # Chama a função distancia passando como parâmetro o tempo e a velocidade e armazena o valor retornado
    litros = litros(distancia)  # Chama a função litros passando como parâmetro a distância e armazena o valor retornado
    resultado(velocidade, tempo, distancia, litros)  # Chama a função resultado passando como parâmetro os valores e mostra a mensagem

