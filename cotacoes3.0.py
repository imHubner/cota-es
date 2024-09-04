import tkinter as tk
import requests

def obter_cotacao(moeda):
    if moeda == "dollar":
        url = "https://api.exchangerate-api.com/v4/latest/USD"
    elif moeda == "euro":
        url = "https://api.exchangerate-api.com/v4/latest/EUR"
    elif moeda == "libra":
        url = "https://api.exchangerate-api.com/v4/latest/GBP"
    elif moeda == "iene":
        url = "https://api.exchangerate-api.com/v4/latest/JPY"

    try:
        resposta = requests.get(url)
        dados = resposta.json()
        cotacao = dados['rates']['BRL']
        if moeda == "dollar":
            resultado_label.config(text=f"Cotação do dólar: R$ {cotacao:.2f}")
        elif moeda == "euro":
            resultado_label.config(text=f"Cotação do euro: R$ {cotacao:.2f}")
        elif moeda == "libra":
            resultado_label.config(text=f"Cotação da libra: R$ {cotacao:.2f}")
        elif moeda == "iene":
            resultado_label.config(text=f"Cotação do iene: R$ {cotacao:.2f}")
    except Exception as e:
        resultado_label.config(text="Erro ao obter a cotação.")

def obter_cotacao_digitada():
    moeda_digitada = moeda.get().strip().lower()
    if moeda_digitada == "dollar":
        obter_cotacao("dollar")
    elif moeda_digitada == "euro":
        obter_cotacao("euro")
    elif moeda_digitada == "libra":
        obter_cotacao("libra")
    elif moeda_digitada == "iene":
        obter_cotacao("iene")
    else:
        resultado_label.config(text="Moeda não reconhecida.")

janela = tk.Tk()
janela.title("Cotação de Moedas")

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1, 2, 3, 4], weight=1)

mensagem = tk.Label(janela, text="Sistema de Busca de Cotação de Moedas", fg='white', bg='black', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=5, sticky="NSEW")

mensagem2 = tk.Label(janela, text="Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

moeda = tk.Entry(janela)
moeda.grid(row=1, column=1)

buscar_button = tk.Button(janela, text="Buscar Cotação", command=obter_cotacao_digitada)
buscar_button.grid(row=1, column=2)

dollar_button = tk.Button(janela, text="Dólar", command=lambda: obter_cotacao("dollar"))
dollar_button.grid(row=2, column=0)

euro_button = tk.Button(janela, text="Euro", command=lambda: obter_cotacao("euro"))
euro_button.grid(row=2, column=1)

libra_button = tk.Button(janela, text="Libra", command=lambda: obter_cotacao("libra"))
libra_button.grid(row=2, column=2)

iene_button = tk.Button(janela, text="Iene", command=lambda: obter_cotacao("iene"))
iene_button.grid(row=2, column=3)

resultado_label = tk.Label(janela, text="", fg='black')
resultado_label.grid(row=3, column=0, columnspan=5, sticky="NSEW" )

janela.mainloop()