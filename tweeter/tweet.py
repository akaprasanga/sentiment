import tweepy
import csv
import pandas as pd
import configparser

config = configparser.RawConfigParser()
config.read('tokens.cfg')
consumer_key = config.get('Main','consumer_key')
consumer_secret = config.get('Main','consumer_secret')
access_token = config.get('Main','access_token')
access_token_secret = config.get('Main','access_token_secret')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
print(api)
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#bitcoin",count=100,
                           lang="en",
                           since="2017-02-2").items(10):
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

# for tweets in tweepy.Cursor(api.user_timeline,id="BTCTN", count=100, lang="en").items(10):
#     print(tweets.created_at, tweets.text)
#     csvWriter.writerow([tweets.created_at, tweets.text.encode('utf-8')])