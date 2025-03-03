# Importando a biblioteca requests para fazer requisições HTTP
import requests

# Definindo a URL do site que queremos acessar
url = "https://www.google.com"  # 🔥 Aqui só estamos testando com o Google (vamos mudar depois)

# Fazendo a requisição HTTP GET para a URL
response = requests.get(url)

# Exibindo o código de status da resposta
print("Status Code:", response.status_code)  # 200 = Sucesso, 404 = Não encontrado, 500 = Erro do servidor

# Validando se a requisição foi bem-sucedida
if response.status_code == 200:
    print("✅ Site acessado com sucesso!")
else:
    print("❌ Falha ao acessar o site!")
