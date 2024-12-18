import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

# get
response = requests.get(url)

# dados
data = response.json()
print(data)