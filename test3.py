import tweepy
from tweepy import OAuthHandler
 
consumer_key = '3eRdmwDRW7ezS0ysg51i8I2yx'
consumer_secret = 'x4LT2G2otn7UYBG6alP2P7tSBNJ0HILUJHUbSFmhswI5BX7qHf'
access_token = '2661873764-42So7jeZ5mrPYNwWovPfrrj6LPVvabm7peeQEcl'
access_secret = 'QoQL9w6I44Eb3DmmPQAVgdmzpo1vLkVRfWqBvbujxBrwE'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


#for status in tweepy.Cursor(api.home_timeline).items(10):
for status in tweepy.Cursor(api.user_timeline, id="nontakhon").items(10):
    # Process a single status
    print("\n")
    print(status.text,status.created_at)
    
