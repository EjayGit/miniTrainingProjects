import requests
import os

#ApiKey = 'e9edaf6ff60328c3c3118ebedd08d853'
ApiKey = os.environ.get('owm_api_key')
apiParam = {
    'q':'Paris',
    'appid': ApiKey,
    'cnt':8
}
endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
response = requests.get(endpoint, params=apiParam)
print(response.json())
print(ApiKey)