dias = int(input("Quantos dias foi alugado"))
km = float(input("Quantos km foi percorrido "))
diaria = dias*60
percurso = km * 0.15
custo = percurso + diaria

print("O total a pagar é R$:{:.2f}" .format(custo))
