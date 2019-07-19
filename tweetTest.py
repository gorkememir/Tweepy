import time
import pprint
import tweepy

#Put your tokens (consumer and access) below to access twitter:
auth = tweepy.OAuthHandler('la6GIOnNNTgUrDT7i0CdOfjFP',
                           'yntJ0Lr6hXIslmVcJsISmSBXM1iJ2MYEVt5danvHM8PEBeBY4N')
auth.set_access_token('362381427-YWm5IUmM4SKjCntpAKrWK9Kv7V0cgf06B960T4yM',
                      '0ltVcOAvTNsAmqTcdFrAPMSFZKsUoOx1qBgTbxNW6MHxK')

#Tweepy object 'api' will authorize us to connect to twitter
api = tweepy.API(auth)

api.update_status("Hello")