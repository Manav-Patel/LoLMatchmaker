import requests

def requestSummonerData(region, summonerName, APIKey):

    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + summonerName + "?api_key=" + APIKey
    print(URL)
    response = requests.get(URL)
    return response.json()

def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + APIKey
    print(URL)
    response = requests.get(URL)
    return response.json()
    

def main():
    print("\nEnter your region to get started")
    print("Type in one of the following regions or else the program wont work correctly:\n")
    print("NA or EUW (Note: You can add more regions by just changing up the URL!\n")

    region = (str)(raw_input('Type in one of the regions above: '))
    summonerName = (str)(raw_input('Type your Summoner Name here and DO NOT INCLUDE ANY SPACES: '))
    APIKey = (str)(raw_input('Copy and paste your API Key here: '))

    #I send these three pieces off to my requestData function which will create the URL and give me back a JSON that has the ID for that specific summoner.
    #Once again, what requestData returns is a JSON.
    responseJSON  = requestSummonerData(region, summonerName, APIKey)
    
    ID = responseJSON[summonerName]['id']
    ID = str(ID)
    print(ID)
    responseJSON2 = requestRankedData(region, ID, APIKey)
    print(responseJSON2[ID][0]['tier'])
    print(responseJSON2[ID][0]['entries'][0]['division'])
    print(responseJSON2[ID][0]['entries'][0]['leaguePoints'])

#This starts my program!
if __name__ == "__main__":
    main()