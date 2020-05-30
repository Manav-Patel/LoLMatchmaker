import requests
from bs4 import BeautifulSoup


def infoScraper(ign):
    print ("asd")
        
    URL = 'https://na.op.gg/summoner/userName='+ign
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    roughRank = str(soup.find_all(class_='TierRank'))
    roughLP = str(soup.find_all(class_='LeaguePoints'))

    print(roughRank[23:29]) 
    print(roughLP[33:36])

    return [roughRank, roughLP]

def infoToNum(rank, lp):
    return 1

#test input: arcaras,clanceejr,100 Tenacity,IllIlIlIl,BladeGO,jojopyun 15,V1per1,Neøø,elise player,DISCORD TARZANED
def main(): 
    userSummonerNames = input('Enter 10 summoner names (summoners have to be ranked) separated by commas (no spaces required after commas): ')
    #region = input('Enter your region (na, euw, eune, etc...): ')
    splitNames = (str(userSummonerNames)).split(',')
    
    if (len(splitNames) == 10):
        playerDict = {}
        for name in splitNames:
            print(infoScraper(name))
            playerDict[name] = 0
        
    else:
        print("Invalid number of names entered") 


#Runs the main function
if __name__ == "__main__":
    main()


input('Press ENTER to exit')

#TierRank
#LeaguePoints