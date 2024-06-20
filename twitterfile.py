import tweepy
import json

api_key = '1LHA4wSfQonh0prq2j4KKHCZr'
api_key_secret = 'SKNHJwlezq139t1LfdxAZVuGc2lUK6JnNnLfcjvkN4Mg8LAmnm'
access_token = '1803660694442876930-exsMZQ1qWGtySgxyqJDnTeXDjldWNJ'
access_token_secret = 'fMzEs6ocpRdNzR3k2Z5H7gspqU8RoMbbdD9aytdlHQ41Z'


auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)


try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

tweet_text = "Hello from Tweepy!"
try:
    api.update_status(status=tweet_text)
    print("Tweet posted successfully")
except Exception as e:
    print(f"Error posting tweet: {e}")
