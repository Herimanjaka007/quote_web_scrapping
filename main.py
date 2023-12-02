from scrappy import result,top_tags

if __name__ == "__main__":
    print("""
    *********************************
          Ce programme vous 
          offre des citations 
          de votre choix
    *********************************
""")
            
    print("Ci-dessous la liste de top tag :")
    print(top_tags)
    user_tags = input("Veuillez saisir votre tags: ")
    find = False

    for quote in result:
        if user_tags in [tag.string for tag in quote.find_all('a','tag')] :
            print('\n')
            print(quote.find('span','text').string)
            find = True
    
    if not find:
        print('Tag non trouve dans cette page')