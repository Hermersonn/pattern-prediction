import requests
from bs4 import BeautifulSoup

# URL do site (exemplo fictício por enquanto)
url = "https://quotes.toscrape.com/"

# Fazendo a requisição para pegar o HTML
response = requests.get(url)

# Garantindo que a página foi acessada com sucesso
if response.status_code == 200:
    print("✅ Página acessada com sucesso!")

    # Transformando o HTML em texto
    soup = BeautifulSoup(response.text, "html.parser")

    # Buscando todas as frases dentro da classe 'text'
    quotes = soup.find_all("span", class_="text")

    print(f"Encontramos {len(quotes)} frases na pagina!")

    for i, quote in enumerate(quotes):
        print(f"{i + 1} - {quote.text}")

else:
    print("Não foi pussivel acessar a pagina")