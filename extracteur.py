import os
import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd



def recup_liste_url(): #fct qui récupère la liste des url à partir du fichier texte
    debut_url = 'https://en.wikipedia.org/wiki/'
    liste_url = [] #futur liste des urls
    fichier = open("C:/Users/Admin/Documents/PDL/wikiurls.txt","r") #ouvre le fichier
    for ligne in fichier: #parcours chaques ligne du fichier et l'ajoute à la liste
        url = debut_url + ligne #en complétant l'url
        liste_url.append(url.strip()) #strip enlève les espaces avant et après la chaine de caractère
    fichier.close() #ferme le fichier
    return liste_url

def requete_url(url): #requête à partir de l'url
    requete = requests.get(url)
    #print(requete.status_code)
    if (requete.status_code == 200): #si la requête à bien fonctionné
        page = requete.content #recupère le contenu de la page et le renvoi
        resultat = BeautifulSoup(page, features='html.parser')
        return resultat

def recup_tableau(url): #Récupération du ou des tableau(x) de l'url
    response = requests.get(url)
    tableaux = pd.read_html(response.text, attrs={"class" : "wikitable"})
    #soup = BeautifulSoup(response.text, features='html.parser')
    #tableaux = soup.find_all('table',class_='wikitable') #fonction qui récupère les données de tableaux HTML
    return tableaux
 
"""def extract_tableau(url):  
    i=0
    for 
"""

#main
liste_url=recup_liste_url()
for url in liste_url: #boucle pour parcourir la liste des urls en envoyant une requête pour chaque
    resultat = requete_url(url) #si résultat=none la requête n'a pas abouti
    #suite
recup_tableau = recup_tableau(url)

for wikitable in recup_tableau:
    recup_tableau
    print(recup_tableau)