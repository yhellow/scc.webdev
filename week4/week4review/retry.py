# import requests
# r = requests.get('주소')
# rjson = r.json()

# from bs4 import BeautifulSoup

# from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client.dbname

from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.retrydb

# db.retrycol.insert_one({'name':'james', 'computer': 'mac', 'processor':'ios'})
# db.retrycol.insert_one({'name':'alex', 'computer': 'window', 'processor':'window10'})
# db.retrycol.insert_one({'name':'simon', 'computer': 'window', 'processor':'window10'})
# db.retrycol.insert_one({'name':'lisa', 'computer': 'mac', 'processor':'ios'})

all_retrycol = list(db.retrycol.find())
# print (all_retrycol)

only_processor = list(db.retrycol.find({"processor": "ios"}))
# print(only_processor)
# only_processor = list(db.retrycol.find([2]))
# 1. list를 명시하면서 그 속에서 특정 키 값의 밸류 값을 나타내기 힘듦
# print(only_processor)
# print(all_retrycol[0]["processor"])
# 2. print에서 특정 키 값으로 밸류 추출 가능

# for retries in all_retrycol:
    # print(retries)

# 리스트를 만들지 않고도 특정값 뽑기
onejames = db.retrycol.find_one({'name':'james'})
# print (onejames)

# db.retrycol.update_many({'processor':'ios'},{'$set': {'processor': 'catalina'}})
# db.retrycol.update_one({'processor':'catalina'},{'$set': {'processor': 'ios'}})

# db.retrycol.delete_one({'name':'james'})
# db.retrycol.delete_many({'computer':'window'})
