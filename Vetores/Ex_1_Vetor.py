"""
1. Leia um vetor A de 10 elementos inteiros e um valor individual X. A seguir,
imprimir os índices do vetor A em que aparece um valor igual a X
"""
import numpy

vetor_a = numpy.empty(2)

for posicao in range(0, 2):
    vetor_a[posicao] = int(input(f'Digite valor {posicao + 1}\n'))

v_pesquisa = int(input('Digite o valor de pesquisa\n'))

for posicao in range(0, 2):
    if vetor_a[posicao] == v_pesquisa:
        print(f'A pesquisa {v_pesquisa} foi encontra na {posicao +1}')
