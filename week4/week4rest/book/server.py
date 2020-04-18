from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    title_receive = request.form["title"]
    author_receive = request.form["author"]
    review_receive = request.form["review"]

    db.books.insert_one({
        "title": title_receive,
        "author": author_receive,
        "review": review_receive
    })

    # print(title_receive, author_receive, review_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    books = list(db.books.find({},{"_id":0}))



    return jsonify({
        'result': 'success',
        'msg': '이 요청은 GET!',
        'data': books
    })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
