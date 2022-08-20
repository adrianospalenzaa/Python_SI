"""
3. Leia um vetor A com 10 elementos do tipo real. Construir um vetor B de mesmo
tipo, sendo que cada elemento do vetor B deve ser o cubo de cada elemento
correspondente do vetor A. Apresentar no final os dois vetores
"""
import numpy

vetor_a = numpy.empty(10)
vetor_b = numpy.empty(10)

for posicao in range(0, 10):
    vetor_a[posicao] = float(input('Digite valor! \n'))
    vetor_b[posicao] = vetor_a[posicao] ** 3

print(f' Vetor A \n {vetor_a}')
print(f'Verto B ao Cubo \n {vetor_b}')
