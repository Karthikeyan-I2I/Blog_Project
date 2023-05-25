import requests
from config.config import MyConfigClass

class MyNewsDataClass:
    def __init__(self):
        # Initialize any required resources or dependencies here
        pass
    
    def get_data(self):
        api_setting = MyConfigClass().get_apisetting()
        apikey =  api_setting.apikey
        url = api_setting.apiurl
        urls =f'{url}{apikey}'
        response = requests.get(urls)
        data = response.json()
        articles = data['articles']
        return articles
    

    
    
