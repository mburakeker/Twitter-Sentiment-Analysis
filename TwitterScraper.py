try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import re
from collections import Counter
import pandas as pd
from __init__ import *



def Scrape():
	oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
	twitter = Twitter(auth=oauth)
	iterator = twitter.search.tweets(q=TWEET_HASHTAG,count=100,tweet_mode='extended',lang=TWEET_LANGUAGE,exclude="retweets")
	df = pd.DataFrame(columns=['Tweet_ID','User_ID','Text','Favourite_Count'])
	for i in iterator['statuses']:
		df.loc[len(df)] = [i['id'],i['user']['id'],i['full_text'],i['favorite_count']]
	lowid = df["Tweet_ID"].min(),
	while(df["Tweet_ID"].count()<MAX_TWEET_COUNT):
		iterator = twitter.search.tweets(q=TWEET_HASHTAG,count=100,tweet_mode='extended',lang=TWEET_LANGUAGE,max_id=lowid,exclude="retweets")
		for i in iterator['statuses']:
			df.loc[len(df)] = [i['id'],i['user']['id'],i['full_text'],i['favorite_count']]
			print(str(df["Tweet_ID"].count()),end=" - ")
		lowid = df["Tweet_ID"].min()

	df = df.sort_values(by='Favourite_Count',ascending=False)

	print(df["Tweet_ID"].count())
	df = df.drop_duplicates(keep="first")
	df.to_csv("sampledataset.csv", encoding='utf-8', index=False)

