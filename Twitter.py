from textblob import TextBlob
import IMDb
import FamousBirthday
import tweepy
import numpy as np

ckey = 'YZKrxbNsjgbTcEZCvzn8H0tXU'
csecret = 'pHzdAZ7jSC8LMTu0HrbRaVgziXwCKUY0hY4P099Bi6AMIorddf'

atoken = '2286472760-ivIvccDrBMlBCdzvAEhgg8bqr5PuY2nzk5xbl8l'
asecret = '7Xl8Ug01keiybeguDpLHusNAxUWObqpJBDzxpAmo1fufg'

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# def get_label(analysis, threshold = 0):
#     if analysis.sentiment[0]>threshold:
#         return 'Positive'
#     elif analysis.sentiment[0]<threshold:
#         return 'Negative'
#     else:
# 	    return 'Neutral'

celeb_names = {}
# celebNames = {}
celeb_names = IMDb.celeb_name  + FamousBirthday.celeb_name
# sorted(celeb_names)

all_polarities = {}
for candidate in celeb_names:
    this_candidate_polarities = []
    this_candidate_tweets = api.search(candidate)
    i = 0
    mean = 0
    for tweet in this_candidate_tweets:
        # print tweet.text
        i = i + 1
        analysis = TextBlob(tweet.text)
        this_candidate_polarities.append(analysis.sentiment[0])
    if i != 0:
        mean = sum(this_candidate_polarities)/ i
        all_polarities[candidate] = {'mean' : mean}
        # print 'Celebrity Name: ' + candidate + '\t' + 'Mean Polarity: ' + str(mean)
# print all_polarities

for key,value in all_polarities.items():
    print  'Celebrity Name: ' + key + '\t' + ', Mean Polarity: ' + str(value['mean'])
