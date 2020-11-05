import unittest
from urllib.request import urlopen
from extracteur import*


class TestExtracteur(unittest.TestCase):
    bs = None
    
    def test_extracteur(self): #Fonction qui test le nombre de tableaux récupérés, si il est égal à 7 pour cet exemple, alors l'extracteur fonctionne correctement
        TestExtracteur.bs = BeautifulSoup(urlopen('https://en.wikipedia.org/wiki/New_York_City'), 'html.parser')
        TestTableau = TestExtracteur.bs.find_all('table',class_='wikitable')
        TestNbTab = len(TestTableau)    
        
        self.assertTrue(TestTableau)
        self.assertEqual(TestNbTab,7)
if __name__ == '__main__':
    unittest.main()

