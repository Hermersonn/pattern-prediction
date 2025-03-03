# saver.py - Responsável por salvar os dados no CSV
import logging
import pandas as pd
from datetime import datetime
import os

# Configuração do logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def salvar_dados(dados, pasta="data", arquivo="dados.csv"):
    """
    Função para salvar dados extraídos em um arquivo CSV.
    :param dados: Lista de dados para salvar.
    :param pasta: Nome da pasta onde o arquivo será salvo.
    :param arquivo: Nome do arquivo CSV.
    """
    if not dados:
        logging.warning("Nenhum dado para salvar.")
        return

    # Cria a pasta se não existir
    if not os.path.exists(pasta):
        os.makedirs(pasta)
        logging.info(f"Pasta '{pasta}' criada automaticamente.")

    caminho_arquivo = os.path.join(pasta, arquivo)
    data_atual = datetime.now().strftime("%Y-%m-%d")
    hora_atual = datetime.now().strftime("%H:%M:%S")
    df = pd.DataFrame([[frase, data_atual, hora_atual] for frase in dados], columns=["Frase", "Data", "Hora"])

    # Cria o arquivo se não existir ou adiciona novos dados
    if not os.path.exists(caminho_arquivo):
        df.to_csv(caminho_arquivo, index=False)
        logging.info(f"Arquivo '{arquivo}' criado automaticamente.")
    else:
        df.to_csv(caminho_arquivo, index=False, mode="a", header=False)
        logging.info(f"Dados adicionados no arquivo '{arquivo}'.")

    logging.info(f"{len(dados)} frases salvas no CSV com sucesso!")