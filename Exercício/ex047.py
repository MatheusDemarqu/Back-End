s = 0
cont = 0
for c in range(1,501,2):
  if c% 3 == 0:
      cont += 1 #conta as repetições
      s += c #soma os valores
print(f"A soma de todos os {cont} valores solicitados é {s}")
