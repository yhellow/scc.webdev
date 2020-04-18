from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient, DESCENDING

app = Flask(__name__)
client = MongoClient("localhost", 27017)
db = client.dbsparta

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/list", methods=["GET"])
def movie_star_list():
    mystar = list(db.mystar.find({}, {"_id": 0}).sort([("like", DESCENDING)]))
    return jsonify(mystar)


@app.route("/api/like", methods=["POST"])
def movie_star_like():
    name_receive = request.form["name_give"]
    moviestar = db.mystar.find_one({"name": name_receive})
    moviestar_like = moviestar["like"]

    db.mystar.update_one({"name": name_receive}, {"$set": {"like": moviestar_like + 1}})
    return jsonify({"success": True})

@app.route("/api/delete", methods=["POST"])
def movie_star_delete():
    name_receive = request.form["name_give"]
    db.mystar.delete_one({"name": name_receive})
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)

