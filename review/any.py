import requests
from bs4 import BeautifulSoup
import random
from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


url = ''
headers = {User-Agent, ..}
r = requests.get(url, headers= headers)
rjson = r.json()
soup = BeautifulSoup(r.text, 'html.parser')

client = MongoClient('localhost', 27017)
db = client.dbName

@app.route('/', methods=['GET'])
def home:
    return render_template('index.html')

@app.route('/apiName', methods= ['POST'])
def apiroute:


if __name__ = '__main__':
    app.run('0.0.0.0', port= 5000, debug= True)