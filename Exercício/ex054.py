soma_idade = 0
maior = 0
cont_mulheres = 0
senhor = "Nenhum homem registrado"

for c in range(1, 5):
    print("-" * 5 + f" {c}ª pessoa " + "-" * 5)
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    
    soma_idade += idade  
    if sexo == "M":
        if c == 1 or idade > maior:
            maior = idade
            senhor = nome
    if sexo == "F" and idade < 20:
        cont_mulheres += 1
media = soma_idade / 4

print(f"A média de idade do grupo é de {media:.1f} anos.")
print(f"O homem mais velho tem {maior} anos e se chama {senhor}.")
print(f"Ao todo são {cont_mulheres} mulheres com menos de 20 anos.")
