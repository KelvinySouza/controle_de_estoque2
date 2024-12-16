from Models.Database import BancoDeProdutos
from Models.Produtos_Models import Produtos
from Models.estoque import Estoque

def adicionar_produto(estoque):
    nome = input("Nome: ")
    quantidade = int(input("Quantidade: "))
    valor = float(input("Valor: "))

    newProduto = Produtos()
    newProduto.set_prod(nome, quantidade, valor)

    if estoque.add_produto(newProduto.get_id(), newProduto.get_nome(), newProduto.get_quantidade(), newProduto.get_preco()):
        print("Produto adicionado:", newProduto.get_nome())
    else:
        print('Erro ao adicionar produto')

def remover_produto(estoque):
    id = input("Id: ")
    if estoque.remover_produto(id):
        print("Produto removido com sucesso.")
    else:
        print("Erro ao remover produto.")

def atualizar_produto(estoque):
    id = input("Id: ")
    nome = input("Nome: ")
    quantidade = int(input("Quantidade: "))
    valor = float(input("Valor: "))
    values = {
        'name': nome,
        'quantidade': quantidade,
        'value': valor
    }
    if estoque.atualizar_produto(values, f"id = '{id}'"):
        print("Produto atualizado com sucesso.")
    else:
        print("Erro ao atualizar produto.")

def listar_produtos(estoque):
    produtos = estoque.listar_produtos()
    for produto in produtos:
        print(produto)
    if not produtos:
        print("Nenhum produto encontrado.")

def buscar_produto(estoque):
    id = input("Id: ")
    produto = estoque.buscar_produto(id)
    if produto:
        print(produto)
    else:
        print("Produto não encontrado.")

def main():
    estoque = Estoque('estoque.db')
    banco = BancoDeProdutos('estoque.db')

    while True:
        print('''\033[32m
        ################################################################
        # ███████╗███████╗████████╗ ██████╗  ██████╗ ██╗   ██╗███████╗ #
        # ██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║   ██║██╔════╝ #
        # █████╗  ███████╗   ██║   ██║   ██║██║   ██║██║   ██║█████╗   #
        # ██╔══╝  ╚════██║   ██║   ██║   ██║██║▄▄ ██║██║   ██║██╔══╝   #
        # ███████╗███████║   ██║   ╚██████╔╝╚██████╔╝╚██████╔╝███████╗ #
        # ╚══════╝╚══════╝   ╚═╝    ╚═════╝  ╚══▀▀═╝  ╚═════╝ ╚══════╝ #
        ################################################################ \033[0m''')
        print("Menu:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Atualizar produto")
        print("4. Listar produtos")
        print("5. Buscar produto")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '0':
            break

        match escolha:
            case '1':
                adicionar_produto(estoque)
            case '2':
                remover_produto(estoque)
            case '3':
                atualizar_produto(estoque)
            case '4':
                listar_produtos(estoque)
            case '5':
                buscar_produto(estoque)