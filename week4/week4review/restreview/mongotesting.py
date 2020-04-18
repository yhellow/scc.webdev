from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.testingdb

# db.collectiona.insert_one({'fruit': 'grapes'})
# db.collectiona.insert_one({'fruit': 'apples'})
# db.collectiona.insert_one({'fruit':'pears'})
# db.collectiona.insert_one({'fruit':'bananas','quantity':1})

all_fruit = list(db.collectiona.find())
# print(all_fruit)
one_fruit = list(db.collectiona.find({"quantity": 1}))
print(one_fruit)
# print(one_fruit['fruit'])
