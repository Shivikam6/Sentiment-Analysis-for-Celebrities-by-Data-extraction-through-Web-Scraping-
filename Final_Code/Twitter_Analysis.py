from textblob import TextBlob   # To perform Text Sentiment Analysis
import IMDB_data                # Import IMDb_data class objects
import FamousBirthday_data      # Import FamousBirthday_data class objects
import tweepy                   # To call Twitter API
import numpy as np
import simplejson as json

ckey = 'YZKrxbNsjgbTcEZCvzn8H0tXU'  # Twitter Consumer key
csecret = 'pHzdAZ7jSC8LMTu0HrbRaVgziXwCKUY0hY4P099Bi6AMIorddf'  # Twitter Consumer Secret key

atoken = '2286472760-ivIvccDrBMlBCdzvAEhgg8bqr5PuY2nzk5xbl8l'   # Twitter Authorization Token
asecret = '7Xl8Ug01keiybeguDpLHusNAxUWObqpJBDzxpAmo1fufg'       # Twitter Authorization Secret Token

## Calling the Twitter APIs and fetching the Tweets
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

celeb_names = {}
celeb_names = IMDB_data.celeb_name + FamousBirthday_data.celeb_name

#Sentiment Polarity lies in between -1 to 1
all_polarities = {}
for candidate in celeb_names:
    this_candidate_polarities = []
    this_candidate_tweets = api.search(candidate)
    i = 0
    mean = 0
    for tweet in this_candidate_tweets:
        i = i + 1
        analysis = TextBlob(tweet.text)
        this_candidate_polarities.append(analysis.sentiment[0])
    if i != 0:
        mean = sum(this_candidate_polarities)/ i
        all_polarities[candidate] = {'mean' : mean}

## Saving the data in one JSON file called Result.json
with open('Result.json', 'w') as fp:
    json.dump(all_polarities, fp)
    
# for key,value in all_polarities.items():
#     print  'Celebrity Name: ' + key + '\t' + ', Mean Polarity: ' + str(value['mean'])
