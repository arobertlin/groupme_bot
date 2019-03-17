import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    #We don't want to reply to ourselves!
    if data['name'] == 'Christian McClain':
        msg = 'shut up, Christian'
        send_message(msg)

    if data['name'] == 'Andrew Lin':
        msg = "wow, I can't beleive im in Romania for the fifth time"
        send_message(msg)

    if data['name'] == 'Rohin Maganti':
        msg = "Roniiiiiii"
        send_message(msg)

    if data['name'] == 'Wesley Hibbs':
        msg = "Can you even hear me Wesley?"
        send_message(msg)

    if data['name'] == 'Easton Honaker':
        msg = "Bubo bubo bubo"
        send_message(msg)

    if data['name'] == 'Rohil Rai':
        msg = "miss you Rohil"
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
