# Sistema ORGF - Gerenciador Financeiro Pessoal

O **Sistema ORGF** é um aplicativo desktop desenvolvido em Python para controle e gerenciamento de finanças pessoais. Ele permite o registro de fluxos de caixa (rendas e despesas), monitoramento de saldos acumulados, gerenciamento de um cofrinho virtual para reserva de valores e simulações de metas financeiras de longo prazo.

O diferencial do projeto está na sua independência: após o empacotamento, o sistema roda diretamente no Windows como um executável autônomo, armazenando todas as informações localmente em um banco de dados embarcado, sem a necessidade de conexões externas ou internet.

---

## Estrutura e Arquitetura do Software

O desenvolvimento do sistema foi guiado pelos princípios de separação de responsabilidades, dividindo o código em três componentes principais que trabalham de forma independente:

* **Interface Gráfica (`interface_grafica.py`):** Construída com a biblioteca Tkinter, gerencia exclusivamente o visual do programa, captura as interações do usuário e exibe as respostas na tela. Ela não faz contas e não acessa o banco de dados diretamente.
* **Gerenciador Financeiro (`gerenciador.py`):** É o cérebro da aplicação. Concentra as regras de negócio, realiza os cálculos de saldo, simula o tempo necessário para atingir metas e formata os dados antes que eles sejam salvos ou exibidos.
* **Banco de Dados (`banco.py`):** Gerencia a persistência utilizando o SQLite. Cria as tabelas necessárias de forma automática no primeiro uso (`movimentacoes` e `cofrinho`) e executa os comandos SQL de inserção, consulta e exclusão.

---

## Funcionalidades Principais

* **Fluxo de Caixa:** Registro rápido de entradas (rendas) e saídas (despesas) com atualização automática do saldo em tempo real na tela.
* **Histórico Integrado:** Exibição de todos os lançamentos em uma tabela visual, permitindo a exclusão de registros antigos diretamente com cliques do mouse.
* **Reserva (Cofrinho):** Módulo dedicado para isolar parte do saldo disponível em uma poupança virtual, impedindo que esse valor seja contabilizado no saldo livre do dia a dia.
* **Simulador de Objetivos:** Ferramenta matemática que calcula em quantos meses o usuário atingirá uma meta financeira com base em um aporte mensal fixo.

---

## Tecnologias Utilizadas

* **Linguagem:** Python
* **Interface:** Tkinter (Interface nativa)
* **Banco de Dados:** SQLite (Arquivo local `.db`)
* **Empacotamento:** PyInstaller (Geração do executável `.exe`)

---

## Guia de Execução e Compilação do Projeto

Certifique-se de ter o Python instalado em sua máquina e execute a sequência de comandos abaixo no terminal para rodar o código-fonte ou gerar a versão executável:

```bash
# =====================================================================
# ALTERNATIVA A: EXECUTAR O PROJETO A PARTIR DO CÓDIGO-FONTE
# =====================================================================

# 1. Clone o repositório para sua máquina local
git clone https://github.com/gabrielareis-dev/Sistema-ORG-Financeira.git

# 2. Acesse a pasta do projeto
cd Sistema-ORGF

# 3. Crie o ambiente virtual (.venv)
python -m venv .venv

# 4. Ative o ambiente virtual no Windows
.venv\Scripts\activate

# 5. Instale todas as dependências necessárias
pip install -r requirements.txt

# 6. Execute o aplicativo principal
python main.py


# =====================================================================
# ALTERNATIVA B: DISTRIBUIÇÃO E EXECUÇÃO AUTÔNOMA (GERAR .EXE)
# =====================================================================

# 1. Com o ambiente virtual ativo e as dependências instaladas, compile o app:
pyinstaller --onefile --noconsole main.py

# Nota: O arquivo executável final será gerado dentro da pasta 'dist'.
# Ele pode ser renomeado para "Sistema Financeiro ORGF.exe" e movido para a Área
# de Trabalho, desde que mantido na mesma pasta do banco de dados (financas.db). 
