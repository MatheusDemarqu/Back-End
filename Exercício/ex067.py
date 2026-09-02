# Inicialização das variáveis de controle
total_gasto = 0
produtos_mais_de_1000 = 0
menor_preco = 0
produto_mais_barato = ""
contador = 0

while True:
    print("-" * 30)
    nome_produto = input("Nome do produto: ").strip()
    preco = float(input("Preço: R$ "))
    contador += 1
    
    # a) Acumula o valor total gasto
    total_gasto += preco
    
    # b) Conta quantos produtos custam mais de R$ 1000
    if preco > 1000:
        produtos_mais_de_1000 += 1
        
    # c) Descobre o nome do produto mais barato
    if contador == 1 or preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = nome_produto
        
    # Pergunta se o usuário deseja continuar e valida a resposta
    resposta = " "
    while resposta not in "SN":
        resposta = input("Quer continuar? [S/N] ").strip().upper()[0]
        
    if resposta == "N":
        break

print("-" * 30)
print(f"{" FIM DO PROGRAMA ":^30}")
print("-" * 30)

# Exibição dos resultados finais
print(f"a) O total gasto na compra foi: R$ {total_gasto:.2f}")
print(f"b) Quantidade de produtos que custam mais de R$ 1000: {produtos_mais_de_1000}")
print(f"c) O produto mais barato foi '{produto_mais_barato}' que custou R$ {menor_preco:.2f}")
