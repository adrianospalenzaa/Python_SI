import numpy

vetor = numpy.empty(5)

for posicao in range(0, 5):
    vetor[posicao] = float(input(f'Digite o valor {posicao + 1}:\n'))

pesquisa = float(input('Digite o valor para pesquisa\n'))

for posicao in range(0, 5):
    if vetor[posicao] == pesquisa:
        print(f'O valor {pesquisa} foi encontrado na posição {posicao}')