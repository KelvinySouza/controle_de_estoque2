from Models.Database import BancoDeProdutos

class Produto:
    def _init_(self, nome='', quantidade=0, preco=0.0):
        """Inicializa um novo produto com nome, quantidade e preço."""
        self.__id = None
        self.__name = nome
        self.__quantidade = quantidade
        self.__preco = preco
        self.__db = BancoDeProdutos('estoque.db')

    def set_prod(self, nome, quantidade, preco):
        """Define os atributos do produto."""
        self.__name = nome
        self.__quantidade = quantidade
        self.__preco = preco

    def get_nome(self):
        """Retorna o nome do produto."""
        return self.__name

    def get_quantidade(self):
        """Retorna a quantidade do produto."""
        return self.__quantidade

    def get_preco(self):
        """Retorna o preço do produto."""
        return self.__preco

    def get_id(self):
        """Retorna o ID do produto."""
        return self.__id

    def set_id(self, id):
        """Define o ID do produto."""
        self.__id = id

    def _str_(self):
        """Retorna uma representação em string do produto."""
        return f'ID: {self._id}\nNome: {self.name}\nQuantidade: {self.quantidade}\nPreço: {self._preco}'

    def save(self):
        """Salva o produto no banco de dados."""
        values = {
            'name': self.__name,
            'quantidade': self.__quantidade,
            'preco': self.__preco
        }
        return self.__db.insert_values('produtos', values)

    def update(self):
        """Atualiza o produto no banco de dados."""
        if self.__id is None:
            raise ValueError("ID do produto não definido.")
        
        values = {
            'name': self.__name,
            'quantidade': self.__quantidade,
            'preco': self.__preco
        }
        condition = {
            'id': self.__id
        }
        return self.__db.update_values('produtos', values, condition)

    def delete(self):
        """Remove o produto do banco de dados."""
        if self.__id is None:
            raise ValueError("ID do produto não definido.")
        
        condition = {
            'id': self.__id
        }
        return self.__db.delete_values('produtos', condition)

    def load(self, id):
        """Carrega um produto do banco de dados pelo ID."""
        produto_data = self.__db.get_value_id('produtos', id)
        if produto_data:
            self._id, self.name, self.quantidade, self._preco = produto_data[0]
            return True
        return False
