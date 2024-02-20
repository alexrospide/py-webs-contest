import json
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


def do_the_scraping():
    # Pegar os dados da url
    url = 'https://www.pm.sc.gov.br/concursos/processos-seletivos-do-colegio-da-pmsc-cfnp?ConcursoSearch%5Bcriado_em%5D=&ConcursoSearch%5Bdescricao%5D=ACT&ConcursoSearch%5Bstatus%5D=1'

    option = Options()
    option.add_argument("--headless")
    driver = webdriver.Firefox(options=option)

    driver.get(url)

    time.sleep(2)

    element = driver.find_element(By.ID, 'w0')

    html_content = element.get_attribute('outerHTML')

    # 2 - Parsear o conteudo HTML - BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find_all(name='table')

    # # 3 - Estruturar o conteúdo em um Data Frame - Pandas
    df_full = pd.read_html(str(table))[0]

    # print(df_full.columns.values)
    df = df_full[['Publicado em', 'Descrição', 'Status']]
    df.columns = ['Publicado em', 'Descrição', 'Status']

    lista_concurso = {'lista': df.to_dict('records')}

    print('aqui é no web scrapping')
    print(lista_concurso['lista'])

    # 4 - transformar os dados em um dicionário

    # js = json.dumps(lista_concurso['lista'], ensure_ascii=False)
    # print(js)
    driver.quit()
    # with open('lista_concurso.json', 'w', encoding='utf-8') as concursos:
    #     concursos.write(js)
    return lista_concurso['lista']