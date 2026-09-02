maior = homens = mulheres = 0
while True:
    print('-=-'*30)
    print(f'CADASTRE UMA PESSOA')
    print('-=-'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [m/f]')).strip().lower()[0]
    continuar = str(input('Quer continuar? [s/n]')).strip().lower()[0]
    if idade > 18:
        maior += 1
    if sexo in 'm':
        homens += 1
    if sexo in 'f' and idade < 20:
        mulheres += 1
    if continuar in 'n':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} cadastrados')
print(f'E temos {mulheres} com menos de 20 anos')
