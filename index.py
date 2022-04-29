import discord
import json
with open('config.json') as f:
	config = json.load(f)
with open('botInfo.json') as f:
	botInfo = json.load(f)

	
import random as r
import shutil as sh
import threading
import time as t
import datetime as d
import shlex
from os.path import exists

version = (f'v{botInfo["currentVersion"]}')
if config['isDev'] :
	version += '-dev'