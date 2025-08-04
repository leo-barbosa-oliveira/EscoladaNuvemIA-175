# Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.import requests

import requests

from datetime import datetime

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            
            chave = f"{moeda}BRL"
            if chave in dados:
                cotacao = dados[chave]
                
                valor_atual = float(cotacao["bid"])
                valor_max = float(cotacao["high"])
                valor_min = float(cotacao["low"])
                timestamp = int(cotacao["timestamp"])
                data_hora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")

                print(f"\n=== Cotação {moeda}/BRL ===")
                print(f"Valor atual: R$ {valor_atual:.2f}")
                print(f"Valor máximo do dia: R$ {valor_max:.2f}")
                print(f"Valor mínimo do dia: R$ {valor_min:.2f}")
                print(f"Última atualização: {data_hora}")
            else:
                print("Código de moeda não encontrado ou inválido.")
        else:
            print("Erro ao acessar a API. Código de status:", resposta.status_code)
    except Exception as e:
        print("Erro durante a requisição:", str(e))

# Entrada do usuário
moeda_usuario = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
consultar_cotacao(moeda_usuario)
