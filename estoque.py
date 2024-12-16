from Models.Produtos_Models import Produtos

class Estoque(Produtos):
    def _init_(self, bd):
        super()._init_(bd)
        self.__table_name = 'produto'
        self.__columns = {
            'id': 'Text',
            'name': 'Text',
            'quantidade': 'int',
            'value': 'real'
        }
        self.create_table(self._table_name, self._columns)

    def add_produto(self, id, nome, quantidade, valor):
        """Adiciona um novo produto ao estoque."""
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        if valor < 0:
            raise ValueError("O valor não pode ser negativo.")

        produto = {
            'values': {
                'id': id,
                'name': nome,
                'quantidade': quantidade,
                'value': valor
            }
        }

        return self.insert_values(self.__table_name, produto['values'])

    def listar_produtos(self):
        """Lista todos os produtos no estoque."""
        return self.get_all(self.__table_name)

    def atualizar_produto(self, values, condition):
        """Atualiza as informações de um produto existente."""
        return self.update_values(self.__table_name, values, condition)

    def remover_produto(self, condition):
        """Remove um produto do estoque com base na condição fornecida."""
        return self.delete_values(self.__table_name, condition)

    def buscar_produto(self, id):
        """Busca um produto pelo ID."""
        return self.get_value_id(self.__table_name, id)

    def calcular_valor_total(self):
        """Calcula o valor total dos produtos em estoque."""
        return self.get_value(self.__table_name, {'where': 'quantidade > 0'})

    def verificar_produto_existe(self, id):
        """Verifica se um produto existe no estoque."""
        produto = self.buscar_produto(id)
        return produto is not None