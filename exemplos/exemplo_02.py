import requests

url = "https://jsonplaceholder.typicode.com/comments"
params = {"postId":1} # Obter apenas comentários do postId 1 

# get
response = requests.get(url, params=params)

comentarios = response.json()

print(f"Encontrados {len(comentarios)} comentários")
