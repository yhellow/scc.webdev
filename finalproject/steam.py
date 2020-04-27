import requests
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.projecttwo

apiHost = 'http://api.steampowered.com'
apiDetailHost = 'https://store.steampowered.com'
apiKey = '2139D73057CEFDB17BAD92F50E4D0CA4'
# apiKey = 'STEAMKEY'

def get_game_list():
    res = requests.get("{}/ISteamApps/GetAppList/v0002/?format=json&key={}".format(apiHost, apiKey))
    data = res.json()

    app_list = data["applist"]
    apps = app_list["apps"]

    for app in apps:
        app_id = app["appid"]
        name = app["name"]
        #app_id 가 정수일 경우 True 
        if isinstance(app_id, int):
            db.gameIds.insert_one({
                "app_id": app_id,
                "name": name
            })


def get_game_detail():
    games = list(db.gameIds.find({}, {'_id': 0}))
    # enumerate?
    for index, game in enumerate(games):
        app_id = game["app_id"]
        app_res = requests.get("{}/api/appdetails?appids={}".format(apiDetailHost, app_id))

        data = app_res.json()
        data_for_id = data[str(app_id)]
        success = data_for_id["success"]
        
        if success:
            game_data = data_for_id["data"]
            name = game_data["name"]
            # if not isinstance(price, int): 정수가 아닐 경우
            price = game_data.get('price_overview', 0)
            if not isinstance(price, int):
                price = price.get('final_formatted', 0)
            
            image = game_data.get('header_image', '')

            desc = game_data.get('short_description', '')

            genres = game_data.get('genres', [])

            db.games.insert_one({
                "name": name,
                "price": price,
                "image": image,
                "desc": desc,
                "genres": [genre.get('description') for genre in genres if genre.get('description') is not None]
            })

# instead of app.run('0.0.0.0', port= 5000, debug= True)
# 실행했을 때 get_game_detail() 함수 실행
if __name__ == "__main__":
    # get_game_list()
    get_game_detail()