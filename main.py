import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Função para criar diretório se não existir
def criar_diretorio(nome_usuario):
    if not os.path.exists(nome_usuario):
        os.makedirs(nome_usuario)

# Inicialize o WebDriver do Chrome
driver = webdriver.Chrome()

# URL do perfil do Twitter que você deseja acessar
url_perfil = 'https://twitter.com/ukazuhira'

# Abra a página do perfil do Twitter
driver.get(url_perfil)

# Aguarde até que todas as imagens estejam presentes
wait = WebDriverWait(driver, 20)
elementos_imagens = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//img[@srcset]')))

# Obtenha o nome de usuário a partir da URL
nome_usuario = url_perfil.split('/')[-1]

# Chame a função para criar o diretório
criar_diretorio(nome_usuario)

# Encontre todas as imagens na página
imagens = driver.find_elements(By.XPATH, '//img[@srcset]')

# Itera sobre as imagens e faça o download
for i, img in enumerate(imagens):
    url = img.get_attribute('src')
    identificador = url.split('/')[-1].split('?')[0]
    extensao = url.split('=')[-1]
    response = requests.get(url)
    with open(f'{nome_usuario}/imagem_{i}.{extensao}', 'wb') as f:
        f.write(response.content)

# Feche o navegador
driver.quit()
