"""
2. Leia um vetor A de 10 elementos inteiros e um valor individual X. A seguir,
imprimir “Achei” se o valor X existir em A e “Não achei” caso contrário
"""
import numpy

vetor_A = numpy.empty(5)

for contador in range(0, 5):
    vetor_A[contador] = int(input(f'Digite o valor interiro {contador + 1}\n'))
pesquisa = int(input('Digite o valor para pesquisa\n'))

achei = False
for contador in range(0, 5):
    if vetor_A[contador] == pesquisa and achei == False:
        achei = True
        print('"ACHEI"')
if achei == False:
    print('"NÃO ACHEI"')
