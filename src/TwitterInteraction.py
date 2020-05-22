from dotenv import load_dotenv
import os
import re
import json
import tweepy
load_dotenv()

class TwitterAccess :
    def __init__(self) :
        self.apiKey = os.getenv("API_PUB")
        self.apiPriv = os.getenv("API_PRIV")
        self.accessKey = os.getenv("ACCESS_PUB")
        self.accessPriv = os.getenv("ACCESS_PRIV")
        auth = tweepy.OAuthHandler(self.apiKey, self.apiPriv)
        auth.set_access_token(self.accessKey, self.accessPriv)
        self.tweepy = tweepy.API(auth)
        self.readTweets = {}
    
    def printKeys(self) :
        print(self.apiKey)
        print(self.apiPriv)
        print(self.accessKey)
        print(self.accessPriv)
    
    def testTweepy(self) :
        user = self.tweepy.get_user('twitter')
        print(user.screen_name)
        print(user.followers_count)
    
    def tweetBuy(self, price, qty) :
        message = "Buying %d shares of TSLA at a price of %d" % (qty, price)
        self.tweepy.update_status(message)
    
    def parseTweets(self, status) :
        parse = (lambda status :
            (status.id not in self.readTweets) and
            (re.search(r"([Tt][eS][sL][Al][a]?)", status.text) != None) and
            (9 < status.created_at.hour < 16))
        return parse(status)
    
    def getElonsTweets(self) :
        tweets = {}
        parse = (lambda status :
            (status.id not in self.readTweets) and
            (re.search(r"([Tt][eS][sL][Al][a]?)", status.text) != None))
        for page in tweepy.Cursor(self.tweepy.user_timeline,
            id='elonmusk').items(750) :
            if parse(page) :
                tweets[page.created_at] = page.text
                
        return tweets
    
    def sendMessage(self, recipient, message):
        user = self.tweepy.get_user(recipient)
        id = user.id
        self.tweepy.send_direct_message(id, message)
            

twit = TwitterAccess()
twit.sendMessage("SaraJane_8", "Hi lovey!! I'm sending this message from a python script hehe I love you!!")
#twit.getElonsTweets()
#twit.getElonsTweets()


