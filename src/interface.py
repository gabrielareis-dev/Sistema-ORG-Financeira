from src.gerenciador import GerenciadorFinanceiro
import math # Importado para arredondar os meses para cima, ex: 2.3 meses viram 3 meses

class InterfaceUsuario:
    def __init__(self):
        self.gerenciador = GerenciadorFinanceiro()

    def mostrar_menu(self):
        while True:
            print("\n" + "="*30)
            print("     SISTEMA FINANCEIRO ORGF     ")
            print("="*30)
            print(f" Saldo Atual: R$ {self.gerenciador.calcular_saldo():.2f}")
            print(f" No Cofrinho: R$ {self.gerenciador.obter_saldo_cofrinho():.2f}")
            print("-"*30)
            print("1. Adicionar Renda")
            print("2. Adicionar Despesa")
            print("3. Ver Histórico de Movimentações")
            print("4. Guardar dinheiro no Cofrinho")
            print("5. Excluir Movimentação")
            print("6. Simulador de Meta (Cofrinho)")
            print("7. Esvaziar/Zerar Cofrinho")  # <-- NOVA LINHA NO MENU
            print("0. Sair")
            print("="*30)

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                desc = input("Descrição da Renda: ")
                val = float(input("Valor: R$ "))
                self.gerenciador.adicionar_movimentacao(desc, val, "Renda")
                print(" Renda adicionada!")

            elif opcao == "2":
                desc = input("Descrição da Despesa: ")
                val = float(input("Valor: R$ "))
                self.gerenciador.adicionar_movimentacao(desc, val, "Despesa")
                print(" Despesa adicionada!")

            elif opcao == "3":
                print("\n" + "-"*40)
                print("       HISTÓRICO DE MOVIMENTAÇÕES")
                print("-"*40)
                historico = self.gerenciador.obter_historico()
                if not historico:
                    print("Nenhuma movimentação encontrada no banco.")
                else:
                    for item in historico:
                        print(f"ID: {item[0]:<3} | [{item[3]:<7}] {item[1]:<20} | R$ {item[2]:.2f}")
                    print("-" * 40)

            elif opcao == "4":
                val = float(input("Quanto deseja guardar no cofrinho? R$ "))
                sucesso, mensagem = self.gerenciador.guardar_no_cofrinho(val)
                print(f"\n {mensagem}")

            elif opcao == "5":
                print("\n--- EXCLUIR MOVIMENTAÇÃO ---")
                try:
                    id_excluir = int(input("Digite o ID da movimentação que deseja excluir: "))
                    sucesso, mensagem = self.gerenciador.excluir_movimentacao(id_excluir)
                    print(f"\n {mensagem}")
                except ValueError:
                    print("Por favor, digite um número válido para o ID.")

            elif opcao == "6":  
                print("\n--- SIMULADOR DE META DO COFRINHO ---")
                meta = float(input("Qual o valor total do seu objetivo? R$ "))
                aporte = float(input("Quanto você pode guardar por mês? R$ "))
                
                resultado = self.gerenciador.simular_objetivo(meta, aporte)
                
                print("\n" + "-"*35)
                if resultado["ja_conquistado"]:
                    print("🎉 Parabéns! Você já tem esse valor no cofrinho!")
                else:
                    print(f"🎯 Para chegar em R$ {meta:.2f}:")
                    print(f"💸 Falta economizar: R$ {resultado['falta_economizar']:.2f}")
                    
                    if resultado["meses_necessarios"] == float('inf'):
                        print("⏳ Guardando R$ 0.00 por mês você nunca alcançará a meta!")
                    else:
                        meses_finais = math.ceil(resultado["meses_necessarios"])
                        print(f"⏳ Tempo estimado: {meses_finais} mês(es)")
                print("-"*35)

            elif opcao == "7":  # <-- NOVO BLOCO PARA ZERAR COFRINHO
                print("\n⚠️ TEM CERTEZA QUE DESEJA ZERAR O COFRINHO?")
                confirmar = input("Digite 'S' para confirmar ou qualquer outra tecla para cancelar: ").upper()
                if confirmar == "S":
                    sucesso, mensagem = self.gerenciador.esvaziar_cofrinho()
                    print(f"\n {mensagem}")
                else:
                    print("\nAção cancelada.")

            elif opcao == "0":
                print("Saindo do sistema... Até logo!")
                break
            else:
                print("Opção inválida! Tente novamente.")