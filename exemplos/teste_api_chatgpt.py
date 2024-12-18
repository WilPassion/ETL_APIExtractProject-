import requests
import json

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Qual é a capital da Inglaterra?"}]
}

response = requests.post(url, headers=headers, json=data)

print(response.json())  # Para ver a resposta em formato JSON
