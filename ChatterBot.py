# Dependencies
import tweepy
import time
import json
from os import environ
#from config import consumer_key, consumer_secret, access_token, access_token_secret

# Twitter API Keys
consumer_key = environ.get('consumer_key')
consumer_secret = environ.get('consumer_secret')
access_token = environ.get('access_token')
access_token_secret = environ.get('access_token_secret')

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(f'Testing twitter bot again and again! This is Tweet {tweet_number}!')

# Create a function that calls the TweetOut function every minute
counter = 0

# Infinite loop
while(counter<5):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(30)

    # Add 1 to the counter prior to re-running the loop
    counter += 1