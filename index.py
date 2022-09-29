from random import choice

print('Digite seu nome:')
nome = str(input('R: ')).strip().title()
print(f'Seja bem vindo, {nome}! Vamos jogar Jokenpo? Você vai enfrentar o OXEbot!')
print('Você começa!')
print("""Escolha uma opção:
[1] PEDRA
[2] PAPEL
[3] TESOURA """)
opcao = int(input('R: '))
opc = opcao
lista = 'PEDRA', 'PAPEL', 'TESOURA'
oxeb = choice(lista)
jkp = 'PEDRA' > 'TESOURA' > 'PAPEL' > 'PEDRA'

from time import sleep

sleep(1)
print('JO!')
sleep(1)
print('KEN!')
sleep(1)
print('PO!')

print('-=' * 12)
if opc == 1:
    print(f'Você escolheu PEDRA')
elif opc == 2:
    print(f'Você escolheu PAPEL')
elif opc == 3:
    print(f'Você escolheu TESOURA')
print(f'OXEbot escolheu {oxeb}')
print('-=' * 12)

if oxeb == 'PEDRA':
    if opcao == 2:
        print(f'{nome} é o VENCEDOR! PARABÉNS!')
    elif opcao == 3:
        print('OXEbot é o VENCEDOR! SEU FRACASSADO!')
    elif opcao == 1:
        print('Deu EMPATE! Jogaram bem.')
    else:
        print('Jogada INVÁLIDA!')
elif oxeb == 'PAPEL':
    if opcao == 1:
        print('OXEbot é o VENCEDOR! SEU FRACASSADO!')
    elif opcao == 3:
        print(f'{nome} é o VENCEDOR! PARABÉNS!')
    elif opcao == 2:
        print('Deu EMPATE! Jogaram bem.')
    else:
        print('Jogada INVÁLIDA!')
elif oxeb == 'TESOURA':
    if opcao == 2:
        print('OXEbot é o VENCEDOR! SEU FRACASSADO!')
    elif opcao == 1:
        print(f'{nome} é o VENCEDOR! PARABÉNS!')
    elif opcao == 3:
        print('Deu EMPATE! Jogaram bem.')
    else:
        print('Jogada INVÁLIDA!')