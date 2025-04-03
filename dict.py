produtos = {
    "calca": {"Categoria": "Roupas", "preco":1200.00,"estoque":15,"em_promocao": False},

    "tenis": {"Categoria": "Sapato", "preco": 600.00,"estoque":8, "em_promocao": True},

    "camisa": {"Categoria": "Camisa", "preco":100.00,"estoque":10, "em_promocao": False},

    "shorts": {"Categoria": "Bermuda", "preco":50.00,"estoque":5, "em_promocao": True},

    "bone": {"Categoria": "Bones", "preco":20.00,"estoque":10, "em_promocao": True}
}

for produto in produtos:
    print(produto)

nome = input("Ver estoque de:")
print(produtos[nome]["estoque"])

preco = input("Digite o produto para ver o preço:")
print(produtos[preco]["preco"])


for produto in produtos:
    if produtos[produto]["em_promocao"] == False:
        print(f"{produto} nao esta em promocao")

    elif produtos[produto]["em_promocao"] == True:
        print(f"{produto} ESTA EM PROMOÇÃO!!!")










    