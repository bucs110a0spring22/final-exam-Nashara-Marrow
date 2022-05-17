import requests 



class AnimeAPI:

    def __init__(self,facts=0):
        self.url = f'https://anime-facts={facts}-rest-api.herokuapp.com/api/v1'

    def get(self):
        r = requests.get(self.url)
        facts =r.json()
        if facts.get('facts'): 
          return facts['facts']
        else : 
          return None

      




