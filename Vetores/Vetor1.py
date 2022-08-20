import numpy

vetor = numpy.empty(5)

for posicao in range(0, 5):
    valor = float(input(f'Digite o valor {posicao + 1}: '))
    vetor[posicao] = valor
for posicao in range(0, 5):
    print(vetor[posicao])
