import requests


url = 'https://jsonplaceholder.typicode.com/posts/6'

data = {
    'body' : 'bar bar bar',
}

#response = requests.post(url, json=data)
response = requests.delete(url)
print(response.status_code)