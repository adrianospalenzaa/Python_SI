"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores,
 o voto de cada eleitor e ,ao final, mostre o número de votos de cada candidato.
"""
voto1 = 0
voto2 = 0
voto3 = 0
def cont_voto(voto1, voto2, voto3):
    print(f'Candidato 1: {voto1}')
    print(f'Candidato 2: {voto2}')
    print(f'Candidato 3: {voto3}')
votos = int(input('Digite o número de eleitores: '))
for i in range(votos):
    voto = int(input('Digite o voto: '))
    if voto == 1:
        voto1 += 1
    elif voto == 2:
        voto2 += 1
    elif voto == 3:
        voto3 += 1
cont_voto(voto1, voto2, voto3)
