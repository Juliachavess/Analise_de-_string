nome = input ("Qual é o seu nome?")
altura = float(input ("Qual é a sua altura?"))
peso = float(input ("Qual é o seu peso?"))
imc = peso/(altura*altura)
print('{} seu IMC é: {:.2f}'.format(nome,imc))
if imc <17:
    print('Muito abaixo do peso!')
elif imc < 18.49:
    print('Abaixo do peso!')
elif imc <24.99:
    print('Peso normal!')
elif imc <29.99:
    print('Acima do peso!')
elif imc < 34.99:
    print('Obesidade!')
else:
    print('Obesidade morbida!')
