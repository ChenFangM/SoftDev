# Bottlers (Jeff Chen, Yusha Aziz, Fang Chen)	
# SoftDev
# K14 - Serving Looks
# October 19 2022
# time spent: 0.5 hrs

from flask import Flask, render_template
app = Flask(__name__) 

@app.route("/")       
def display():
  return render_template('index.html')

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
