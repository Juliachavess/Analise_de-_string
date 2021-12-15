km = float(input('Qual a distância da sua viajem? '))
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print('Sua viagem de {}Km vai custar R${:.2f}'.format(km,preço))
