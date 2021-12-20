
import requests
from bs4 import BeautifulSoup
from Models.Dictionnary import Dictionary

aphabetique = ['a', 'b', 'c', 'd', 'e', 'f',
               'g',
               'h',
               'i',
               'j',
               'k',
               'l',
               'm',
               'n',
               'o',
               'p',
               'q',
               'r',
               's',
               't',
               'u',
               'v',
               'w', 'x', 'y', 'z']
dicio = Dictionary()
for i in aphabetique:
    reponse = requests.get(
        f'https://www.le-dictionnaire.com/repertoire/{i}01.html',
    )
    soup = BeautifulSoup(reponse.content, 'html.parser')
    lis = soup.find_all('li')
    for li in lis[50:61]:
        nom = li.text
        definition = requests.get(
            f"https://www.le-dictionnaire.com/definition/{li.text}")
        soup = BeautifulSoup(definition.content, 'html.parser')
        deffs = soup.find_all('li')
        defini = deffs[0].text.encode('utf-8')
        datas = {'nom': nom, 'definition': defini}
        dicio.AjouterUnMot(datas)
