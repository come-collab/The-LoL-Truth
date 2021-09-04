# The-LoL-Truth
### [Go visit the project !](www.lolbasedondata.com)
## Defining the purpose of the website.

### 1) Why you will not be good at League of Legend.
The purpose is to fetch data from the best players in the world and show with a graph how quickly they climbed the ladder with their mains account.
The idea behind the graph comes from LS interview on youtube and the fact that kind of blew my mind which is that most of the pros that he ever encoutered, reached their top ELO in less then 2 years of playing the game.

Meanwhile you have people tryharding the game uncapable of going past gold ! With data we will find out what is truth behind top level in video games.

### What technologies ?

The application will mainly run with javascript dependency so we will try a JS framework.

The framework we will use is : **Vue.js** for its simplicity in usage.

We will also use **Chart JS** for the graphs.

And of course the **League of Legend API** for the data collection.

Since the LoL API isnt really well documented i will use a homemade **Python scrapper** for the **op.gg** website wich contains really interesting informations.
Most of the data is coming from the scrapper named datascrapper.py in the project which uses two dependencies :
**BeautifulSoup**
and
**request**

