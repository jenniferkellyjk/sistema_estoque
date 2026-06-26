# Sistema de Controle de Estoque e Vendas
# versao 1.0 - feito rapido pra entregar antes do prazo
# autor: equipe antiga


# Configuração do sistema
SENHA_ADMIN = "1234"  # (em produção viria de variável de ambiente)

LIMITE_DESCONTO_VENDA = 100
DESCONTO_VENDA = 0.10

LIMITE_DESCONTO_RELATORIO = 200
DESCONTO_RELATORIO = 0.15

LIMITE_ESTOQUE_BAIXO = 5

estoque_produtos = []


def adicionar_produto(nome_produto, preco, quantidade, historico_produtos=None):
    if historico_produtos is None:
        historico_produtos = []

    estoque_produtos.append({
        "nome": nome_produto,
        "preco": preco,
        "qtd": quantidade
    })

    historico_produtos.append(nome_produto)
    print("Produto Adicionado!")


def vender_produto(nome_produto, quantidade):
    for item_produto in estoque_produtos:
        if item_produto["nome"] == nome_produto:
            if item_produto["qtd"] >= quantidade:
                item_produto["qtd"] -= quantidade

                total = item_produto["preco"] * quantidade

                if total > LIMITE_DESCONTO_VENDA:
                    total -= total * DESCONTO_VENDA

                print("Venda realizada. Total: " + str(total))
                return total

            print("Estoque insuficiente")
            return 0

    print("Produto não encontrado")
    return 0


def calcular_total(preco, quantidade):
    total = preco * quantidade
    if total > LIMITE_DESCONTO_RELATORIO:               # limite diferente do usado em vender()
        total = total - total * DESCONTO_RELATORIO       # desconto diferente do usado em vender()
    return total


def listar_produtos():
    print("=== PRODUTOS ===")
    for item_produto in estoque_produtos:
        print(item_produto["nome"] + " - R$" + str(item_produto["preco"]) + " - qtd: " + str(item_produto["qtd"]))


def relatorio_estoque_baixo():
    print("=== ESTOQUE BAIXO ===")
    for item_produto in estoque_produtos:
        if item_produto["qtd"] < LIMITE_ESTOQUE_BAIXO:       
            print(item_produto["nome"] + " está com estoque baixo (" + str(item_produto["qtd"]) + ")")


def relatorio_vendas():
    # TODO: Implementação em breve. Em andamento.
    pass


def menu():
    while True:
        print("\n1-Cadastrar  2-Vender  3-Listar  4-Estoque baixo  5-Admin  0-Sair")
        opcao = input("Opcao: ")
        if opcao == "1":
            try:
                nome_produto = input("Nome: ")
                preco = float(input("Preco: "))
                quantidade = int(input("Qtd: "))
                adicionar_produto(nome_produto, preco, quantidade)
            except ValueError:
                    print("Entrada inválida! Preço e quantidade devem ser números. ")
        elif opcao == "2":
            try:
                nome_produto = input("Nome do produto: ")
                quantidade = int(input("Quantidade: "))
                vender_produto(nome_produto, quantidade)
            except ValueError:
                print("Entrada inválida! Quantidade deve ser número inteiro.")
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            relatorio_estoque_baixo()
        elif opcao == "5":
            senha = input("Senha: ")
            if senha == SENHA_ADMIN:
                print("Acesso liberado!")
            else:
                print("Senha errada.")
        elif opcao == "0":
            break
        else:
            print("Opcao invalida!")


menu()
