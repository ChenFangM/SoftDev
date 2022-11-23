"""
Crocs (Fang Chen, Ziying Jian)
Softdev
K20 -- A RESTful Journey Skyward
2022-11-22
time spent: .7 hr
"""

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def display():
  key = open('key.txt', 'r').read()  # reads the key
  # print(key)
  url = "https://api.myanimelist.net/v2/anime/ranking" #  url format
  # print(url)
  data = json.loads(requests.get(url).text)  # open the url and then using json.load to convert the page to a json file
  # print(data)
  return render_template('main.html', content=data["error"])

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()