from pymongo import MongoClient
import time
import threading
from config import Your_data_base
import requests
password = 'QRFfsca9UaLUH9H2'
cluster_url = 'mongodb+srv://uchisasuke468:' + \
    password + '@cluster0.byr4qsl.mongodb.net/'

client = MongoClient(cluster_url)

db = client['BNSL']

cli = Your_data_base

data = db[cli]

url = "https://discord.com/api/v9/channels/1144174264128389181/messages"

while True:
    dat = data.find_one({'cli':cli})
    if dat:
        for aut in dat['auths']:
            try:
                d2 = data.find_one({'xyz':auth})
                if d2:
                    last = d2['last_time'] + 7200
                    current_time = time.time()
                    if current_time >= last:
                        auth = {'authorization':aut}
                        msg = {'content':'!work'}
                        requests.post(url,headers=auth,data=msg)
                        data.update_one({'xyz':auth},{'$set':{'last_time':current_time}})
                else:
                    auth = {'authorization':aut}
                    msg = {'content':'!work'}
                    requests.post(url,headers=auth,data=msg)
                    data.update_one({'xyz':auth},{'$set':{'last_time':current_time}},upsert=True)
            except Exception as e:
                print(e)
                continue
            time.sleep(10)
    time.sleep(60)
