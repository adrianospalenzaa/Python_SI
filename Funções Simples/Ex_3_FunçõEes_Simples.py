"""
3. Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem,
utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o
usuário deve fornecer o # tempo gasto na viagem # e a # velocidade média # durante
ela. Desta forma, será possível obter a # distância percorrida # com a fórmula
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

tempo_gasto = 0
veloc_media = 0
dist_percorrida = 0
litros_usados = 0


def entr_dados():  # Função para ler os valores de tempo gasto e velocidade média
    global tempo_gasto
    tempo_gasto = float(input('Informe o tempo gasto da viagem:\n'))
    global veloc_media
    veloc_media = float(input('Informe a velocidade média:\n'))


def distancia():  # Função para calcular a distância
    global dist_percorrida
    dist_percorrida = tempo_gasto * veloc_media


def litros():  # Função para calcular a quantidade de litros
    global litros_usados
    litros_usados = dist_percorrida / 12


def resultado():  # Função para mostrar o resultado
    print(f'A velocidade média na viagem é:\n {veloc_media}')
    print(f'O tempo gasto na viagem é:\n {tempo_gasto}')
    print(f'A distancia percorrida na viagem é:\n {dist_percorrida}')
    print(f'A quantidade de litros usados na viagem é:\n {litros_usados}')


if __name__ == '__main__':  # Executa o programa
    entr_dados()  # Chama a função para ler os valores de tempo gasto e velocidade média
    distancia()  # Chama a função para calcular a distância
    litros()  # Chama a função para calcular a quantidade de litros
    resultado()  # Chama a função para mostrar o resultado
