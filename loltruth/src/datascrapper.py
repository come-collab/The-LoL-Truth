from bs4 import BeautifulSoup
import requests
import csv
import numpy as np
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
    elements_to_remove = ['S6','S9','S2020','S8','S7','S5','S2021','S4','S3','S2','S1']
    lowestElo =""
    #recupere le tableau avec tout les rangs
    #el dans new_data doit etre le rang simple et ce serrais cool qu'il ny ai que les informations de rang pour eviter
    #un traitement de données trop laborieux
    #on supprime les duplicate et les noms des chall
    nameUser = new_data[1]
    new_data = list(set(new_data)) 
    new_data.remove(nameUser)

    #On supprime toutes les informations concernants les saisons
    new_data = [element for element in new_data if element not in elements_to_remove]   
    #on retraite le tableau en supprimant les informations de ELO dont on a pas besoin
      
    new_data = [element.split() for element in new_data if element is not None]
    #On flatten l'array
    new_data = [item for sublist in new_data for item in sublist]  
    #Fonction permettant de definir qu'elle est le ELO le plus bas de chaque player in challenger babyyyyyyy 
    lowestElo = '' 
    if 'Bronze' in new_data:
          lowestElo = 'Bronze'
          write_lowest_elo(lowestElo,nameUser)
          return lowestElo
    else:
      if 'Silver' in new_data:
          lowestElo = 'Silver'
          write_lowest_elo(lowestElo,nameUser)
          return lowestElo
      else :
            if 'Gold' in new_data:
                lowestElo =  'Gold'
                write_lowest_elo(lowestElo,nameUser)
                return lowestElo
            else:
                  if 'Platinum' in new_data:
                      lowestElo = 'Platinum'
                      write_lowest_elo(lowestElo,nameUser)
                      return lowestElo
                  else:
                        if 'Diamond' in new_data:
                            lowestElo = 'Diamond'
                            write_lowest_elo(lowestElo,nameUser)
                            return lowestElo
                        else:
                            lowestElo = 'Smurf'
                            write_lowest_elo(lowestElo,nameUser)
                            return lowestElo                           
    #Probablement devoir appeller une fonction qui crée un csv avec le elo minimum de chaque Challenger 
    #Ecrire le prenom sur csv avec le ELO le plus bas du joueur 

def write_lowest_elo(lowestElo,nameUser):
    with open('lowestRankPerName.csv', 'a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((lowestElo,nameUser))


def getTimeToHighRank(actualdata):
       rankings = ['Silver','Gold','Diamond','Platinum','Bronze','Master','Challenger','GrandMaster']
    #premiere chose a faire rendre le tableau lisible  
       nameUser = actualdata[1]
       actualdata = [element.split() for element in actualdata if element is not None]
       actualdata = [item for sublist in actualdata for item in sublist]
       #reste en ordre  
       counter = 0
       newnewdata = []
       #Clear le tableau pour qu'il ne reste que les rangs
       for el in actualdata:
           if el == 'Challenger' or el == 'Gold' or el == 'Platinum' or el =='Master' or el =='Diamond' or el =='Grandmaster' or el =='Silver' or el =='Bronze':
               newnewdata.append(el)

       print('actual data after cleaning it :', newnewdata)
       for el in newnewdata:
           counter += 1
           if el == "Master" or el =="Challenger" or el == "Grandmaster":
            break    
       counter = counter -  1
       print("Counter :", counter)
       write_seasonToHighElo(counter,nameUser)
       





def write_seasonToHighElo(counter,nameUser):
      with open('TimeToHighElo.csv', 'a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((counter,nameUser))

#Global variable
actualdata = []

def getAllinformationOnUser(data,new_data,actualdata,i):
      #Le but dans cette fonction est de recuperer tout les fonction de utilisateur 1 et de les reunir en un object
      # avec tout les rangs de toutes les saisons
      print('i',i)
      if (i > 0 and data['price'] != actualdata[1]):
            #ici on recupere le tableau complet par nom
            getTheLowestElo(actualdata)
            getTimeToHighRank(actualdata)
            #on clear le tableau apres chaque user
            actualdata.clear()
      actualdata.append(new_data['rangs'])
      actualdata.append(data['price'])
      actualdata.append(new_data['saisons'])
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
                getAllinformationOnUser(data,new_data,actualdata,i)           

if __name__ == '__main__':
   main()

