import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Inicialize o WebDriver do Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome('./chromedriver.exe')

# URL do perfil do Twitter
url = 'https://twitter.com/ukazuhira'

# Abra a página no navegador
driver.get(url)

# Aguarde até que as imagens estejam presentes na página
wait = WebDriverWait(driver, 10)
elementos_imagens = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))

# Crie uma instância do BeautifulSoup com o conteúdo atualizado da página
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Encontre as imagens na página
imagens = soup.find_all('img')

# Itera sobre as imagens e faça o download
for i, img in enumerate(imagens):
    url = img['src']
    response = requests.get(url)
    with open(f'imagem_{i}.jpg', 'wb') as f:
        f.write(response.content)

# Feche o navegador
driver.quit()
