import requests

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)

data = response.json()

astronauts = [person['name'] for person in data['people']]

print(response.status_code)

for name in astronauts[:5]:
    print(name)