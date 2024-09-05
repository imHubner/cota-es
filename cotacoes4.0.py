import tkinter as tk
import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import matplotlib.ticker as mticker
from mplfinance.original_flavor import candlestick_ohlc
from datetime import datetime

# Chave da API Alpha Vantage (substitua pela sua chave)
API_KEY = "SUA_CHAVE_AQUI"

# Lista das 10 moedas mais valorizadas do mundo
moedas = {
    "Dinar do Kuwait": "KWD",
    "Dinar do Bahrein": "BHD",
    "Rial de Omã": "OMR",
    "Dinar da Jordânia": "JOD",
    "Libra Esterlina": "GBP",
    "Dólar das Ilhas Caimã": "KYD",
    "Franco Suíço": "CHF",
    "Euro": "EUR",
    "Dólar Americano": "USD",
    "Dólar Canadense": "CAD"
}

def obter_cotacao_atual(codigo_moeda):
    url = f"https://api.exchangerate-api.com/v4/latest/{codigo_moeda}"
    resposta = requests.get(url)
    dados = resposta.json()
    cotacao = dados['rates']['BRL']
    return cotacao

def obter_dados_historicos(codigo_moeda):
    url = f"https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={codigo_moeda}&to_symbol=BRL&apikey={API_KEY}&outputsize=compact"
    resposta = requests.get(url)
    dados = resposta.json()

    if "Time Series FX (Daily)" in dados:
        series_temporal = dados["Time Series FX (Daily)"]
        data = []
        for data_str, valores in series_temporal.items():
            data.append([
                mdates.date2num(datetime.strptime(data_str, '%Y-%m-%d')),  # Data no formato numérico para o matplotlib
                float(valores['1. open']),
                float(valores['2. high']),
                float(valores['3. low']),
                float(valores['4. close']),
            ])
        return data[::-1]  # Invertendo a lista para ordenar as datas corretamente
    else:
        return None

def criar_grafico_candles(nome_moeda, codigo_moeda):
    dados = obter_dados_historicos(codigo_moeda)

    if dados:
        plt.style.use('dark_background')  # Aplicar estilo de fundo escuro

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.xaxis_date()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax.xaxis.set_major_locator(mticker.MaxNLocator(10))

        candlestick_ohlc(ax, dados, width=0.6, colorup='green', colordown='red')

        plt.title(f'Gráfico de Candles - {nome_moeda} (em BRL)', color='white')
        plt.xlabel('Data', color='white')
        plt.ylabel('Cotação (em BRL)', color='white')
        plt.xticks(rotation=45, ha='right', color='white')
        plt.yticks(color='white')
        plt.tight_layout()
        plt.show()
    else:
        resultado_label.config(text="Erro ao obter os dados históricos.")

def criar_grafico_colunas():
    nomes_moedas = list(moedas.keys())
    cotacoes = []
    cores = ['blue', 'green', 'red', 'purple', 'orange', 'pink', 'yellow', 'cyan', 'magenta', 'gray']

    for nome_moeda, codigo_moeda in moedas.items():
        cotacao = obter_cotacao_atual(codigo_moeda)
        cotacoes.append(cotacao)

    plt.style.use('dark_background')  # Aplicar estilo de fundo escuro

    plt.figure(figsize=(10, 6))  # Definindo o tamanho do gráfico
    plt.bar(nomes_moedas, cotacoes, color=cores)  # Adicionando cores às barras
    plt.xlabel("Moeda", color='white')
    plt.ylabel("Cotação (em BRL)", color='white')
    plt.title("Cotação Atual das 10 Moedas Mais Valorizadas do Mundo", color='white')
    plt.xticks(rotation=45, ha="right", color='white')  # Rotacionando os nomes das moedas para melhor visualização
    plt.yticks(color='white')
    plt.tight_layout()  # Ajustando o layout
    plt.show()

janela = tk.Tk()
janela.title("Cotação de Moedas")

janela.rowconfigure(0, weight=1)
janela.columnconfigure([i for i in range(len(moedas) + 2)], weight=1)

mensagem = tk.Label(janela, text="Sistema de Gráficos para Moedas", fg='white', bg='black', width=40, height=5)
mensagem.grid(row=0, column=0, columnspan=len(moedas) + 1, sticky="NSEW")

mensagem2 = tk.Label(janela, text="Selecione a moeda desejada para ver o gráfico de candles")
mensagem2.grid(row=1, column=0, columnspan=len(moedas))

# Criando botões para cada moeda
for i, (nome_moeda, codigo_moeda) in enumerate(moedas.items()):
    button = tk.Button(janela, text=nome_moeda, command=lambda nm=nome_moeda, cm=codigo_moeda: criar_grafico_candles(nm, cm))
    button.grid(row=2, column=i)

grafico_colunas_button = tk.Button(janela, text="Ver Gráfico de Colunas", command=criar_grafico_colunas)
grafico_colunas_button.grid(row=3, column=0, columnspan=len(moedas))

resultado_label = tk.Label(janela, text="")
resultado_label.grid(row=4, column=0, columnspan=len(moedas))

janela.mainloop()
