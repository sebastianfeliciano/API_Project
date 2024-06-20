import requests

# URL to get the latest item
latest_item_url = 'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'

# Get the ID of the most recent news story
response = requests.get(latest_item_url)
latest_item_id = response.json()[0]

item_details_url = f'https://hacker-news.firebaseio.com/v0/item/{latest_item_id}.json?print=pretty'

response = requests.get(item_details_url)
item_details = response.json()

if item_details.get('type') == 'story':
    title = item_details.get('title')
    author = item_details.get('by')
    url = item_details.get('url')

    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Link: {url}")
else:
    print("The latest item is not a story.")
