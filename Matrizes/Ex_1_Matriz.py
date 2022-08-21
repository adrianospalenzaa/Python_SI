"""
1. Leia uma matriz de inteiros 3x3. Após leia um valor
individual e mostre quantas vezes o número
digitado aparece na matriz
"""
import numpy

matriz = numpy.empty([3, 3]) # Cria uma matriz 3x3 vazia

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha, coluna] = int(input(f'Digite o valor da linha {linha} e da coluna {coluna}:'))
pesquisa = int(input('Digite numero de pesquisa:'))
cont = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(matriz[linha, coluna])
        if matriz[linha, coluna] == pesquisa:
            cont += 1
print(cont)
