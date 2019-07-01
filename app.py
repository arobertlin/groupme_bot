import os
import json
import random

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

AutoRemove = True

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)

    #We don't want to reply to ourselves!
    if data['name'] == 'Andrew Lin':
        msg = 'testing testing'
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


