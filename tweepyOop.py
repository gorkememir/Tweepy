import time
import pprint
import tweepy

class TweepyOop:

    def __init__(self):

        self.accKey = input("accKey gir: ")
        self.accSec = input("accSec gir: ")
        self.consKey = input("consKey gir: ")
        self.consSec = input("consSec gir: ")

        self.auth = tweepy.OAuthHandler(self.accKey, self.accSec)
        self.auth.set_access_token(self.consKey, self.consSec)
        self.api = tweepy.API(self.auth)

user1 = TweepyOop()

print(user1.accKey)
print(user1.accSec)


'''
    #Create a list called 'followerIds' that contains the userIDs(int) ofdd
    #the followers of a specific account (specified after screen_name="")
    followerIds = []
    for page in tweepy.Cursor(api.followers_ids, screen_name="grkmdfg").pages():
        followerIds.extend(page)
        time.sleep(5)

    #Create a list called 'followingIds' that contains the userIDs(int) of
    #the accounts followed by a specific account (specified after screen_name="")
    followingIds = []
    for page in tweepy.Cursor(api.friends_ids, screen_name="grkmdfg").pages():
        followingIds.extend(page)
        time.sleep(5)

    #Create a list of traitors who don't follow back
    traitors = list(set(followingIds)-set(followerIds))

    #Unfollows the traitors with less than 100 tweets.
    #COMMENT THIS AND UNCOMMENT THE FOLLOWING BLOCK IF YOU WANT TO SEE THE LIST FIRST BEFORE UNFOLLOWING.
    #CANNOT UNDO!!!
    for traitor in traitors:
        traitorTweetCount = api.get_user(traitor).statuses_count
        traitorFollowerCount = api.get_user(traitor).followers_count
        if traitorFollowerCount < 100:
            api.destroy_friendship(traitor)
'''

''' Txt File Creator Block
    #Checks traitors' tweet counts, creates a list of traitors who has less than 1000 followers.
    inactiveTraitorList = []
    for traitor in traitors:
        traitorName = api.get_user(traitor).screen_name
        traitorTweetCount = api.get_user(traitor).statuses_count
        traitorFollowerCount = api.get_user(traitor).followers_count
        if traitorFollowerCount < 1000:
            currentTraitor = traitorName + " " + "Tweet Count: " + str(traitorTweetCount) + "Follower Count: " + str(traitorFollowerCount)
            inactiveTraitorList.append(currentTraitor)
    
    #Writes the traitors with less than 100 tweets in a file called 'inactiveTraitors100.txt'
    inactiveTraitorTxt = open('C:\\temp\\inactiveTraitors100' + '.txt', 'w')
    pprint.pprint(inactiveTraitorList, inactiveTraitorTxt)
'''