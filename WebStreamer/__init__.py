# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

import logging
import os
import time
import random
import string
import subprocess
import requests
from .vars import Var
from WebStreamer.bot import StreamBot

import telegram.ext as tg
from dotenv import load_dotenv

load_dotenv('config.env')

def getConfig(name: str):
    return os.environ[name]
  
  try:
    SHORTENER = getConfig('SHORTENER')
    SHORTENER_API = getConfig('SHORTENER_API')
    if len(SHORTENER) == 0 or len(SHORTENER_API) == 0:
        raise KeyError
except KeyError:
    SHORTENER = None
    SHORTENER_API = None

print('\n')
print('------------------- Initalizing Telegram Bot -------------------')

StreamBot.start()
bot_info = StreamBot.get_me()
__version__ = 1.06
StartTime = time.time()


