from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.sixthm

# print(db.mmovies.find_one({'ttitle': '가버나움'})['sstar'])
# matching = db.mmovies.find_one({"ttitle": "가버나움"})
# print (finding['sstar'])
matcher = db.mmovies.find_one({'ttitle':'베일리 어게인'})['sstar']
# print(matcher)

movies = list(db.mmovies.find({'sstar':matcher}))
# print (movies)
# for movie in movies:
#     print(movie['ttitle'])

for movie in movies:
    db.mmovies.update_many({'sstar':matcher},{'$set':{'sstar':0}})