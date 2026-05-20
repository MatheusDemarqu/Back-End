valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

meses = anos * 12
prestacao = valor_casa / meses
limite = salario * 0.30

print(f'\nPara pagar uma casa de R$ {valor_casa:.2f} em {anos} anos,', end=' ')
print(f'a prestação será de R$ {prestacao:.2f}.')

if prestacao <= limite:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO! A prestação excede 30% do salário.')
