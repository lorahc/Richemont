
import requests
from api_communication import *
import sys
import os


filename = sys.argv[1]

title=os.path.splitext(os.path.basename(filename))[0]

audio_url = upload(filename)
save_word_timestamps(audio_url, title)
