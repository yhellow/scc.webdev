from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient("localhost", 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.memoapp  # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memo', methods=["GET"])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    print = list(db.articles.find({},{'_id':0}))
    # 2. articles라는 키 값으로 영화정보 내려주기
    return jsonify({"result": "success", "articles": print})

@app.route('/memo', methods= ["POST"])
def saving():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    r = requests.get(url_receive, headers= headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    ogtitle = soup.select_one('meta[property="og:title"]')
    ogimage = soup.select_one('meta[property="og:image"]')
    ogdescription = soup.select_one('meta[property= "og:description"]')

    title = ogtitle['content']
    image = ogimage['content']
    description = ogdescription['content']

    article = {'url': url_receive, 'comment': comment_receive, 'title': title, 'image': image, 'description': description}

    db.articles.insert_one(article)

    return jsonify({'result': 'success'})

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)



# @app.route("/market/stats")
# def market_stats():
#     res = requests.get(
#         "{}/ISteamApps/GetAppList/v0002/?format=json&key={}".format(apiHost, apiKey)
#     )
#     data = res.json()

#     app_list = data["applist"]
#     apps = app_list["apps"]

#     for app in apps:
#         app_id = app["appid"]
#         app_res = requests.get(
#             "{}/api/appdetails?appids={}".format(apiDetailHost, app_id)
#         )
#         print(app_res.json())

#     return jsonify([])


# @app.route('/search', methods= ["POST"])
# def search_receive():
#     search_receive = request.form['search_give']
#     search = {'searchgame': search_receive}
#     db.searches.insert_one(search)

    # return jsonify({'result':'success', 'search':search_receive})