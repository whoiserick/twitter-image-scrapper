import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Função para criar diretório se não existir
def criar_diretorio(nome_usuario):
    if not os.path.exists(nome_usuario):
        os.makedirs(nome_usuario)

# Inicialize o WebDriver do Chrome
driver = webdriver.Chrome()

# URL do login do Twitter
url_login = 'https://twitter.com/login'

# Credenciais da sua conta
usuario = 'seu_usuario'
senha = 'sua_senha'

# Abra a página de login do Twitter
driver.get(url_login)

# Aguarde até que os campos de login e senha estejam presentes na página
wait = WebDriverWait(driver, 10)
elemento_usuario = wait.until(EC.presence_of_element_located((By.NAME, 'session[username_or_email]')))
elemento_senha = wait.until(EC.presence_of_element_located((By.NAME, 'session[password]')))

# Preencha os campos de login e senha
elemento_usuario.send_keys(usuario)
elemento_senha.send_keys(senha)

# Envie o formulário de login
elemento_senha.send_keys(Keys.RETURN)

# Aguarde até que todas as imagens estejam carregadas
elementos_imagens = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))

# Crie uma instância do BeautifulSoup com o conteúdo atualizado da página
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Encontre as imagens na página
imagens = soup.find_all('img')

# Obtenha o nome de usuário a partir da URL
nome_usuario = usuario

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
