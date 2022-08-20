"""
5. Leia o vetor nomes e o vetor notas, nos quais devem ser informados os
nomes dos alunos e as notas, respectivamente em cada vetor. Ao final,
mostrar o nome do aluno e sua nota
"""
import numpy

v_nome = numpy.empty(2, dtype=object)
v_nota = numpy.empty(2)

for posicao in range(0, 2):
    v_nome[posicao] = input(f'Digite nome do aluno {posicao + 1}.\n')
    v_nota[posicao] = float(input(f'Digite nota do aluno {posicao + 1}.\n'))
for posicao in range(0, 2):
    print(f'{v_nome[posicao]} - {v_nota[posicao]}')
