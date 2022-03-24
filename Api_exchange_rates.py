import requests
import json

class Api_exchange_rates:
    def __init__(self):
        self.api_key = "sua_api_key_aqui"
        self.url_base = "http://api.exchangeratesapi.io/v1/"
        self.opcoes_api = {
            "mais_recente":"latest",
            "historico":"historical",
            "conversao":"convert",
            "serie_temporal":"timeseries",
            "flutuacao":"fluctuation"
        }


    def ultima_cotacao(self, lista_moedas_alvo):
        moedas_alvo = ",".join(lista_moedas_alvo)
        req = self.opcoes_api["mais_recente"]
        url = f"{self.url_base}{req}?access_key={self.api_key}&symbols={moedas_alvo}"
        r = requests.get(url)
        if r.status_code != 200:
            print("Não foi possível obter os dados!")
        else:
            conteudo = json.loads(r.text)
            print(conteudo)


    def data_cotacao(self, data ,lista_moedas_alvo):
        moedas_alvo = ",".join(lista_moedas_alvo)
        url = f"{self.url_base}{data}?access_key={self.api_key}&symbols={moedas_alvo}"
        r = requests.get(url)
        if r.status_code != 200:
            print("Não foi possível obter os dados!")
        else:
            conteudo = json.loads(r.text)
            print(conteudo)


# Criando a instância da classe e chamando as funções 
api_de_dados = Api_exchange_rates()
api_de_dados.ultima_cotacao(["BRL","USD"])
api_de_dados.data_cotacao("2022-03-01", ["BRL", "USD"])
