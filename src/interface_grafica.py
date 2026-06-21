import tkinter as tk
from tkinter import messagebox, ttk
import math
from src.gerenciador import GerenciadorFinanceiro

class InterfaceGrafica:
    def __init__(self, janela):
        self.gerenciador = GerenciadorFinanceiro()
        
        # Configurações da Janela Principal
        self.janela = janela
        self.janela.title("Sistema Financeiro ORGF - Completo")
        self.janela.geometry("600x700")
        self.janela.configure(bg="#f0f2f5")

        # --- Bloco de Saldo e Cofrinho ---
        self.frame_valores = tk.Frame(janela, bg="#ffffff", bd=1, relief="solid")
        self.frame_valores.pack(pady=15, fill="x", padx=20)

        self.lbl_saldo = tk.Label(self.frame_valores, text="Saldo Atual: R$ 0.00", font=("Arial", 14, "bold"), bg="#ffffff", fg="#2ecc71")
        self.lbl_saldo.pack(pady=3)

        self.lbl_cofrinho = tk.Label(self.frame_valores, text="No Cofrinho: R$ 0.00", font=("Arial", 12), bg="#ffffff", fg="#3498db")
        self.lbl_cofrinho.pack(pady=3)

        # --- Bloco 1: Entrada de Renda/Despesa ---
        self.frame_inputs = tk.LabelFrame(janela, text=" Adicionar Movimentação ", font=("Arial", 10, "bold"), bg="#f0f2f5", padx=10, pady=5)
        self.frame_inputs.pack(pady=10, padx=20, fill="x")

        tk.Label(self.frame_inputs, text="Descrição:", bg="#f0f2f5").grid(row=0, column=0, sticky="w", pady=2)
        self.txt_descricao = tk.Entry(self.frame_inputs, font=("Arial", 10), width=25)
        self.txt_descricao.grid(row=0, column=1, pady=2, padx=5)

        tk.Label(self.frame_inputs, text="Valor: R$", bg="#f0f2f5").grid(row=0, column=2, sticky="w", pady=2)
        self.txt_valor = tk.Entry(self.frame_inputs, font=("Arial", 10), width=12)
        self.txt_valor.grid(row=0, column=3, pady=2, padx=5)

        btn_renda = tk.Button(self.frame_inputs, text="+ Renda", bg="#2ecc71", fg="white", font=("Arial", 9, "bold"), command=self.adicionar_renda)
        btn_renda.grid(row=0, column=4, padx=5)

        btn_despesa = tk.Button(self.frame_inputs, text="- Despesa", bg="#e74c3c", fg="white", font=("Arial", 9, "bold"), command=self.adicionar_despesa)
        btn_despesa.grid(row=0, column=5, padx=5)

        # --- Bloco 2: Operações do Cofrinho ---
        self.frame_cofrinho_ops = tk.LabelFrame(janela, text=" Gerenciar Cofrinho ", font=("Arial", 10, "bold"), bg="#f0f2f5", padx=10, pady=5)
        self.frame_cofrinho_ops.pack(pady=10, padx=20, fill="x")

        tk.Label(self.frame_cofrinho_ops, text="Valor para Guardar: R$", bg="#f0f2f5").grid(row=0, column=0, sticky="w")
        self.txt_cofrinho_val = tk.Entry(self.frame_cofrinho_ops, font=("Arial", 10), width=15)
        self.txt_cofrinho_val.grid(row=0, column=1, padx=5)

        btn_guardar = tk.Button(self.frame_cofrinho_ops, text="Guardar", bg="#3498db", fg="white", font=("Arial", 9, "bold"), command=self.guardar_cofrinho)
        btn_guardar.grid(row=0, column=2, padx=5)

        btn_zerar = tk.Button(self.frame_cofrinho_ops, text="Zerar Cofrinho", bg="#95a5a6", fg="white", font=("Arial", 9, "bold"), command=self.zerar_cofrinho)
        btn_zerar.grid(row=0, column=3, padx=20)

        # --- Bloco 3: Simulador de Metas ---
        self.frame_simulador = tk.LabelFrame(janela, text=" Simulador de Meta ", font=("Arial", 10, "bold"), bg="#f0f2f5", padx=10, pady=5)
        self.frame_simulador.pack(pady=10, padx=20, fill="x")

        tk.Label(self.frame_simulador, text="Meta: R$", bg="#f0f2f5").grid(row=0, column=0, sticky="w")
        self.txt_meta = tk.Entry(self.frame_simulador, font=("Arial", 10), width=12)
        self.txt_meta.grid(row=0, column=1, padx=3)

        tk.Label(self.frame_simulador, text="Aporte Mensal: R$", bg="#f0f2f5").grid(row=0, column=2, sticky="w")
        self.txt_aporte = tk.Entry(self.frame_simulador, font=("Arial", 10), width=12)
        self.txt_aporte.grid(row=0, column=3, padx=3)

        btn_simular = tk.Button(self.frame_simulador, text="Simular", bg="#9b59b6", fg="white", font=("Arial", 9, "bold"), command=self.simular_meta)
        btn_simular.grid(row=0, column=4, padx=5)

        # --- Bloco 4: Tabela de Histórico e Exclusão ---
        self.frame_tabela = tk.Frame(janela, bg="#f0f2f5")
        self.frame_tabela.pack(pady=10, padx=20, fill="both", expand=True)

        tk.Label(self.frame_tabela, text="Histórico de Movimentações:", font=("Arial", 10, "bold"), bg="#f0f2f5").pack(anchor="w")
        
        self.tabela = ttk.Treeview(self.frame_tabela, columns=("ID", "Tipo", "Descrição", "Valor"), show="headings", height=8)
        self.tabela.heading("ID", text="ID")
        self.tabela.heading("Tipo", text="Tipo")
        self.tabela.heading("Descrição", text="Descrição")
        self.tabela.heading("Valor", text="Valor")
        
        self.tabela.column("ID", width=40, anchor="center")
        self.tabela.column("Tipo", width=80, anchor="center")
        self.tabela.column("Descrição", width=220)
        self.tabela.column("Valor", width=100, anchor="e")
        self.tabela.pack(pady=5, fill="both", expand=True)

        # Botão de Excluir Registro Selecionado
        btn_excluir = tk.Button(janela, text="❌ Excluir Item Selecionado", bg="#e74c3c", fg="white", font=("Arial", 10, "bold"), command=self.excluir_selecionado)
        btn_excluir.pack(pady=10)

        # Carrega os dados iniciais na tela
        self.atualizar_tela()

    def atualizar_tela(self):
        """Atualiza saldos e recarrega a tabela de histórico."""
        saldo = self.gerenciador.calcular_saldo()
        cofrinho = self.gerenciador.obter_saldo_cofrinho()
        
        self.lbl_saldo.config(text=f"Saldo Atual: R$ {saldo:.2f}")
        self.lbl_saldo.config(fg="#e74c3c" if saldo < 0 else "#2ecc71")
        self.lbl_cofrinho.config(text=f"No Cofrinho: R$ {cofrinho:.2f}")

        for linha in self.tabela.get_children():
            self.tabela.delete(linha)

        historico = self.gerenciador.obter_historico()
        for item in historico:
            self.tabela.insert("", "end", values=(item[0], item[3], item[1], f"R$ {item[2]:.2f}"))

    def adicionar_renda(self):
        try:
            desc = self.txt_descricao.get()
            val = float(self.txt_valor.get())
            if not desc: raise ValueError
            self.gerenciador.adicionar_movimentacao(desc, val, "Renda")
            self.txt_descricao.delete(0, tk.END)
            self.txt_valor.delete(0, tk.END)
            self.atualizar_tela()
        except ValueError:
            messagebox.showerror("Erro", "Insira uma descrição e um valor numérico válido.")

    def adicionar_despesa(self):
        try:
            desc = self.txt_descricao.get()
            val = float(self.txt_valor.get())
            if not desc: raise ValueError
            self.gerenciador.adicionar_movimentacao(desc, val, "Despesa")
            self.txt_descricao.delete(0, tk.END)
            self.txt_valor.delete(0, tk.END)
            self.atualizar_tela()
        except ValueError:
            messagebox.showerror("Erro", "Insira uma descrição e um valor numérico válido.")

    def guardar_cofrinho(self):
        try:
            val = float(self.txt_cofrinho_val.get())
            sucesso, msg = self.gerenciador.guardar_no_cofrinho(val)
            if sucesso:
                self.txt_cofrinho_val.delete(0, tk.END)
                self.atualizar_tela()
                messagebox.showinfo("Cofrinho", msg)
            else:
                messagebox.showwarning("Aviso", msg)
        except ValueError:
            messagebox.showerror("Erro", "Insira um valor numérico válido para o cofrinho.")

    def zerar_cofrinho(self):
        if messagebox.askyesno("Confirmar", "Tem certeza que deseja esvaziar o cofrinho?"):
            sucesso, msg = self.gerenciador.esvaziar_cofrinho()
            self.atualizar_tela()
            messagebox.showinfo("Sucesso", msg)

    def simular_meta(self):
        try:
            meta = float(self.txt_meta.get())
            aporte = float(self.txt_aporte.get())
            res = self.gerenciador.simular_objetivo(meta, aporte)
            
            if res["ja_conquistado"]:
                messagebox.showinfo("Meta", "🎉 Parabéns! Você já atingiu esse valor com o saldo atual do seu cofrinho!")
            else:
                msg = f"🎯 Objetivo: R$ {meta:.2f}\n"
                msg += f"💸 Falta economizar: R$ {res['falta_economizar']:.2f}\n"
                if res["meses_necessarios"] == float('inf'):
                    msg += "⏳ Guardando R$ 0.00 você não alcançará a meta."
                else:
                    msg += f"⏳ Tempo estimado: {math.ceil(res['meses_necessarios'])} mês(es)"
                messagebox.showinfo("Resultado da Simulação", msg)
        except ValueError:
            messagebox.showerror("Erro", "Insira valores numéricos válidos para a simulação.")

    def excluir_selecionado(self):
        # Pega a linha que o usuário clicou com o mouse na tabela
        item_selecionado = self.tabela.selection()
        if not item_selecionado:
            messagebox.showwarning("Aviso", "Por favor, clique em uma movimentação da lista para excluí-la!")
            return
            
        # Pega os dados da linha clicada
        valores = self.tabela.item(item_selecionado, "values")
        id_excluir = int(valores[0]) # O ID fica na primeira coluna
        
        if messagebox.askyesno("Confirmar Exclusão", f"Deseja mesmo excluir o item de ID {id_excluir}?"):
            sucesso, msg = self.gerenciador.excluir_movimentacao(id_excluir)
            self.atualizar_tela()
            messagebox.showinfo("Sucesso", msg) 