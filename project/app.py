from flask import Flask, jsonify
import requests

app = Flask(__name__)

apiHost = 'http://api.steampowered.com'
apiKey = '2139D73057CEFDB17BAD92F50E4D0CA4'

apiDetailHost = 'https://store.steampowered.com'


@app.route('/market/stats')
def market_stats():
    res = requests.get("{}/ISteamApps/GetAppList/v0002/?format=json&key={}".format(apiHost, apiKey))
    data = res.json()

    app_list = data["applist"]
    apps = app_list["apps"]

    for app in apps:
        app_id = app["appid"]
        
        app_res = requests.get("{}/api/appdetails?appids={}".format(apiDetailHost, app_id))

        print(app_res.json())

    return jsonify([])


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
