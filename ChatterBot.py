# Dependencies
import tweepy
import time
import json
from os import environ
#import requests
import datetime
import openweathermapy.core as owm
#from config import *

# API Keys
#consumer_key = consumer_key
#consumer_secret = consumer_secret
#access_token = access_token
#access_token_secret = access_token_secret
#weather_api_key = weather_api_key

consumer_key = environ.get('consumer_key')
consumer_secret = environ.get('consumer_secret')
access_token = environ.get('access_token')
access_token_secret = environ.get('access_token_secret')
weather_api_key = environ.get('weather_api_key')

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Create a function that tweets
def WeatherBot():
    
    #auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    #auth.set_access_token(access_token, access_token_secret)
    #api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    
    data = []
    cities = ['Yekaterinburg', 'Washington']
    settings = {"units": "metric", "appid": weather_api_key} 
    curtime = datetime.datetime.now().strftime('%H:%M:%S %d-%m-%y ')
    
    for city in cities:
        data.append(owm.get_current(city, **settings))
    
    search = ['name', 'sys.country', 'main.temp','main.humidity', 'clouds.all', 'wind.speed']
    
    ext_data = [city(*search) for city in data]
    
    tweet = [f'On {curtime} ']
    
    for x in range(len(cities)):
        tweet.append(f'Temperature in {ext_data[x][0]}, {ext_data[x][1]}: {ext_data[x][2]}C°, Humidity: \
{ext_data[x][3]}, Cloudiness: {ext_data[x][4]}, Wind Speed: {ext_data[x][5]}KmH.')

    ans = '\n'.join((tweet))
    
    api.update_status(f'{ans}')
    
    print('done')

# Infinite loop

while(True):
    WeatherBot()
    time.sleep(40000)
