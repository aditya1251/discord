# from pymongo import MongoClient
# import time
# import threading
# from config import Your_data_base
import requests
import random

# password = 'QRFfsca9UaLUH9H2'
# cluster_url = 'mongodb+srv://uchisasuke468:' + \
#     password + '@cluster0.byr4qsl.mongodb.net/'

# client = MongoClient(cluster_url)

# db = client['BNSL']

# cli = Your_data_base

# data = db[cli]

url = "https://discord.com/api/v9/channels/1208474261992378428/messages"

msg_list = ['Go',"gpoo","lfg","dont loose hope in sir","keep grinding","need to be active to reach level 11","go to moon","thats amazing","i think everyone has been participating long time"]

auths = ['MTAxODUwOTgxMjc0NjY5MDY5Ng.GgG2yI.xQp0JNhSiUCFDqNx2nYMRxSmW_QQaGF5Da2JPs','MTAzNDcyNDE1ODAyMzY2MzYxNg.GhudA7.Z7fwQpvTaSWonFdWhATS680aXkm2YPKWogMj_M']

# def main2():
#     time.sleep(46400)
#     while True:
#         dat = data.find_one({'cli':cli})
#         if dat:
#             for aut in dat['auths']:
#                 try:
#                     auth = {'authorization':aut}
#                     msg = {'content':'!daily'}
#                     requests.post(url,headers=auth,data=msg)
#                     time.sleep(10)
#                 except Exception:
#                     continue
#         time.sleep(86400)

# time_thread = threading.Thread(target=main2)
# time_thread.start()

# def main3():
#     time.sleep(1800)
#     while True:
#         dat = data.find_one({'cli':cli})
#         if dat:
#             for aut in dat['auths']:
#                 try:
#                     auth = {'authorization':aut}
#                     msg = {'content':'!guess 10'}
#                     requests.post(url,headers=auth,data=msg)
#                 except Exception:
#                     continue
#             i = 1
#             while i <= 5:  
#                 for aut in dat['auths']:
#                     smsg2 = str(random.randrange(1,100))
#                     try:
#                         auth = {'authorization':aut}
#                         msg = {'content':smsg2}
#                         requests.post(url,headers=auth,data=msg)
#                     except Exception:
#                         pass
#                 i += 1
#                 time.sleep(62)
#         time.sleep(3600)

# time_thread = threading.Thread(target=main3)
# time_thread.start()

while True:
    for aut in auths:
        try:
            auth = {'authorization':aut}
            msg = {'content': random.choice(msg_list)}
            requests.post(url,headers=auth,data=msg)
        except Exception:
            continue

