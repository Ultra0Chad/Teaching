import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

installs = ['instagram_explore', 'instabot', 'urllib']

for i in installs:
    install(i)

# import instagram_explore as ie 
# import instaloader
# import requests
# from datetime import datetime
# import json 
# from instabot import Bot
# import os
# import time as time
# import urllib
