# Sistema de Controle de Estoque e Vendas
# versao 1.0 - feito rapido pra entregar antes do prazo
# autor: equipe antiga


SENHA_ADMIN = "1234" 

produtos = []


def add(nome, preco, quantidade, hist=[]):
    produtos.append({"nome": nome, "preco": preco, "qtd": quantidade})
    hist.append(nome)
    print("Produto adicionado!")


def vender(nome, quantidade):
    for i in range(len(produtos)):
        if produtos[i]["nome"] == nome:
            if produtos[i]["qtd"] >= quantidade:
                produtos[i]["qtd"] = produtos[i]["qtd"] - quantidade
                total = produtos[i]["preco"] * quantidade
                # desconto pra compras acima de R$100.
                if total > 100:
                    total = total - total * 0.1
                print("Venda realizada. Total: " + str(total))
                return total
            else:
                print("Estoque insuficiente")
                return 0
    print("Produto nao encontrado")
    return 0


def calcular_total(preco, quantidade):
    total = preco * quantidade
    if total > 200:                 # limite diferente do usado em vender()
        total = total - total * 0.15        # desconto diferente do usado em vender()
    return total


def listar():
    print("=== PRODUTOS ===")
    for produto in produtos:
        print(produto["nome"] + " - R$" + str(produto["preco"]) + " - qtd: " + str(produto["qtd"]))


def relatorio_estoque_baixo():
    print("=== ESTOQUE BAIXO ===")
    for produto in produtos:
        if produto["qtd"] < 5:       
            print(produto["nome"] + " está com estoque baixo (" + str(produto["qtd"]) + ")")


def relatorio_vendas():
    # TODO: implementar de verdade
    pass


def menu():
    while True:
        print("\n1-Cadastrar  2-Vender  3-Listar  4-Estoque baixo  5-Admin  0-Sair")
        opcao = input("Opcao: ")
        if opcao == "1":
            nome = input("Nome: ")
            preco = float(input("Preco: "))
            quantidade = int(input("Qtd: "))
            add(nome, preco, quantidade)
        elif opcao == "2":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            vender(nome, quantidade)
        elif opcao == "3":
            listar()
        elif opcao == "4":
            relatorio_estoque_baixo()
        elif opcao == "5":
            senha = input("Senha: ")
            if senha == SENHA_ADMIN:
                print("Acesso liberado")
            else:
                print("Senha errada")
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")


menu()
