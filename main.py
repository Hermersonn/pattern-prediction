# main.py - Arquivo principal
import logging
from extractor import extrair_dados
from saver import salvar_dados

# URL de teste
URL = "https://quotes.toscrape.com/"

if __name__ == "__main__":
    logging.info("Iniciando processo de extração e salvamento de dados.")
    dados = extrair_dados(URL)
    salvar_dados(dados)
    logging.info("Processo finalizado com sucesso.")