import random
numero = random.randint(0,5)
print('Adivinhe um número de 0 a 5.')
usuario = int(input('Adivinhe o número:'))
if usuario == numero:
    print('Você venceu')
else:
    print('Você perdeu!')
print('FIM')