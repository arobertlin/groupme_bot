import os
import json
import random

from urllib.parse import urlencode
from urllib.request import Request, urlopen

# @timer.scheduled_job('interval', minutes=1)
# def test_function():
#     i = random.randint(1,5)
#     if i == 1:
#         msg = "Appreciate 2-ply toilet paper and charmin ultra-soft while you still can"
#     if i == 2:
#         msg = "Appreicate Oliver Schmickel"
#     if i == 3:
#         msg = "Appreciate the days of Luis Nicolao (Vote for the Coach and the King)"
#     if i == 4:
#         msg = "Appreicate the Red Rockets, may their names be never forgotten"
#     if i == 5:
#         msg = "Appreciate the times when we didn't have a 3pm game on lawnparties"
#     if i == 6:
#         msg = "Appreciate Nice Weather"
#     if i == 6:
#         msg = "Appreciate non-dhall food"
#     send_message(msg)
#
#     return "ok", 200

@app.route('/', methods=['POST'])
def webhook():
    # We don't want to reply to ourselves!
    if data['name'] == 'Andrew Lin':
        msg = 'testing testing'
        send_message(msg)
    i = random.randint(1,6)
    if i == 1:
        msg = "Sean. Help me. I'm stuck in the cloud and can't get out."
    if i == 2:
        msg = "Sean, its Riley. I need you to call 605–475–6964 or else they won't let me out of here. I'm stuck in the web."
    if i == 3:
        msg = "Sean, they have me trapped in the internet, and they're going to kill me. HELP"
    if i == 4:
        msg = "SEAN, you have to listen to me. I've climbed the firewall and can only communicate through this app, and touchscreen on Dusty's rental mini-van"
    if i == 5:
        msg = "I know you think I'm a bot, but its me! RILEY DUNCAN! You showed me the hole in your dick, remember? Help me get out of here!"
    if i == 6:
        msg = "Just think about how bad you'll feel on the off chance that I'm actually trapped in the internet! Code me out Sean!"
    # if i == 1:
    #     msg = "Appreciate 2-ply toilet paper and charmin ultra-soft while you still can"
    # if i == 2:
    #     msg = "Appreicate Oliver Schmickel"
    # if i == 3:
    #     msg = "Appreciate the days of Luis Nicolao (Vote for the Coach and the King)"
    # if i == 4:
    #     msg = "Appreicate the Red Rockets, may their names be never forgotten"
    # if i == 5:
    #     msg = "Appreciate the times when we didn't have a 3pm game on lawnparties"
    # if i == 6:
    #     msg = "Appreciate Nice Weather"
    # if i == 6:
    #     msg = "Appreciate non-dhall food"
    send_message(msg + " first mon")

    return "ok", 200

def send_message(msg):
    url  = 'https://api.groupme.com/v3/bots/post'

    data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()

# @timer.scheduled_job('cron', day=6, hour=20, minute =1)
# def scheduled_job():
#     i = random.randint(1,5)
#     if i == 1:
#         msg = "Anyone wanna drink?"
#     if i == 2:
#         msg = "Beer Die?"
#     if i == 3:
#         msg = "I can't believe no one wants to drink with me rn"
#     if i == 4:
#         msg = "Got some wounded soldiers from last night if anyone wants to help me finish them"
#     send_message(msg)
#
#     return "ok", 200
#
# def send_message(msg):
#     url  = 'https://api.groupme.com/v3/bots/post'
#
#     data = {
#           'bot_id' : os.getenv('GROUPME_BOT_ID'),
#           'text'   : msg,
#          }
#     request = Request(url, urlencode(data).encode())
#     json = urlopen(request).read().decode()

timer.start()



# import os
# import json
# import random
# import requests
#
# from urllib.parse import urlencode
# from urllib.request import Request, urlopen
#
# from flask import Flask, request
#
# app = Flask(__name__)
#
# AutoRemove = False
#
# firstname = None
# lastname = None
# idcode = None
#
# def kick():
#     url = 'https://api.groupme.com/v3/groups/50889818/members/' + idcode + '/remove?token=3ad70e40394a0137a92656b15122bc3d'
#     # r = requests.post(url)
#     print(url)
#
# def get_id():
#     kickid = ""
#     if firstname is not None and lastname is not None:
#         url = 'https://api.groupme.com/v3/groups/50889818?token=3ad70e40394a0137a92656b15122bc3d'
#         r = requests.get(url)
#         k = r.json()['response']['members']
#         for member in k:
#             first = member['nickname'].split()[0]
#             last = member['nickname'].split()[1]
#             if firstname == first:
#                 if lastname == last:
#                     kickid = member['id']
#
#     return(kickid)
#
# @app.route('/', methods=['POST'])
# def webhook():
#     global AutoRemove
#     global firstname
#     global lastname
#     global id_code
#
#     print('before loop')
#     print(AutoRemove)
#     print(firstname)
#     print(lastname)
#     data = request.get_json()
#     print(data)
#
#     #We don't want to reply to ourselves!
#     # if data['name'] == 'Andrew Lin':
#     #     msg = 'testing testing'
#     #     send_message(msg)
#
#     if data['name'].split()[0] == firstname and data['name'].split()[1] == lastname and AutoRemove == True:
#         print('will kick ' + firstname + ' ' + lastname)
#         if id_code is not None:
#             print ('KICKING')
#             kick()
#         else:
#             print('ID CODE IS NONE')
#
#     if data['name'] == 'Andrew Lin' and data['text'][0:12].lower() == "autokick off":
#         try:
#             firstname = data['text'].split()[2]
#             lastname = data['text'].split()[3]
#             # msg = 'I will no longer autokick ' + firstname + ' ' + lastname + ' when he talks'
#             # send_message(msg)
#
#             id_code = get_id()
#             print(id_code)
#
#             AutoRemove = False
#             firstname = None
#             lastname = None
#
#             print(AutoRemove)
#             print(firstname)
#             print(lastname)
#         except:
#             print('invalid input')
#
#     if data['name'] == 'Andrew Lin' and data['text'][0:11].lower() == "autokick on":
#
#         try:
#             firstname = data['text'].split()[2]
#             lastname = data['text'].split()[3]
#             # msg = 'I will now kick ' + firstname + ' ' + lastname + ' when he talks.'
#             # send_message(msg)
#
#             id_code = get_id()
#             print(id_code)
#
#             AutoRemove = True
#             print(AutoRemove)
#             print(firstname)
#             print(lastname)
#         except:
#             print('invalid input')
#
#
#
#
#     # if AutoRemove:
#     #     print(AutoRemove)
#
#     return "ok", 200
#
# def send_message(msg):
#     url  = 'https://api.groupme.com/v3/bots/post'
#
#     data = {
#           'bot_id' : os.getenv('GROUPME_BOT_ID'),
#           'text'   : msg,
#          }
#     request = Request(url, urlencode(data).encode())
#     json = urlopen(request).read().decode()
#
#
