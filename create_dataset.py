import time
import tweepy
import csv
import sys
import json

tweets_list = []

with open('tweets_database.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:       
        tweets_list.append(row)
csvFile.close()

print(tweets_list)