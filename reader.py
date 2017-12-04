#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, random, re, os, glob

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = ############################################
CONSUMER_SECRET = ############################################
ACCESS_KEY = ###########################################
ACCESS_SECRET = ###########################################
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

twts = api.search(q="@me0wb0t #meow")
#list of specific strings we want to check for in Tweets

for s in twts:
    found = False
    with open('files/tweets.txt','r') as f:
        line = f.readline() #read first
        while line:
            if line.startswith(str(s.id)):
                found = True
                print("item found")
            line = f.readline()
    with open('files/tweets.txt','a+') as f:
        if found:
            print(str(s.id)+" Exists in the document!")
        else:
            f.write(str(s.id)+"\n")
