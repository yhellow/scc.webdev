from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에 insert 하기

# 'users'라는 collection에 {'name':'bobby','age':21}를 넣습니다.
# CRUD 중 create하는 과정 (users라는 데이터를 만들어줌)
# 딕셔너리 하나를 밸류값으로 넣어줌
db.users.insert_one({'name': 'bobby', 'age': 21})
db.users.insert_one({'name': 'kay', 'age': 27})
db.users.insert_one({'name': 'john', 'age': 30})

# MongoDB에서 데이터 모두 보기
all_users = list(db.users.find())

# 참고) MongoDB에서 특정 조건의 데이터 모두 보기
same_ages = list(db.users.find({'age': 21}))

print(all_users[0])  # 0번째 결과값을 보기
print(all_users[0]['name'])  # 0번째 결과값의 'name'을 보기

# for user in all_users:  # 반복문을 돌며 모든 결과값을 보기
  #   print(user)

# name: john 과 동시에 age: 21 인 데이터 조회
john_data = list(
    db.users.find({
        'name': 'john',
        "age": 21
    })
)
# print(john_data)

user = db.users.find_one({"name":"bobby"})
print(user)

user = db.users.find_one({"name":"bobby"},{'_id':0, "name":0})
print (user)

db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
user = db.users.find_one({"name":'bobby'})
print(user)

db.users.delete_one({"name":"bobby"})
# print(user)