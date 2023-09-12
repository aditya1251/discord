from pymongo import MongoClient
import time
import threading
from config import Your_data_base
import requests
import random

password = 'QRFfsca9UaLUH9H2'
cluster_url = 'mongodb+srv://uchisasuke468:' + \
    password + '@cluster0.byr4qsl.mongodb.net/'

client = MongoClient(cluster_url)

db = client['BNSL']

cli = Your_data_base

data = db[cli]

url = "https://discord.com/api/v9/channels/1144174264128389181/messages"

def main2():
    time.sleep(56400)
    while True:
        dat = data.find_one({'cli':cli})
        if dat:
            for aut in dat['auths']:
                try:
                    auth = {'authorization':aut}
                    msg = {'content':'!daily'}
                    requests.post(url,headers=auth,data=msg)
                    time.sleep(10)
                except Exception:
                    continue
        time.sleep(86400)

time_thread = threading.Thread(target=main2)
time_thread.start()

def main3():
    while True:
        dat = data.find_one({'cli':cli})
        if dat:
            for aut in dat['auths']:
                try:
                    auth = {'authorization':aut}
                    msg = {'content':'!guess 10'}
                    requests.post(url,headers=auth,data=msg)
                except Exception:
                    continue
            i = 1
            while i <= 5:  
                for aut in dat['auths']:
                    smsg2 = str(random.randrange(1,100))
                    i += 1
                    try:
                        auth = {'authorization':aut}
                        msg = {'content':smsg2}
                        requests.post(url,headers=auth,data=msg)
                    except Exception:
                        pass
                time.sleep(62)
        time.sleep(3600)

time_thread = threading.Thread(target=main3)
time_thread.start()

while True:
    dat = data.find_one({'cli':cli})
    if dat:
        for aut in dat['auths']:
            try:
                auth = {'authorization':aut}
                msg = {'content':'!work'}
                requests.post(url,headers=auth,data=msg)
                time.sleep(10)
            except Exception:
                continue
    time.sleep(14400)

