import requests
from bs4 import BeautifulSoup

#code bloquant en cas de perte de connexion
res = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(res.text,'html.parser')
result = soup.find_all('div','quote')
top_tags = [tag.string for tag in soup.find('div','tags-box').find_all('a','tag')]



