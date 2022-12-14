# import requests

# class API:
#   def __init__(self,api_key):
#     self.api_key = api_key

# def search(self,query,search_type='',limit=10,page1):
#   url = f'http://ws.audioscrobbler.com/2.0/?method=album.search&album=believe&api_key=YOUR_API_KEY&format=json'
#   response = requests.get(url)
#   data = response.get(url)
#   data = response.json()
#   return data 

import requests

class LastFmAPI:
    API_ROOT = 'https://ws.audioscrobbler.com/2.0/'

    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, query, search_type='track', limit=1, page=1):
        params = {
            'method': 'track.search',
            'track': query,
            'api_key': self.api_key,
            'format': 'json',
            'limit': limit,
            'page': page
        }

        response = requests.get(self.API_ROOT, params=params)
        return response.json()
