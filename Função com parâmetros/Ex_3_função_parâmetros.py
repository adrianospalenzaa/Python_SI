"""
3. Leia a idade do usuário e classifique-o em:
• Criança – 0 a 12 anos
• Adolescente – 13 a 17 anos
• Adulto – acima de 18 anos (mostrar mensagem se o número for
negativo)
• Função para ler a idade (recebe uma mensagem como parâmetro)
• Função para mostrar na tela a faixa etária, recebendo como
parâmetro a idade da pessoa
"""


idade = 0


def leitura(msg):  # Função para ler a idade (recebe uma mensagem como parâmetro)
    global idade  # Declaração do idade como variável global
    idade = int(input(msg))


def resultado(ida):  # Função para mostrar na tela a faixa etária, recebendo como parâmetro a idade da pessoa
    if ida <= 12:  # Se a idade for menor ou igual a 12
        print('Criança!\n')
    elif 12 < ida <= 17:  # Se a idade for maior que 12 e menor ou igual a 17
        print('Adolescente!\n')
    else:  # Se a idade for maior que 17
        print('Adulto!\n')


if __name__ == '__main__':  # Se o nome do módulo for main
    leitura('Informe sua idade:\n')  # Chama a função leitura
    resultado(idade)  # Chama a função resultado passando como parâmetro a idade da pessoa
