#WEB SCRAPPING
from bs4 import BeautifulSoup
import requests

#Ele irá pegar to.do o conteúdo e jogar para o objeto 'site'.
site = requests.get("https://www.climatempo.com.br/").content

#Objeto site está recebendo o conteúdo da requisição http do site....
soup = BeautifulSoup(site, 'html.parser')
#Objeto soup está baixando do site o html desse site
# print(soup.prettify())
#Transforma html em string e o print vai exibir o html

temperatura = soup.find('span', class_='temperature _margin-l-5 -font-13')
print(temperatura.string)

#Imprimindo somente a string do título
print(soup.title.string)

#identificando a primeira TAG de âncora
print(soup.a)

#identificando outra TAG de âncora com string
print(soup.p.string)

