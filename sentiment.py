import requests

url = 'http://text-processing.com/api/sentiment/'

user_text = input("Enter text for sentiment analysis: ")

myobj = {'text': user_text}

response = requests.post(url, data=myobj)

print(response.json())
