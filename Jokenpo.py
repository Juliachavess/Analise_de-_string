from random import randint
from time import sleep

jogada = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('0 Pedra; 1 Papel; 2 Tesoura')
voce = int(input('Digite a sua opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(2)
print('-=' * 11)
print(f'Computador jogou: {jogada[computador]}')
print(f'Você jogou: {jogada[voce]}')
print('-='*11)

if computador==0:
 if voce==0:
     print('Empate!')
 elif voce==1:
     print('Você venceu!')
 elif voce==2:
     print('Computador venceu!')
 else:
     print('Jogada Invalida')

if computador==1:
 if voce==1:
     print('Empate!')
 elif voce==0:
     print('Computador venceu!')
 elif voce==2:
     print('Você venceu!')
 else:
     print('Jogada Invalida')

if computador==2:
 if voce==2:
     print('Empate!')
 elif voce==0:
     print('Computador venceu!')
 elif voce==1:
     print('Você venceu!')
 else:
     print('Jogada Invalida')
