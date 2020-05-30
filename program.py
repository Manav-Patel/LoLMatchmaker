import requests
from bs4 import BeautifulSoup

def main(): 
    #userSummonerName = input('Enter your summoner name: ')
    #region = input('Enter your region (na, euw, eune, etc...): ')
    
    URL = 'https://na.op.gg/summoner/userName=arcaras'
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    roughRank = str(soup.find_all(class_='TierRank'))
    roughLP = str(soup.find_all(class_='LeaguePoints'))

    print(roughRank[23:29]) 
    print(roughLP[33:36])


#Runs the main function
if __name__ == "__main__":
    main()


input('Press ENTER to exit')

#TierRank
#LeaguePoints