import requests


url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    'title' : 'Sample title',
    'body' : 'we are testing post request',
    'userId' : 1
}

response = requests.post(url, json=data)
print(response.json())
"""if response.status_code == 201:
    print('Success')
else: 
    print('Failed')"""