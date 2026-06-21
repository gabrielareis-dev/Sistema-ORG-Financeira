from src.banco_de_dados import BancoDeDados

class GerenciadorFinanceiro:
    def __init__(self):
        # Cria o elo com o nosso motor do banco de dados
        self.db = BancoDeDados()

    def adicionar_movimentacao(self, descricao: str, valor: float, tipo: str):
        """Registra uma Renda ou uma Despesa no banco de dados."""
        sql = """
            INSERT INTO movimentacoes (descricao, valor, tipo)
            VALUES (?, ?, ?)
        """
        # O Python passa os dados de forma segura através de uma tupla
        self.db.executar_comando(sql, (descricao, valor, tipo))

    def obter_historico(self):
        """Busca todas as movimentações registradas no banco."""
        sql = "SELECT id, descricao, valor, tipo FROM movimentacoes ORDER BY id DESC"
        return self.db.consultar_dados(sql)

    def calcular_saldo(self):
        """Calcula o saldo atual (Total de Rendas - Total de Despesas)."""
        sql_renda = "SELECT SUM(valor) FROM movimentacoes WHERE tipo = 'Renda'"
        sql_despesa = "SELECT SUM(valor) FROM movimentacoes WHERE tipo = 'Despesa'"

        # Busca os totais do banco
        resultado_renda = self.db.consultar_dados(sql_renda)
        resultado_despesa = self.db.consultar_dados(sql_despesa)

        # Trata os valores caso o banco ainda esteja vazio (None)
        total_renda = resultado_renda[0][0] if resultado_renda[0][0] is not None else 0.0
        total_despesa = resultado_despesa[0][0] if resultado_despesa[0][0] is not None else 0.0

        # Retorna a matemática simples: o que entrou menos o que saiu
        return total_renda - total_despesa

    def excluir_movimentacao(self, id_movimentacao: int):
        """Exclui uma movimentação do banco de dados pelo ID."""
        sql_verificar = "SELECT id FROM movimentacoes WHERE id = ?"
        existe = self.db.consultar_dados(sql_verificar, (id_movimentacao,))
        
        if not existe:
            return False, "ID não encontrado no histórico!"
        
        sql_deletar = "DELETE FROM movimentacoes WHERE id = ?"
        self.db.executar_comando(sql_deletar, (id_movimentacao,))
        return True, "Movimentação excluída com sucesso!"

    def guardar_no_cofrinho(self, valor: float):
        """Adiciona um valor ao cofrinho se houver saldo suficiente."""
        saldo_atual = self.calcular_saldo()
        
        if valor > saldo_atual:
            return False, "Saldo insuficiente para guardar no cofrinho!"

        # Se houver saldo, primeiro tiramos o dinheiro das movimentações (como uma despesa de cofrinho)
        self.adicionar_movimentacao("Guardado no Cofrinho", valor, "Despesa")

        # Depois, atualizamos o total acumulado na tabela do cofrinho
        sql_atualizar = """
            INSERT INTO cofrinho (valor_acumulado) 
            VALUES (?)
        """
        self.db.executar_comando(sql_atualizar, (valor,))
        return True, f"R$ {valor:.2f} guardados com sucesso!"

    def obter_saldo_cofrinho(self):
        """Retorna o valor total acumulado dentro do cofrinho."""
        sql = "SELECT SUM(valor_acumulado) FROM cofrinho"
        resultado = self.db.consultar_dados(sql)
        return resultado[0][0] if resultado[0][0] is not None else 0.0
    
    def simular_objetivo(self, valor_objetivo: float, valor_mensal: float):
        """Calcula o que falta economizar e em quantos meses chega ao objetivo."""
        saldo_cofrinho_atual = self.obter_saldo_cofrinho()
        
        # Se o usuário já tem o dinheiro no cofrinho
        if saldo_cofrinho_atual >= valor_objetivo:
            return {
                "falta_economizar": 0.0,
                "meses_necessarios": 0,
                "ja_conquistado": True
            }
            
        # Calcula quanto ainda falta juntar
        falta_economizar = valor_objetivo - saldo_cofrinho_atual
        
        # Evita divisão por zero se a pessoa digitar que vai guardar R$ 0 por mês
        if valor_mensal <= 0:
            meses = float('inf') # Infinitos meses
        else:
            meses = falta_economizar / valor_mensal
            
        return {
            "falta_economizar": falta_economizar,
            "meses_necessarios": meses,
            "ja_conquistado": False
        }
    
    def esvaziar_cofrinho(self):
        """Apaga todos os registros do cofrinho, zerando o valor acumulado."""
        # Remove tudo da tabela cofrinho
        sql = "DELETE FROM cofrinho"
        self.db.executar_comando(sql)
        return True, "Cofrinho esvaziado com sucesso! Saldo do cofrinho zerado."