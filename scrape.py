#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import tweepy
import re
import arrow
from pymongo import MongoClient
#from pymongo import InsertOne, DeleteOne, ReplaceOne

config = yaml.safe_load(open("config.yml"))

consumer_key = config['consumer_key']
consumer_secret = config['consumer_secret']
access_token = config['access_token']
access_token_secret = config['access_token_secret']

print consumer_key, consumer_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.user_timeline("NEAsg")
final_tweets = []
tweets=[]

for tweet in public_tweets:
    if re.match('3-hour(.*)', tweet.text):
        print tweet.text
        tweets.append(tweet)

for tweet in tweets:
    p = "is (\d+)[. ]"
    m = re.findall(p,tweet.text, re.DOTALL)
    time_posted = arrow.get(str(tweet.created_at).strip(), "YYYY-MM-DD HH:mm:ss").timestamp

    obj = {
        "timestamp": time_posted,
        "psi": m[0]
    }
    final_tweets.append(obj)

print final_tweets


client = MongoClient()
db = client.haze
#db.psi.insert_many(final_tweets)
for tweet in final_tweets:
    db.psi.update(tweet, {"$set": tweet}, upsert=True)

print '-- updated ' + str(arrow.now().to('+07:00')) + ' --'
