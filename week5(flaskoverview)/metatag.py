import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/memo', methods=["GET"])
def memo_get():
  memos = list(db.memo.find({}, {"_id": 0}))
  return jsonify(memos)

@app.route('/memo', methods=["POST"])
def memo_post():
  url_received = request.form.get('url', None)
  comment_received = request.form.get('comment', '')

  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get(url_received, headers=headers)
  soup = BeautifulSoup(data.text, 'html.parser')

  og_title = soup.select_one('meta[property="og:title"]')
  og_description = soup.select_one('meta[property="og:description"]')
  og_image = soup.select_one('meta[property="og:image"]')

  title = og_title["content"]
  description = og_description["content"]
  image = og_image["content"]

  db.memo.insert_one({
    "title": title,
    "description": description,
    "image": image,
    "url": url_received,
    "comment": comment_received
  })

  return jsonify({"success": True})

if __name__ == "__main__":
  app.run('0.0.0.0', port=5000, debug=True)