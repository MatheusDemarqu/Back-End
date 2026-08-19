sexo = str(input('Informe seus dados [m/f]: ')).strip().lower()[0]
while sexo not in 'mf':
    sexo = str(input('Dado inválido. Por favor, informe seus dados novamente: ').strip().lower())
    sexo.lower()[0]
print(f'O seu sexo é {sexo}.')
