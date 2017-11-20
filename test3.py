import os
import io
import tweepy
from tweepy import OAuthHandler
 
consumer_key = '3eRdmwDRW7ezS0ysg51i8I2yx'
consumer_secret = 'x4LT2G2otn7UYBG6alP2P7tSBNJ0HILUJHUbSFmhswI5BX7qHf'
access_token = '2661873764-42So7jeZ5mrPYNwWovPfrrj6LPVvabm7peeQEcl'
access_secret = 'QoQL9w6I44Eb3DmmPQAVgdmzpo1vLkVRfWqBvbujxBrwE'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
path="C:\\Users\\MicroComSci\\Documents\\FetchDataFromTweet\\tweet"
countline=1

#for status in tweepy.Cursor(api.home_timeline).items(10):
for status in tweepy.Cursor(api.user_timeline, id="nontakhon").items(10):
   #str dateToString=print(" "+status.created_at)
    #dateOnly=dateToString
    stringDate=status.created_at.strftime('%d%m%Y')
    pathfile=createdFolder(path,folder)+countline
    day_file=open(pathfile,'a')
    day_file.write(stringDate+"  "+status.text)
    print(a)
    


def createdFolder(path,folder):
    folderCreateCheck=path+"\\"+folde
    if  not os.path.exists(folderCreateCheck):
    os.makedirs(folderCreateCheck)
    SetNewCount()
    print("OK,Creaated"+folderCreateCheck)
    return folderCreateCheck

def SetNewCount():
    countline=1
    