print("run stalkSetup.py before the first time running this, only need to run it once")
import instagram_explore as ie 
from instabot import Bot
import urllib
image = urllib.request.URLopener()

bot = Bot()

boobTag = input("From what hashtag? ")
result = ie.tag(boobTag) 

bot.login(username = "ventilgamingofficial",  
          password = "gotitbro64") 


boobCount = input("How many boobs?")

for i in range(int(boobCount)):
    try:
        sexy = result.data['edge_hashtag_to_top_posts']['edges'][i]['node']['thumbnail_src']
        imgName = (str(i) + ".jpg")
        image.retrieve(sexy, imgName)
    except:
        print("no worky worky")