import os
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd



def recup_liste_url(url): #fct qui récupère la liste des url à partir du fichier texte
    debut_url = 'https://en.wikipedia.org/wiki/'
    liste_url = [] #futur liste des urls
    fichier = open("inputdata/"+url,"r") #ouvre le fichier
    for ligne in fichier: #parcours chaques ligne du fichier et l'ajoute à la liste
        url = debut_url + ligne #en complétant l'url
        liste_url.append(url.strip()) #strip enlève les espaces avant et après la chaine de caractère
    fichier.close() #ferme le fichier
    return liste_url


def recup_tableau(url): #Récupération du ou des tableau(x) de la page
    response = requests.get(url)
    #tableaux = pd.read_html(response.text, attrs={"class" : "wikitable"}) // Test avec pandas
    if (response.status_code == 200):
        soup = BeautifulSoup(response.text, "html.parser")
        tableaux = soup.find_all('table',class_='wikitable') #Fonction qui récupère les données des tableaux HTML
    
        print ("Tableaux récupérés : {num}".format(num=len(tableaux))) #Nombre de tableaux récupérés par la fonction
        return tableaux

    return None
       
def get_table_rows(table):
    rows = []
    for tr in table.find_all("tr"):
        cells =[]
        tds = tr.find_all("td")
        if len(tds) == 0:
            ths = tr.find_all("th")
            for th in ths:
                cells.append(th.text.strip())
        else:
            for td in tds:
                cells.append(td.text.strip())
        rows.append(cells)
    return rows  

def save_to_csv(table_name, rows):
    dircsv = './output'
    if not os.path.exists(dircsv):
        os.mkdir(dircsv)
    pd.DataFrame(rows).to_csv(f"output/{table_name}.csv",encoding='utf-8')
    #with open(f"output/{table_name}.csv", "w", encoding="utf-8") as f:
    #    f.write(rows)


def wikipedia_extractor(url):
    tables = recup_tableau(url)
    if tables is not None:
        for i, table in enumerate(tables, start = 1):
            table_name = f"{url[30:]}_{i}"
            rows = get_table_rows(table)
            save_to_csv(table_name, rows)

def extractor(urls):
    list_url = recup_liste_url(urls)
    for url in list_url:
        wikipedia_extractor(url)

if __name__ == "__main__":
    urls = "wikiurls.txt"
    extractor(urls)

