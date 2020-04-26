from flask import Flask, jsonify, render_template, request
import requests
from bs4 import BeautifulSoup
import random
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.projecttwo

app = Flask(__name__)

apiHost = "http://api.steampowered.com"
apiKey = "2139D73057CEFDB17BAD92F50E4D0CA4"
apiDetailHost = "https://store.steampowered.com"
# apiKey = 'STEAMKEY'

@app.route("/")
def home():
    return render_template("index.html")

# 페이지 바꿔서 다시 해볼 것
@app.route("/home", methods=["GET"])
def trendingshow():
    url = "https://store.steampowered.com/games/#p=0&tab=ConcurrentUsers"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    r = requests.get(url, headers= headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    recs = soup.select('#ConcurrentUsersRows>a')

    data = []
    for rec in recs:
        gameurl = rec["href"]

        titleTag = rec.select('.tab_item_name')[0]
        imageTag = rec.select('img')[0]
        priceTag = rec.select('.discount_final_price')[0]

        tags = ''.join([tag.text for tag in rec.select('.top_tag')])

        res = requests.get(gameurl, headers= headers)
        resSoup = BeautifulSoup(res.text, 'html.parser')

        descriptionTag = resSoup.select('.game_description_snippet')
        reviewTag = resSoup.select('.game_review_summary')

        title = titleTag.text
        image = imageTag["src"]
        price = priceTag.text

        try:
            desc = descriptionTag[0].text
        except:
            desc = ''

        try:
            review = reviewTag[0].text
        except:
            review = ''

        data.append({
            'title': title,
            'image': image,
            'desc': desc,
            'review': review,
            'price': price,
            'url': gameurl,
            'tag': tags
        })

        # db.trendinggames.insert_one({'image':image, 'title':title})  

    randomtrending = random.sample(data, 3)
    # alltrending = list(db.trendinggames.find({},{'_id':0}))
    # randomtrending = random.choice(alltrending)
    # threetrending = list(randomtrending)

    return jsonify ({"result":"success", "trending": randomtrending})

@app.route('/random', methods= ["GET"])
def randompick():
    gameslist = list(db.games.find({}, {'_id':0})) 
    randomgame = random.choice(gameslist)

    return jsonify ({'result':'success', 'randomgame': randomgame})

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)



    # recs = soup.find('div', class_= "carousel_items")
    # rec = recs.find_all('div', class_= "appTitle")    