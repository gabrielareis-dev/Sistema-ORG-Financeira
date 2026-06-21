import sqlite3

class BancoDeDados:
    def __init__(self, nome_arquivo="financas.db"):
        self.nome_arquivo = nome_arquivo
        self.criar_tabelas()

    def conectar(self):
        """Abre uma conexão com o banco de dados SQLite."""
        return sqlite3.connect(self.nome_arquivo)

    def criar_tabelas(self):
        """Cria as tabelas do sistema se elas não existirem."""
        conexao = self.conectar()
        cursor = conexao.cursor()

        # Tabela para registrar a renda e os gastos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movimentacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL,
                tipo TEXT NOT NULL
            )
        """)

        # Tabela para gerenciar o cofrinho
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cofrinho (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valor_acumulado REAL NOT NULL
            )
        """)

        conexao.commit()
        conexao.close()

    def executar_comando(self, sql: str, parametros: tuple = ()):
        """Executa comandos de inserção, atualização ou deleção (INSERT, UPDATE, DELETE)."""
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(sql, parametros)
        conexao.commit()
        conexao.close()

    def consultar_dados(self, sql: str, parametros: tuple = ()):
        """Executa comandos de busca (SELECT) e retorna os dados."""
        conexao = self.conectar()
        cursor = conexao.cursor()
        cursor.execute(sql, parametros)
        dados = cursor.fetchall()
        conexao.close()
        return dados
    