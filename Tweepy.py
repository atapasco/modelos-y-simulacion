from multiprocessing.connection import Listener
from re import A
import tweepy
from tweepy import StreamingClient
import json 

twitters = []
usuarios = []
twitsYUsuarios = []

api_key = 'rQp7PTADjQWapSkQHeGPMFgah'
api_key_secret = '2xryn6rpxkP3lzkkS7Pr4KmlBgxVO57yccSIBykE5igyhKgVWR api key secret'

access_token = '1568681787097845760-3tNUahK6HEQS3ShnWjLdUPpRbRhWzV'
access_token_secret = 'yTfE5t4QqLkePgZRe6OX6aotBHrbzLkbQUD5OlST6WXbB'

Bearer_Token = "AAAAAAAAAAAAAAAAAAAAAH7BgwEAAAAA98QAK4a4%2Fk6WRGx7gsNL0FgysvE%3DrWrpsOe5C9ZatftXzJsqlDsXlDPDvSZLxRFULw8wLE2q3JpZbE"
client = tweepy.Client(Bearer_Token,api_key,api_key_secret,access_token,access_token_secret)

totalTwits = 50


class Twitts:
    def twittsPorSemana(self, tema):
        tweets = client.search_recent_tweets(tema+"(lang:es)", max_results=100, expansions='entities.mentions.username,attachments.poll_ids')
        
        

        for item in tweets.data:
            twitters.append(item.text) 

        for item in tweets.includes['users']:
            usuarios.append(item)

        for i in range(50):
            twitsYUsuarios.append(str(usuarios[i])+": "+str(twitters[i])+"\n\n\n")

        twitters.clear()
        usuarios.clear()

        return twitsYUsuarios


    def twittsTotales(self):
        return totalTwits







    

