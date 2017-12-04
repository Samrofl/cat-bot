#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, random, re, os, glob, datetime

CONSUMER_KEY = ###########################################
CONSUMER_SECRET = ###########################################
ACCESS_KEY = ###########################################
ACCESS_SECRET = ###########################################
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

file_count=0;
bark_count=0;

for f in os.listdir("pics/."):
    ext = f.split(".")[1]
    if ext in ("jpg","png","jpeg"):
        file_count+=1
print("Image Count: "+str(file_count))

for f in os.listdir("bark/."):
    ext = f.split(".")[1]
    if ext in ("jpg","png","jpeg"):
        bark_count+=1
print("Bark Reaction Count: "+str(bark_count))
while True:
    #Randomly post an image
    value = random.randint(1,file_count)
    if glob.glob('pics/'+str(value)+'.*'):
        print("["+datetime.datetime.now().strftime('%H:%M:%S')+"] Item Posted: No. "+str(value))
        file=glob.glob('pics/'+str(value)+'.*')[0]
        api.update_with_media(file,"No. "+str(value))
    else:
        print("File not found: "+str(value))

    for x in range(1,60):
        value = random.randint(1,file_count)
        #Respond to #meow requests
        twts = api.search(q="@me0wb0t meow") #Searches for tweets

        #For each tweet, extract the ID and check if it has been replied to already.
        for s in twts:
            found = False
            with open('files/tweets.txt','r') as f:
                line = f.readline() #read first
                while line:
                    if line.startswith(str(s.id)):
                        found = True
                    line = f.readline()
            with open('files/tweets.txt','a+') as f:
                if not found:
                    if glob.glob('pics/'+str(value)+'.*'):
                        sn = s.user.screen_name
                        m="@%s meow" % (sn)
                        file=glob.glob('pics/'+str(value)+'.*')[0]
                        api.update_with_media(file,m,in_reply_to_status_id=s.id)
                        print("["+datetime.datetime.now().strftime('%H:%M:%S')+"] Replied to "+sn)
                    f.write(str(s.id)+"\n")

        #Respond to #bark requests
        twts = api.search(q="@me0wb0t #bark") #Searches for tweets with '#bark'
        twt2 = api.search(q="@me0wb0t #woof") #Searches for more tweets with '#woof'
        barkvalue = random.randint(1,bark_count)
        #For each tweet, extract the ID and check if it has been replied to already.
        for s in twts:
            found = False
            with open('files/tweets.txt','r') as f:
                line = f.readline() #read first
                while line:
                    if line.startswith(str(s.id)):
                        found = True
                    line = f.readline()
            with open('files/tweets.txt','a+') as f:
                if not found:
                    if glob.glob('bark/'+str(barkvalue)+'.*'):
                        sn = s.user.screen_name
                        bark="@%s" % (sn)
                        file=glob.glob('bark/'+str(barkvalue)+'.*')[0]
                        api.update_with_media(file,bark,in_reply_to_status_id=s.id)
                        print("["+datetime.datetime.now().strftime('%H:%M:%S')+"] Replied to "+sn)
                    f.write(str(s.id)+"\n")
        for s in twt2:
            found = False
            with open('files/tweets.txt','r') as f:
                line = f.readline() #read first
                while line:
                    if line.startswith(str(s.id)):
                        found = True
                    line = f.readline()
            with open('files/tweets.txt','a+') as f:
                if not found:
                    if glob.glob('bark/'+str(barkvalue)+'.*'):
                        sn = s.user.screen_name
                        bark="@%s" % (sn)
                        file=glob.glob('bark/'+str(barkvalue)+'.*')[0]
                        api.update_with_media(file,bark,in_reply_to_status_id=s.id)
                        print("["+datetime.datetime.now().strftime('%H:%M:%S')+"] Replied to "+sn)
                    f.write(str(s.id)+"\n")
        time.sleep(60)
