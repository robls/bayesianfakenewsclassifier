import time
import tweepy
import csv
import sys
import json

# Autenticação do OAuth
# https://dev.twitter.com/apps
consumer_key= "6wRJ1aCS8pus8eel4NjKHXhkt"
consumer_secret = "Clzu38EZUwy36sBWzyKDAHGrpAbGYThwQqKb5YGT8GgCNFMnUl" 

access_token= "260529292-iSzMqq5KZeAcYr5SI565dsh06ODehE3xQEY3yCIP"
access_token_secret="ge9nM6HOM46sHkdHfDNzVDSLkF81SWkGzyBHkfarrDNG8"

# OAuth 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Interface criada.
api = tweepy.API(auth)

status = "1167088815275745281"
results = api.get_status(status)
#print(results)

csvfile = open('tweets_database.csv', 'a', newline='\n')

csvwriter = csv.writer(csvfile)

# 1 - Fake News 
# 0 - Noticias Verdadeiras 
# CATEGORIAS - POLITICA, ESPORTES, etc
# [ NOME DA CONTA, ID, TEXTO, CLASSIFICACAO]
csvwriter.writerow( [ bytes(results.user.screen_name, "utf-8").decode("cp1252"), 
                        bytes(status,"utf-8").decode("cp1252"),
                           bytes(results.text,"utf-8").decode("cp1252"),
                               1 ] )      