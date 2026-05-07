cidade = str(input('Digite o nome de uma cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')

cidade = str(input('Digite o nome de uma cidade: ')).strip()
esplitado = cidade.split()

print(esplitado[0].upper() == 'SANTO')
