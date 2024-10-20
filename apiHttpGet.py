import requests


url = 'https://jsonplaceholder.typicode.com/posts/6'

data = {
    'body' : 'bar bar bar',
}

#response = requests.post(url, json=data)
response = requests.patch(url,data)
print(response.json())