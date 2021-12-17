casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
ano = int(input('Em quantos anos você quer pagar? '))
prestacao = casa / (ano * 12)
if prestacao >= salario * 0.30:
    print('Empréstimo NEGADO, sua prestação está em R${:.2f} e é mais de 30% do seu salário'.format(prestacao))
else:
    print('Emprestimo APROVADO, sua prestação será de R${:.2f}'.format(prestacao))
