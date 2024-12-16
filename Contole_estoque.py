from Models.estoque import Estoque
from Models.Produtos_Models import Produtos

estoque = Estoque('estoque.db')

def obter_dados_produto():
    nome = input("Nome: ")
    quantidade = input("Quantidade: ")
    valor = input("Valor: ")
    return nome, quantidade, valor

def Add_produto():
    nome, quantidade, valor = obter_dados_produto()
    
    newProduto = Produtos()
    newProduto.set_prod(nome, quantidade, valor)

    if estoque.Add_Produto(newProduto.get_id(), newProduto.get_nome(), newProduto.get_quantidade(), newProduto.get_preco()):
        print(f"Produto adicionado: {newProduto.get_nome()}")
    else:
        print('Erro ao adicionar produto')

def Listar_produtos():
    produtos = estoque.listar_produtos()    
    if produtos:
        for produto in produtos:
            print(produto)
    else:
        print("Nenhum produto encontrado.")

def Buscar_produto():
    id = input("ID: ")
    produto = estoque.buscar_produto('produto', id)
    if produto:
        print(produto)
    else:
        print("Produto não encontrado.")

def Remover_produto():
    id = input("ID: ")
    if estoque.remover_produto('produto', id):
        print("Produto removido")
    else:
        print("Erro ao remover produto ou produto não encontrado.")

def Atualizar_produto():
    id = input("ID: ")
    nome, quantidade, valor = obter_dados_produto()

    newProduto = Produtos()
    newProduto.set_prod(nome, quantidade, valor)

    if estoque.atualizar_produto('produto', newProduto.get_prod(), id):
        print("Produto atualizado")
    else:
        print("Erro ao atualizar produto ou produto não encontrado.")

def Comprar_produto():
    id = input("ID: ")
    quantidade = input("Quantidade: ")
    if estoque.comprar_produto('produto', id, quantidade):
        print("Produto comprado")
    else:
        print("Erro ao comprar produto ou produto não encontrado.")

def Calcular_valor_total():
    total = estoque.calcular_valor_total()
    print(f"Valor total do estoque: {total}")
