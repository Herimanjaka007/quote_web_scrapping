import os
from dotenv import load_dotenv
from fonction import *

if __name__ == "__main__":
    load_dotenv()
    url = os.getenv('URL')
    print(url)
    print("\nChargement ...\n")
    soup = get_BeautifulSoup(url)
    top_tags = [tag.string for tag in soup.find('div','tags-box').find_all('a','tag')]
    print("""
    *********************************
          Ce programme vous 
          offre des citations 
          de votre choix

    *********************************
          
""")
            
    print("Ci-dessous la liste de top tag :")
    print(top_tags)
    print("\n")
    user_tags = input("Veuillez saisir votre tags: ")
    print("\n Chargement ... \n")
    
    soup = get_BeautifulSoup(url+ f"/tag/{user_tags}")

    if len(soup.find_all('div','quote')) > 0:
        for quote in soup.find_all('div','quote'):
            if user_tags in [tag.string for tag in quote.find_all('a','tag')] :
                print('\n')
                print(quote.find('span','text').string)
    else:
        print("Y a pas de citations qui correspond a votre tag")