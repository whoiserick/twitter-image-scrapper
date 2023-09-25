import os
import requests  # Adicione esta linha no início do seu código
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Função para criar diretório se não existir
def criar_diretorio(nome_usuario):
    if not os.path.exists(nome_usuario):
        os.makedirs(nome_usuario)

# Caminho para o ChromeDriver na pasta raiz do projeto
chromedriver_path = os.path.join(os.getcwd(), 'chromedriver')

# Inicialize o WebDriver do Chrome
driver = webdriver.Chrome(chromedriver_path)

# URL do perfil do Twitter
url = 'https://twitter.com/ukazuhira'

# Obtenha o nome de usuário a partir da URL
nome_usuario = url.split('/')[-1]

# Abra a página no navegador
driver.get(url)

# Aguarde até que todas as imagens estejam carregadas
wait = WebDriverWait(driver, 10)
elementos_imagens = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))

# Crie uma instância do BeautifulSoup com o conteúdo atualizado da página
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Encontre as imagens na página
imagens = soup.find_all('img')

# Chame a função para criar o diretório
criar_diretorio(nome_usuario)

# Itera sobre as imagens e faça o download
for i, img in enumerate(imagens):
    url = img['src']
    response = requests.get(url)
    with open(f'{nome_usuario}/imagem_{i}.jpg', 'wb') as f:
        f.write(response.content)

# Feche o navegador
driver.quit()
