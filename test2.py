# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# We use the file saved from last step as example
tweets_filename = "C:\\Users\\MicroComSci\\Documents\\Python\\a.txt"
tweets_file = open(tweets_filename, "r")

for line in tweets_file:
    try:
        # Read in one line of the file, convert it into a json object 
        tweet = json.loads(line.strip())
        if 'text' in tweet: # only messages contains 'text' field is a tweet
            print("aa")
            print (tweet['id']) # This is the tweet's id
            print (tweet['created_at']) # when the tweet posted
            print (tweet['text']) # content of the tweet
                        
            print (tweet['user']['id']) # id of the user who posted the tweet
            print (tweet['user']['name']) # name of the user, e.g. "Wei Xu"
            print (tweet['user']['screen_name']) # name of the user account, e.g. "cocoweixu"

            hashtags = []
            print("I come from hastag")
            for hashtag in tweet['entities']['hashtags']:
            	hashtags.append(hashtag['text'])
            print (hashtags)

    except:
        # read in a line is not in JSON format (sometimes error occured)
        continue
    
    """
f=open(tweets_filename)
data=f.read()
print(data)
f.close()
"""


