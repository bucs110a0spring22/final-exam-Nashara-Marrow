import requests 
import CatAPI
import AnimeAPI
#response = requests.get('https://api.thecatapi.com/v1/images/search')
#CAT = response.json()


def main():
    #Proxy Class
    capi = CatAPI.CatAPI()
    results = capi.get()
    for catpic in results: 
      answers = catpic['results']
    print(answers)

def kitty():
    #Proxy Class
    aapi = AnimeAPI.AnimeAPI()
    results = aapi.get()
    for anime in results: 
      answers = anime['facts'] 
    print(answers)

main()