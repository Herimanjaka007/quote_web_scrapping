from bs4 import BeautifulSoup
import requests

def get_BeautifulSoup(url:str):
    """scrapp un url fournit en argument et retourne un Objet Beautifulsoup.

    Args:
        url (str): url a scrapper

    Returns:
        BeautifulSoup: Objet qui fournit des methodes pour naviguer et chercer dans l'arborescence du page.
    """
    res = requests.get(url)
    return BeautifulSoup(res.text,'html.parser')
