import datetime
import csv
import TwitterInteraction 

def parseDateTime(dt):
    dt = dt.split(' ')
    date = dt[0].split('-')
    time = dt[1].split(':')
    ret = datetime.datetime(
        int(date[0]), int(date[1]), int(date[2]),
        hour=(int(time[0]) + 4), minute=int(time[1]))
    return ret

def parseRow(dictionary, row):
    pOpen = float(row[1])
    pClose = float(row[2])
    date = parseDateTime(row[0])
    dictionary[date] = [pOpen, pClose]

def parseCSV(dictionary):
    with open("marketData.csv", "r") as csvFile :
        reader = csv.reader(csvFile, delimiter=',')
        for row in reader:
            parseRow(dictionary, row)

def pairTweetToMarket(marketDictionary, tweetDictionary):
    pairs = []
    for date in tweetDictionary:
        temp = date.replace(minute=(date.minute - date.minute % 15), second=0, microsecond=0)
        if temp in marketDictionary:
            print(date)
            print(
                "Tweet: " + tweetDictionary[date] +
                " Price Before: %f, Price After:%f" % (marketDictionary[temp.replace(hour=13, minute=30)][0],
                marketDictionary[temp.replace(hour=19, minute=45)][1])
            )

def generateTrainingData():
    marketDictionary = {}
    twit = TwitterInteraction.TwitterAccess()
    tweetDictionary = twit.getElonsTweets()
    parseCSV(marketDictionary)
    pairTweetToMarket(marketDictionary, tweetDictionary)

generateTrainingData()
