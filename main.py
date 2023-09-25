import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm

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

# Aguarde até que todas as imagens estejam presentes, com um tempo de espera de 20 segundos
wait = WebDriverWait(driver, 20)
elementos_imagens = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//img[@srcset]')))

# Obtenha o nome de usuário a partir da URL
nome_usuario = url_perfil.split('/')[-1]

# Chame a função para criar o diretório
criar_diretorio(nome_usuario)

# Encontre todas as imagens com atributo srcset
imagens = driver.find_elements(By.XPATH, '//img[@srcset]')

# Itera sobre as imagens e faça o download
for i, img in tqdm(enumerate(imagens), total=len(imagens), desc='Baixando imagens'):
    url = img.get_attribute('src')
    response = requests.get(url)
    with open(f'{nome_usuario}/imagem_{i}.jpg', 'wb') as f:
        f.write(response.content)

# Feche o navegador
driver.quit()
