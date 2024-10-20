import requests

""" response = requests.get("https://official-joke-api.appspot.com/random_joke")
#print(response.content)
"""""" print(response.status_code)
if response.status_code == 200:
    print('Success')
else:
    print('Error') """"""
response.raise_for_status()
print(response.json()['setup'])
print(response.json()['punchline']) """

parameters = {
    'lat': 48.856613,
    'lng':2.352222,
    'formatted':0
}
response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
print(data['results'])
