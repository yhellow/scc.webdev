import requests
url = '크롤링주소'
# 서버 우회 원할 시 headers 추가 
headers = {}
dataName = requests.get(url , headers= headers)
datajson = dataName.json()

from bs4 import BeautifulSoup
soup = BeautifulSoup(dataName.text, 'html.parser')
import random

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbName

from flask import Flask, render_template
app = Flask(__name__)
# flask codes
if __name__ == '__main__':
    app.run('0.0.0.0', port= 5000, deug= True)
