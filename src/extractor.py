# extractor.py - Responsável pela extração de dados
import requests
from bs4 import BeautifulSoup
import logging

# Configuração do logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extrair_dados(url):
    """
    Função para extrair dados de uma página HTML.
    :param url: URL da página web para coleta.
    :return: Lista de frases extraídas.
    """
    logging.info(f"Iniciando extração de dados da URL: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        logging.info("Página acessada com sucesso.")
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("span", class_="text")
        frases = [quote.text for quote in quotes]
        logging.info(f"{len(frases)} frases extraídas com sucesso.")
        return frases
    else:
        logging.error("Não foi possível acessar a página.")
        return []
