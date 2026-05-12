velocidade = float(input('Digite a velocidade do seu carro: '))

multa = (velocidade - 80) * 7


if velocidade > 80:
    print('ACIMA DA VELOCIDADE')
    print('\n')
    print('Você foi multado em R$ {}'.format(multa))
else:
    print('Dentro do Limite')
