import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

# Url de teste
url = "https://quotes.toscrape.com/"

# Fazendo requisição
response = requests.get(url)

if response.status_code == 200:
    print("Pagina acessada com sucesso.")

    # Transformando o HTML em objeto BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Buscando todas as frases dentro da classe 'text'
    quotes = soup.find_all("span", class_="text")

    # Lista para armazenamento de dados
    data = []

    # Loop para extrair dados
    for quote in quotes:
        frase = quote.text
        data_atual = datetime.now().strftime("%Y-%m-%d")
        hora_atual = datetime.now().strftime("%H:%M:%S")
        data.append([frase, data_atual, hora_atual])

    # Criando o dataframe
    df = pd.DataFrame(data, columns=["Frase", "Data", "Hora"])

    # Caminho raiz do repositório (sempre um nível acima da pasta 'src')
    repo_raiz = os.path.dirname(os.path.dirname(__file__))

    # Caminho da pasta data dentro do repositório
    pasta = os.path.join(repo_raiz, "data")

    # Criando pasta se não existir
    if not os.path.exists(pasta):
        os.makedirs(pasta)
        print("Pasta 'data' criada automaticamente.")

    # Caminho do arquivo
    caminho_arquivo = os.path.join(pasta, "dados.csv")

    # Criando o arquivo dados.csv se não existir
    if not os.path.exists(caminho_arquivo):
        df.to_csv(caminho_arquivo, index=False)
        print("Arquivo 'dados.csv' criado automaticamente.")
    else:
        df.to_csv(caminho_arquivo, index=False, mode="a", header=False)
        print("Dados adicionados no arquivo 'dados.csv'")

    print(f"{len(quotes)} frases salvas no CSV com sucesso!")
else:
    print("Não foi possível acessar a página.")
