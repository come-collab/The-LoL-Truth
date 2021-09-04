from bs4 import BeautifulSoup
import requests
import csv
import numpy as np

url = 'https://www.op.gg/ranking/ladder/'

page = requests.get (url)


print(page.status_code)

soup = BeautifulSoup (page.text, "html.parser")
#print(soup)

def get_html(url):
   response = requests.get(url)
   return response.text

def get_all_items(html):
    soup = BeautifulSoup(html, 'lxml')

    items = soup.find("table", {"class": "ranking-table"}).findAll("tr", {"class": "ranking-table__row"})
    return items


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


#Global  variable to define the number of people starting in Silver/Gold.....
BronzeCounter = 0
SilverCounter = 0
GoldCounter = 0
PlatCounter = 0 
DiamondCounter = 0
SmurfCounter = 0


def getTheLowestElo(new_data):
    elements_to_remove = ['S6','S9','S2020','S8','S7','S5','S2021','S4','S3','S2','S1']
    lowestElo =""
    nameUser = new_data[1]
    new_data = list(set(new_data)) 
    new_data.remove(nameUser)

   
    new_data = [element for element in new_data if element not in elements_to_remove]   
 
      
    new_data = [element.split() for element in new_data if element is not None]
    
    new_data = [item for sublist in new_data for item in sublist]  
    
    lowestElo = '' 
    if 'Bronze' in new_data:
          lowestElo = 'Bronze'
          global BronzeCounter
          BronzeCounter += 1
          write_lowest_elo(lowestElo,nameUser,BronzeCounter)
          return lowestElo
    else:
      if 'Silver' in new_data:
          lowestElo = 'Silver'
          global SilverCounter
          SilverCounter += 1
          write_lowest_elo(lowestElo,nameUser,SilverCounter)
          return lowestElo
      else :
            if 'Gold' in new_data:
                lowestElo =  'Gold'
                global GoldCounter
                GoldCounter += 1
                write_lowest_elo(lowestElo,nameUser,GoldCounter)
                return lowestElo
            else:
                  if 'Platinum' in new_data:
                      lowestElo = 'Platinum'
                      global PlatCounter
                      PlatCounter += 1
                      write_lowest_elo(lowestElo,nameUser,PlatCounter)
                      return lowestElo
                  else:
                        if 'Diamond' in new_data:
                            lowestElo = 'Diamond'
                            global DiamondCounter
                            DiamondCounter += 1
                            write_lowest_elo(lowestElo,nameUser,DiamondCounter)
                            return lowestElo
                        else:
                            lowestElo = 'Smurf'
                            global SmurfCounter
                            SmurfCounter += 1
                            write_lowest_elo(lowestElo,nameUser,SmurfCounter)
                            return lowestElo

def write_lowest_elo(lowestElo,nameUser,totalSameElo):
    with open('lowestRankPerName.csv', 'a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((lowestElo,nameUser,'Total same Elo :', totalSameElo))


#counter year global variable
counterYear1 = 0
counterYear2 = 0
counterYear3 = 0
counterYear4 = 0
counterYearMorethan4 = 0

def getTimeToHighRank(actualdata): 
       nameUser = actualdata[1]
       actualdata = [element.split() for element in actualdata if element is not None]
       actualdata = [item for sublist in actualdata for item in sublist]
         
       counter = 0
       newnewdata = []
       for el in actualdata:
           if el == 'Challenger' or el == 'Gold' or el == 'Platinum' or el =='Master' or el =='Diamond' or el =='Grandmaster' or el =='Silver' or el =='Bronze':
               newnewdata.append(el)

       print('actual data after cleaning it :', newnewdata)
       for el in newnewdata:
           counter += 1
           if el == "Master" or el =="Challenger" or el == "Grandmaster":
            break
       if counter == 1:
           global counterYear1
           counterYear1 += 1
       if counter ==2:
           global counterYear2
           counterYear2 += 1
       if counter == 3:
           global counterYear3
           counterYear3 += 1
       if counter == 4:
           global counterYear4
           counterYear4 +=1
       if counter > 4:
           global counterYearMorethan4
           counterYearMorethan4 += 1    
       write_seasonToHighElo(counter,nameUser)

def write_seasonToHighElo(counter,nameUser):
      with open('TimeToHighElo.csv', 'a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(("Counter :",counter,nameUser))


actualdata = []

def getAllinformationOnUser(data,new_data,actualdata,i):
      print('i',i)
      if (i > 0 and data['price'] != actualdata[1]):
            getTheLowestElo(actualdata)
            getTimeToHighRank(actualdata)
            actualdata.clear()
      actualdata.append(new_data['rangs'])
      actualdata.append(data['price'])
      actualdata.append(new_data['saisons'])
      print("actual data :", actualdata)
      

def write_counter_year(data1,data2,data3,data4,data5):
    with open('yearstohighelo.csv', 'a',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(("In 1 year :",data1,"In 2 year :",data2,"In 3 year :",data3,"In 4 year :",data4,"In 5 year :",data5))

def main():
   url = 'https://www.op.gg/ranking/ladder/'
   for page in range(1, 5):  # count of pages to parse
       all_items = get_all_items(get_html(url + 'page={}'.format(page)))
       for i, item in enumerate(all_items):
            data = get_item_data(item)
            write_csv(i, data)
            new_url = data['title']
            print ('voila la nouvelle url ' + new_url)
            all_ranks = get_ranks(get_html('https:' + new_url))
            for j, rank in enumerate(all_ranks):
                print('enumerate : ')  
                print(enumerate(all_ranks))  
                new_data = get_data_rank(rank)
                write_past_rank(j,new_data,data)
                getAllinformationOnUser(data,new_data,actualdata,i)    
   write_counter_year(counterYear1,counterYear2,counterYear3,counterYear4,counterYearMorethan4)                   

if __name__ == '__main__':
   main()

