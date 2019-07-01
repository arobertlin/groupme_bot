import os
import json
import random
import requests

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

AutoRemove = True

firstname = None
lastname = None
idcode = None

def kick():
    url = 'https://api.groupme.com/v3/groups/50889818/members/' + idcode + '/remove?token=3ad70e40394a0137a92656b15122bc3d'
    # r = requests.post(url)
    print(url)

def get_id():
    kickid = ""
    if firstname is not None and lastname is not None:
        url = 'https://api.groupme.com/v3/groups/50889818?token=3ad70e40394a0137a92656b15122bc3d'
        r = requests.get(url)
        k = r.json()['response']['members']
        for member in k:
            first = member['nickname'].split()[0]
            last = member['nickname'].split()[1]
            if firstname == first:
                if lastname == last:
                    kickid = member['id']

    return(kickid)

@app.route('/', methods=['POST'])
def webhook():
    global AutoRemove
    global firstname
    global lastname
    global id_code

    print(AutoRemove)
    print(firstname)
    print(lastname)
    data = request.get_json()
    print(data)

    #We don't want to reply to ourselves!
    # if data['name'] == 'Andrew Lin':
    #     msg = 'testing testing'
    #     send_message(msg)

    if data['name'].split()[0] == firstname and data['name'].split()[1] == lastname and AutoRemove == True:
        print('will kick ' + firstname + ' ' + lastname)
        if id_code is not None:
            print ('KICKING')
            kick()
        else:
            print('ID CODE IS NONE')

    if data['name'] == 'Andrew Lin' and data['text'][0:12].lower() == "autokick off":
        try:
            firstname = data['text'].split()[2]
            lastname = data['text'].split()[3]
            msg = 'I will no longer autokick ' + firstname + ' ' + lastname + ' when he talks'
            send_message(msg)

            id_code = get_id()
            print(id_code)

            AutoRemove = False
            firstname = None
            lastname = None

            print(AutoRemove)
        except:
            print('invalid input')

    if data['name'] == 'Andrew Lin' and data['text'][0:11].lower() == "autokick on":

        try:
            firstname = data['text'].split()[2]
            lastname = data['text'].split()[3]
            msg = 'I will now kick ' + firstname + ' ' + lastname + ' when he talks.'
            send_message(msg)

            id_code = get_id()
            print(id_code)

            AutoRemove = True
            print(AutoRemove)
        except:
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


