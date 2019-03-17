import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    We don't want to reply to ourselves!
    if data['name'] != 'Lyric Enright' and data['name'] == 'Christian McClain':
        msg = 'shut up, Christian'
        send_message(msg)

    if data['name'] != 'Lyric Enright' and data['name'] == 'Rohil Rai':
        msg = "Rohil you're hot"
        send_message(msg)

    if data['name'] != 'Lyric Enright' and data['name'] == 'Rohin Maganti':
        msg = "Roooniiii"
        send_message(msg)

    if data['name'] != 'Lyric Enright' and data['name'] == 'Wesley Hibbs':
        msg = "Miss you Wesley"
        send_message(msg)

    if data['name'] != 'Lyric Enright' and data['name'] == 'Easton Honaker':
        msg = "Hi Easton!"
        send_message(msg)

    if data['name'] != 'Lyric Enright' and data['name'] == 'Andrew Lin':
        msg = "Hi Andrew!"
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
