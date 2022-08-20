"""
3. Leia duas matrizes A e B com as dimensões 3x3. Crie
uma nova matriz C de mesma dimensão que seja a
soma de A + B. No final, imprimir a matriz C
"""
import numpy

matriz_a = numpy.empty([3, 3])
matriz_b = numpy.empty([3, 3])
matriz_c = numpy.empty([3, 3])

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz_a[linha, coluna] = int(input(f'Informe os valores da Matriz A linha {linha} - colula {coluna}\n'))

print('#################')

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz_b[linha, coluna] = int(input(f'Informe os valores da Matriz B linha {linha} - colula {coluna}\n'))

for linha in range(0, 3):
    for colulna in range(0, 3):
        matriz_c[linha, coluna] = matriz_a[linha, coluna] + matriz_b[linha, coluna]
        print(matriz_c[linha, coluna])
