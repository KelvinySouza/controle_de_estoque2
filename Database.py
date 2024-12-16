import sqlite3

class BancoDeProdutos:
    def _init_(self, bd):
        self.__conn = sqlite3.connect(bd)
        self._cursor = self._conn.cursor()

    def create_table(self, table, columns):
        """Cria uma tabela no banco de dados se não existir."""
        key = ', '.join(f'{col} {type_}' for col, type_ in columns.items())
        query = f'CREATE TABLE IF NOT EXISTS {table} ({key})'

        try:
            self.__cursor.execute(query)
            self.__conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")
            return False

    def get_all(self, table):
        """Retorna todos os registros de uma tabela."""
        self.__cursor.execute(f'SELECT * FROM {table}')
        return self.__cursor.fetchall()

    def get_value_id(self, table, id):
        """Retorna um registro com base no ID."""
        self.__cursor.execute(f'SELECT * FROM {table} WHERE id = ?', (id,))
        return self.__cursor.fetchall()

    def get_value(self, table, condition):
        """Retorna registros com base em uma condição."""
        where_clause = ' AND '.join(f'{key} = ?' for key in condition.keys())
        query = f'SELECT * FROM {table} WHERE {where_clause}' if where_clause else f'SELECT * FROM {table}'

        self.__cursor.execute(query, tuple(condition.values()))
        return self.__cursor.fetchall()

    def insert_values(self, table, values):
        """Insere um novo registro na tabela."""
        keys = ', '.join(values.keys())
        placeholders = ', '.join('?' for _ in values)

        query = f'INSERT INTO {table} ({keys}) VALUES ({placeholders})'

        try:
            self.__cursor.execute(query, tuple(values.values()))
            self.__conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao inserir valores: {e}")
            return False

    def update_values(self, table, values, condition):
        """Atualiza registros na tabela com base em uma condição."""
        set_clause = ', '.join(f'{key} = ?' for key in values.keys())
        where_clause = ' AND '.join(f'{key} = ?' for key in condition.keys())

        query = f'UPDATE {table} SET {set_clause} WHERE {where_clause}'

        try:
            self.__cursor.execute(query, tuple(values.values()) + tuple(condition.values()))
            self.__conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao atualizar valores: {e}")
            return False

    def delete_values(self, table, condition):
        """Remove registros da tabela com base em uma condição."""
        where_clause = ' AND '.join(f'{key} = ?' for key in condition.keys())
        query = f'DELETE FROM {table} WHERE {where_clause}'

        try:
            self.__cursor.execute(query, tuple(condition.values()))
            self.__conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao deletar valores: {e}")
            return False

    def close(self):
        """Fecha a conexão com o banco de dados."""
        self.__conn.close()