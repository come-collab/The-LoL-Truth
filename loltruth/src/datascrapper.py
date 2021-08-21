from bs4 import BeautifulSoup
import requests
import csv
#Url vas permettre de definir la page que l'on veut cibler
url = 'https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276'
#request permet de reach cette page lors de la compilation du code python
page = requests.get (url)

#Renvoi le status de la requete GET/ ou autres
#Rend un status 200 si ca a reussi
print(page.status_code)

#Je comprend pas ce que cette commande fait : 
soup = BeautifulSoup (page.text, "html.parser")
#print(soup)


#On vas y aller etape par etape 
def get_html(url):
   response = requests.get(url)
   return response.text

#Utilisation de beautifulSoup pour scrap le projet trouver le nom des champs a recuperer
def get_all_items(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find("ul", {"class": "b-list__items_nofooter"}).findAll("li", {"class": "s-item"})
    return items

#On dit ce que l'on recupere dans les champs definient au dessus
def get_item_data(item):
    try:
          title = item.find({"h3": "b-s-item__title"}).text
    except:
          title = ''
    try:
          price = item.find("span", {"class": "s-item__price"}).text
    except:
          price = ''
    data = {'title': title,
            'price': price}
    return data

#Fonction pour pouvoir créer le fichier CSV
def write_csv(i, data):
    with open('notebooks.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'],
        data['price']))
        print(i, data['title'], 'parsed')


#Fonction main réunissant toutes les anciennes fonctions en une et créer le projet
def main():
   url = 'https://www.ebay.com/b/Laptops-Netbooks/175672/bn_1648276'
   for page in range(1, 5):  # count of pages to parse
       all_items = get_all_items(get_html(url + '?_pgn={}'.format(page)))
       for i, item in enumerate(all_items):
           data = get_item_data(item)
           write_csv(i, data)


if __name__ == '__main__':
   main()




