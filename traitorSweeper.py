import time
import pprint
import tweepy

#Put your tokens (consumer and access) below to access twitter:
auth = tweepy.OAuthHandler('...',
                           '...')
auth.set_access_token('...',
                      '...')

#Tweepy object 'api' will authorize us to connect to twitter
api = tweepy.API(auth)

#Create a list called 'followerIds' that contains the userIDs(int) of
#the followers of a specific account (specified after screen_name="")
followerIds = []
for page in tweepy.Cursor(api.followers_ids, screen_name="...").pages():
    followerIds.extend(page)
    time.sleep(5)

#Create a list called 'followingIds' that contains the userIDs(int) of
#the accounts followed by a specific account (specified after screen_name="")
followingIds = []
for page in tweepy.Cursor(api.friends_ids, screen_name="").pages():
    followingIds.extend(page)
    time.sleep(5)

#Create a list of traitors who don't follow back
traitors = list(set(followingIds)-set(followerIds))

#Unfollows the traitors with less than 100 tweets.
#COMMENT THIS AND UNCOMMENT THE FOLLOWING BLOCK IF YOU WANT TO SEE THE LIST FIRST BEFORE UNFOLLOWING.
#CANNOT UNDO!!!
for traitor in traitors:
    traitorTweetCount = api.get_user(traitor).statuses_count
    if traitorTweetCount < 100:
        api.destroy_friendship(traitor)

'''
#Checks traitors' tweet counts, creates a list of traitors who tweeted less than 100 tweets.
inactiveTraitorList = []
for traitor in traitors:
    traitorName = api.get_user(traitor).screen_name
    traitorTweetCount = api.get_user(traitor).statuses_count
    if traitorTweetCount < 100:
        currentTraitor = traitorName + " " + str(traitorTweetCount)
        inactiveTraitorList.append(currentTraitor)

#Writes the traitors with less than 100 tweets in a file called 'inactiveTraitors100.txt'
inactiveTraitorTxt = open('C:\\temp\\inactiveTraitors100' + '.txt', 'w')
pprint.pprint(inactiveTraitorList, inactiveTraitorTxt)
'''

