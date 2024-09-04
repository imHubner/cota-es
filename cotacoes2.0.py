import tkinter as tk
import requests

def obter_cotacao():
    moeda_digitada = moeda.get().strip().lower()
    if moeda_digitada == "dollar":
        url = "https://api.exchangerate-api.com/v4/latest/USD"
    elif moeda_digitada == "euro":
        url = "https://api.exchangerate-api.com/v4/latest/EUR"
    elif moeda_digitada == "libra":
        url = "https://api.exchangerate-api.com/v4/latest/GBP"
    elif moeda_digitada == "iene":
        url = "https://api.exchangerate-api.com/v4/latest/JPY"
    else:
        resultado_label.config(text="Moeda não reconhecida.")
        return

    try:
        resposta = requests.get(url)
        dados = resposta.json()
        if moeda_digitada == "dollar":
            cotacao = dados['rates']['BRL']
            resultado_label.config(text=f"Cotação do dólar: R$ {cotacao:.2f}")
        elif moeda_digitada == "euro":
            cotacao = dados['rates']['BRL']
            resultado_label.config(text=f"Cotação do euro: R$ {cotacao:.2f}")
        elif moeda_digitada == "libra":
            cotacao = dados['rates']['BRL']
            resultado_label.config(text=f"Cotação da libra: R$ {cotacao:.2f}")
        elif moeda_digitada == "iene":
            cotacao = dados['rates']['BRL']
            resultado_label.config(text=f"Cotação do iene: R$ {cotacao:.2f}")
    except Exception as e:
        resultado_label.config(text="Erro ao obter a cotação.")

janela = tk.Tk()
janela.title("Cotação de Moedas")

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(janela, text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

mensagem2 = tk.Label(janela, text="Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

mensagem2 = tk.Label(janela, text="Moedas disponiveis: dollar, euro, libra, iene")
mensagem2.grid(row=2, column=0)

moeda = tk.Entry(janela)
moeda.grid(row=1, column=1)

buscar_button = tk.Button(janela, text="Buscar Cotação", command=obter_cotacao)
buscar_button.grid(row=3, column=0, columnspan=2)

resultado_label = tk.Label(janela, text="", fg='black')
resultado_label.grid(row=4, column=0, columnspan=2, sticky="NSEW" )

janela.mainloop()