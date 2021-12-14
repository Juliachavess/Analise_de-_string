import math
oposto = float(input('Digite o cateto oposto: '))
adj = float(input('Digite o cateto adjacente:'))
## se não importar pode usar - hi = (oposto ** 2 + adj **2 ) ** (1/2)
hi = math.hypot(oposto,adj)
print ('A hipotenunsa é {:.2f}'.format(hi))
