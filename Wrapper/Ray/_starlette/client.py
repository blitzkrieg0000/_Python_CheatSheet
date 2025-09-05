import requests

text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief"

response = requests.post("http://127.0.0.1:8000/", json=text)
de_text = response.text

print(de_text)