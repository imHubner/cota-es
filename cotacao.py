import tkinter as tk
import requests

def obter_cotacao():
    moeda_digitada = moeda.get().strip().lower()
    if moeda_digitada == "dollar":
        # URL da API para obter a cotação do dólar
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        
        try:
            resposta = requests.get(url)
            dados = resposta.json()
            cotacao_dolar = dados['rates']['BRL']
            resultado_label.config(text=f"Cotação do dólar: R$ {cotacao_dolar:.2f}")
        except Exception as e:
            resultado_label.config(text="Erro ao obter a cotação.")
    else:
        resultado_label.config(text="Moeda não reconhecida.")

janela = tk.Tk()
janela.title("Cotação de Moedas")

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(janela, text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

mensagem2 = tk.Label(janela, text="Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

moeda = tk.Entry(janela)
moeda.grid(row=1, column=1)

buscar_button = tk.Button(janela, text="Buscar Cotação", command=obter_cotacao)
buscar_button.grid(row=2, column=0, columnspan=2)

resultado_label = tk.Label(janela, text="", fg='black')
resultado_label.grid(row=3, column=0, columnspan=2, sticky="NSEW")

janela.mainloop()