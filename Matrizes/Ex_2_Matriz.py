"""
2. Leia uma matriz 4x4 e apresente:
• O somatório da segunda linha da matriz
• O somatório da segunda coluna da matriz
• O somatório de todos os elementos da matriz
"""
import numpy

matriz = numpy.empty([4, 4])

for linha in range(0, 4):
    for coluna in range(0, 4):
        matriz[linha, coluna] = int(input(f'Digite valor da linha {linha} e o valo da colulna {coluna}:\n'))
soma_linha = 0
soma_coluna = 0
soma_todos = 0
for linha in range(0, 4):
    for coluna in range(0, 4):
        soma_todos += matriz[linha, coluna]
        if linha == 1:
            soma_linha += matriz[linha, coluna]
        if coluna == 1:
            soma_coluna += matriz[linha, coluna]
print(f'Soma da linha 2: {soma_linha}')
print(f'Soma da coluna 2: {soma_coluna}')
print(f'Soma de todos os valores: {soma_todos}')
