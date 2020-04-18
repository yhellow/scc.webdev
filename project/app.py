from flask import Flask, jsonify
import requests

app = Flask(__name__)

apiHost = 'https://api.steamapis.com'
apiKey = '2139D73057CEFDB17BAD92F50E4D0CA4'


@app.route('/market/stats')
def market_stats():
    res = requests.get("{}/market/stats?api_key={}".format(apiHost, apiKey))
    data = res.json()
    return jsonify(data)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
