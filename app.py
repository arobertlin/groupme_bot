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

    if data['name'] == 'Andrew Lin' and data['text'][0:12].lower() == "autokick off":
        try:
            firstname = msg['text'].split()[2]
            lastname = msg['text'].split()[3]
            msg = 'I will no longer autokick' + firstname + ' ' + lastname + 'when he talks'
            send_message(msg)
            AutoRemove = False
            print(AutoRemove)
        finally:
            print('invalid input')

    if data['name'] == 'Andrew Lin' and data['text'][0:11].lower() == "autokick on":
        try:
            firstname = msg['text'].split()[2]
            lastname = msg['text'].split()[3]
            msg = 'I will now kick' + firstname + ' ' + lastname + 'when he talks.'
            send_message(msg)
            AutoRemove = True
            print(AutoRemove)
        finally:
            print('invalid input')

    # if AutoRemove:
    #     print(AutoRemove)

    return "ok", 200

def send_message(msg):
    url  = 'https://api.groupme.com/v3/bots/post'

    data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()


