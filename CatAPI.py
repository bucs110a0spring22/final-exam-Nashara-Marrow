import requests 



class CatAPI:

    def __init__(self):
        self.url = f'https://api.thecatapi.com/v1/images/search'

    def get(self):
        r = requests.get(self.url)
        cats = r.json()
      
        if cats.get('results'):
            return cats['results']
        else:
            return None

    
        