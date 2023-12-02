from bs4 import BeautifulSoup
import requests

def get_BeautifulSoup(url):
    res = requests.get(url)
    return BeautifulSoup(res.text,'html.parser')
