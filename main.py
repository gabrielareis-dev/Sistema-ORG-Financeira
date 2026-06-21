import tkinter as tk
from src.interface_grafica import InterfaceGrafica

if __name__ == "__main__":
    # Cria a janela principal do Windows/Mac
    raiz = tk.Tk()
    
    # Passa a janela para a nossa classe construir o layout
    app = InterfaceGrafica(raiz)
    
    # Mantém a janela aberta e escutando os cliques de botão
    raiz.mainloop()