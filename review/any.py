import requests
from bs4 import BeautifulSoup
import random
from pymongo import MongoClient
client = MongoClient('localhost', 27117)
db = client.dbName
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


# @app.route('/', methods= ['POST'/'GET'])
def home():
    return render_template('any.js')    

@app.route('/apiName')
def saving:
    render_template('any.js')



if __name__ = '__main__':
    app.run('0.0.0.0', port= 5000, debug= True)

