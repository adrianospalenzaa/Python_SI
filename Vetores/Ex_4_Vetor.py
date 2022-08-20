"""
4. Leia um vetor de 10 elementos e apresente:
• O somatório de todos os valores
• A média de todos os valores
• A quantidade de números negativos
"""
import numpy

vetor = numpy.empty(10)
negat = 0
soma = 0
for posicao in range(0, 10):
    vetor[posicao] = int(input(f'Digite o {posicao + 1}° valor!\n'))

for posicao in range(0, 10):
    #soma = sum(vetor)
    soma = soma + vetor[posicao]
    media = soma / 10
    if vetor[posicao] < 0:
        negat = negat + 1
print(f'Soma dos valores {soma}')
print(f'Media dos valores {media}')
print(f'Quantidade de valores negativos {negat}')
