import instagram_explore as ie 
# import instaloader
# import requests
# from datetime import datetime
# import json 
from instabot import Bot
# import os
# import time as time
import urllib
image = urllib.request.URLopener()


# using the tag method 
# L = instaloader.Instaloader()

bot = Bot()

boobTag = input("From what hashtag? ")
result = ie.tag(boobTag) 

bot.login(username = "ventilgamingofficial",  
          password = "gotitbro64") 

# result.data['edge_hashtag_to_media']['edges'][0]['node'].keys()

sexy = result.data['edge_hashtag_to_top_posts']['edges'][0]['node']['thumbnail_src']

print(result.data['edge_hashtag_to_top_posts']['edges'][0]['node']['thumbnail_src'])

# def getImage(url):
#     response = requests.get(url)
#     file = open("sample.jpg", "wb")
#     file.write(response.content)
#     file.close()

boobCount = input("How many boobs?")

for i in range(int(boobCount)):
    # getImage(sexy)
    try:
        sexy = result.data['edge_hashtag_to_top_posts']['edges'][i]['node']['thumbnail_src']
        imgName = (str(i) + ".jpg")
        image.retrieve(sexy, imgName)
    except:
        print("no worky worky")