import requests
from flask import Flask, render_template, redirect, url_for, flash, request

ENDPOINT = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=INR&order=market_cap_desc&per_page=100&page=1&sparkline=false'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


@app.route("/")
def home():
    res = requests.get(ENDPOINT)
    coins = res.json()
    return render_template("index.html", coins=coins)

if __name__ == '__main__':
    app.run(debug=True)