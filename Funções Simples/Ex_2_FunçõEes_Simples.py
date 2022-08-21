"""
2. Ler uma temperatura em graus Celsius e apresentá-la
convertida em graus Fahrenheit. A fórmula de conversão é
F = (9 * C + 160) / 5, na qual F é a temperatura em
Fahrenheit e C é a temperatura em graus Celsius
• Função para ler os valores
• Função para fazer o cálculo
• Função para mostrar o resultado
"""

celsius = 0
fahrenheit = 0


def intro_temperatura():  # Função para ler os valores de temperatura em graus Celsius
    global celsius  # Declaração de variável global
    celsius = float(input('Informe a temperatura em Celsius:\n'))  # Lê a temperatura em graus Celsius


def conv_temperatura():  # Função para fazer o cálculo de temperatura em graus Fahrenheit
    global fahrenheit  # Declaração de variável global
    fahrenheit = (9 * celsius + 160) / 5  # Cálculo da temperatura em graus Fahrenheit


def resul_temperatura():  # Função para mostrar o resultado de temperatura em graus Fahrenheit
    print(f'A temperatura em Fahrenheit e {fahrenheit}')  # Mostra o resultado da temperatura em graus Fahrenheit


intro_temperatura()  # Chama a função para ler os valores de temperatura em graus Celsius
conv_temperatura()  # Chama a função para fazer o cálculo de temperatura em graus Fahrenheit
resul_temperatura()  # Chama a função para mostrar o resultado da temperatura em graus Fahrenheit
