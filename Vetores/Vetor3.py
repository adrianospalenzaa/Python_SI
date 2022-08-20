import numpy

nome = numpy.empty(5, dtype=object)

for posicao in range(0, 5):
    nome[posicao] = input(f'Digite o nome {posicao + 1} \n')
for posicao in range(0, 5):
    print(nome[posicao],(f'\nEstá na posição {posicao}'))

