vel = float(input('Qual a sua velocidade? '))
if vel > 80:
    print('Excedeu o limite permitido de 80Km/h. Você foi multado em R${:.2f}'.format((vel-80)*7))
else:
    print('Viaje com segurança!')