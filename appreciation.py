import os
import json
import random

from apscheduler.schedulers.blocking import BlockingScheduler

from urllib.parse import urlencode
from urllib.request import Request, urlopen

app = Flask(__name__)

timer = BlockingScheduler()

@timer.scheduled_job('interval', minutes=1)
def test_function():
    print("This is a test")

@timer.scheduled_job('cron', day=6, hour=20, minute =1)
def scheduled_job():
    i = random.randint(1,5)
    if i == 1:
        msg = "Anyone wanna drink?"
    if i == 2:
        msg = "Beer Die?"
    if i == 3:
        msg = "I can't believe no one wants to drink with me rn"
    if i == 4:
        msg = "Got some wounded soldiers from last night if anyone wants to help me finish them"
    send_message(msg)

    return "ok", 200

def send_message(msg):
    url  = 'https://api.groupme.com/v3/bots/post'

    data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()

timer.start()


