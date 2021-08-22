from bs4 import BeautifulSoup
import requests
import csv
#Url vas permettre de definir la page que l'on veut cibler
url = 'https://euw.op.gg/ranking/ladder/'
#request permet de reach cette page lors de la compilation du code python
page = requests.get (url)

#Renvoi le status de la requete GET/ ou autres
#Rend un status 200 si ca a reussi
print(page.status_code)

#Je comprend pas ce que cette commande fait : 
soup = BeautifulSoup (page.text, "html.parser")
#print(soup)

def get_html(url):
   response = requests.get(url)
   return response.text

def get_all_items(html):
    soup = BeautifulSoup(html, 'lxml')
    #Ici on defini ce que le Scrapper vas nous renvoyer
    items = soup.find("table", {"class": "ranking-table"}).findAll("tr", {"class": "ranking-table__row"})
    return items

#On dit ce que l'on recupere dans les champs definient au dessus
def get_item_data(item):
    try:
          title = item.find('a').get('href')
    except:
          title = ''
    try:
          price = item.find("span").text
    except:
          price = ''
    data = {'title': title,
            'price': price}
    return data

#la on recupere les ranks
def get_ranks(html):
    data = BeautifulSoup(html, 'html.parser')
    rankser = ['<b>we dont have enough info<b>']
    try:
     ranks = data.find("ul",{"class" : "PastRankList"}).find_all('li')
    except:
      ranks='' 
    if ranks:
       print('right')   
       return ranks
    else:
     return ranks      

#Il faut trouver un moyen de trouver toute les saisons et les liés a une personne
def get_data_rank(rank):

      saison = rank.find("b").text

      rang = rank.get('title')

      rank = {'saisons': saison,
            'rangs': rang}
      return rank


def write_past_rank(i, rank,data):
    with open('ranks.csv', 'a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((rank['saisons'],
        rank['rangs'],data['price']))
        print(i, rank['rangs'], 'parsed')

def write_csv(i, data):
    with open('summoners.csv', 'a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'],
        data['price']))
        print(i, data['title'], 'parsed')

def getTheLowestElo(new_data):
    #Tableau utilisé pour faire notre comparaison  
    rankings = ['Silver','Gold','Platinium','Diamond','Master','GrandMaster','Challenger']

#variable globale
actualdata = []

def getAllinformationOnUser(data,new_data,actualdata,i):
      #Le but dans cette fonction est de recuperer tout les fonction de utilisateur 1 et de les reunir en un object
      # avec tout les rangs de toutes les saisons
      print('i',i)
      if (i > 0 and data['price'] != actualdata[1]):
            #ici on recupere le tableau complet/ nom
            actualdata.clear()
      actualdata.append(new_data['rangs'])
      actualdata.append(data['price'])
      actualdata.append(new_data['saisons'])
      print(data['price'])
      print(actualdata)
      
      print("actual data :", actualdata)
      



def main():
   url = 'https://euw.op.gg/ranking/ladder/'
   for page in range(1, 5):  # count of pages to parse
       all_items = get_all_items(get_html(url + '?_pgn={}'.format(page)))
       #On recupere le premier nom
       for i, item in enumerate(all_items):
            data = get_item_data(item)
            write_csv(i, data)
            new_url = data['title']
            print ('voila la nouvelle url ' + new_url)
            all_ranks = get_ranks(get_html('https:' + new_url))
            #on recupere tout les informations du premier nom
            for j, rank in enumerate(all_ranks):
                print('enumerate : ')  
                print(enumerate(all_ranks))  
                new_data = get_data_rank(rank)
                write_past_rank(j,new_data,data)
                print('data :',data,'newdata:',new_data)
                #on vas tenter de reunir toutes les informations :
                getAllinformationOnUser(data,new_data,actualdata,i)           

if __name__ == '__main__':
   main()

